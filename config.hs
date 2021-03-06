-- boilerplate {{{
{-# LANGUAGE ExistentialQuantification, NoMonomorphismRestriction, TypeSynonymInstances #-}
{-# OPTIONS_GHC -fno-warn-missing-signatures -fno-warn-type-defaults #-}

-- system imports
import Control.Applicative
import Control.Monad
import Control.Monad.Trans
import Data.Char
import Data.List
import Data.Map (Map, fromList)
import Data.Ratio
import Data.Word
import GHC.Real
import System.Environment
import System.Exit
import System.IO
import System.Process

import System.Directory

-- xmonad core
import XMonad
import XMonad.StackSet hiding (workspaces)

-- xmonad contrib
import XMonad.Actions.CycleWS
import XMonad.Actions.CycleWindows
import XMonad.Actions.SpawnOn
import XMonad.Actions.Warp
import XMonad.Config.Azerty
import XMonad.Config.Gnome
import XMonad.Hooks.DynamicLog
import XMonad.Hooks.ManageDocks
import XMonad.Hooks.ManageHelpers
import XMonad.Layout.Grid
import XMonad.Layout.IndependentScreens
import XMonad.Layout.Magnifier
import XMonad.Layout.NoBorders
import XMonad.Util.Cursor
import XMonad.Util.Dzen hiding (x, y)
import XMonad.Util.EZConfig
import XMonad.Util.Run
import XMonad.Util.SpawnOnce
import XMonad.Util.WorkspaceCompare
-- }}}
-- applications to use {{{
myEditor   = "atom"
myTerminal = "terminator"
myCompmgr  = "xcompmgr -fF -D 1 -I 0.56 -O 0.6"
myBrowser  = "firefox --password-store=gnome"
myDropdown = "guake"
myFilemgr  = "nautilus"
myLock     = "i3lock-fancy -p"
myOnboard  = "onboard"
-- }}}
-- utils {{{
showBar str = do
    dzenConfig (timeout 1 >=> onCurr xScreen) str

capitalized :: String -> String
capitalized (head:tail) = toUpper head : map toLower tail
capitalized [] = []
-- }}}
-- convenient actions {{{
centerMouse () = warpToWindow (1/2) (1/2)
viewShift  i   = view i . shift i
floatAll       = composeAll . map (\s -> className =? s --> doFloat)
-- }}}
-- some consts {{{
altMask = mod1Mask
bright  = "#80c0ff"
dark    = "#13294e"
grey    = "#ababab"
white   = "#ffffff"
-- }}}
-- main {{{
myWS = [ "show_editor", "show_browser", "show_pdf"  , "show_console", "show_misc1",
         "show_misc2" , "show_misc3"  , "show_misc4", "show_music"  , "show_mail" ]
dmwitConfig nScreens = docks $ def {
    borderWidth             = 2,
    workspaces              = myWS,
    terminal                = myTerminal,
    normalBorderColor       = dark,
    focusedBorderColor      = bright,
    modMask                 = mod4Mask,
    keys                    = \c -> keyBindings c <+> azertyKeys c <+> keys defaultConfig c,
    layoutHook              = magnifierOff $ avoidStruts (GridRatio 0.9) ||| noBorders Full,
    manageHook              = ( isFullscreen --> doFullFloat )
                          <+> floatAll["Shutter", capitalized myDropdown]
                          <+> manageHook defaultConfig
                          <+> manageDocks,
    logHook                 = allPPs (),
    startupHook             =
                              setDefaultCursor xC_left_ptr >> refresh
                           >> mapM_ (spawnHere . xmobarCommand) [0 .. nScreens-1]
                           >> spawnOnce myCompmgr
                           >> spawnOnce "feh --bg-scale ~/.xmonad/wallpaper.jpg"
                           >> spawnOnce "touchegg"
                           >> spawnOnce "libinput-gestures -c ~/.xmonad/libgestures.conf"
                           >> spawnOnce myDropdown
                           >> spawnOnce "setxkbmap -layout fr,us -option 'grp:ctrls_toggle'"
    }
    `additionalKeysP`
    [ ("<XF86AudioMute>"         , spawn "amixer -q -D pulse sset Master toggle")
    , ("<XF86AudioRaiseVolume>"  , spawn "amixer -q -D pulse sset Master 2000+ unmute")
    , ("<XF86AudioLowerVolume>"  , spawn "amixer -q -D pulse sset Master 2000- unmute")
    , ("<XF86MonBrightnessUp>"   , spawn "~/.xmonad/change_brightness inc 50")
    , ("<XF86MonBrightnessDown>" , spawn "~/.xmonad/change_brightness dec 50")
    , ("<XF86AudioPlay>"         , showBar "Music: Play" <+> spawn "playerctl play-pause")
    , ("<XF86AudioStop>"         , showBar "Music: Stop" <+> spawn "playerctl stop")
    , ("<XF86AudioPrev>"         , showBar "Music: Prev" <+> spawn "playerctl previous")
    , ("<XF86AudioNext>"         , showBar "Music: Next" <+> spawn "playerctl next")
    ]

main = countScreens >>= xmonad . dmwitConfig
-- }}}
-- keybindings {{{
keyBindings conf = let m = modMask conf in fromList . anyMask $ [
    ((m                , xK_o          ), sendMessage Toggle),

    ((m                , xK_Up         ), prevScreen),
    ((m                , xK_Down       ), nextScreen),
    ((m .|. shiftMask  , xK_Tab        ), moveTo Prev HiddenWS),
    ((m                , xK_Tab        ), moveTo Next HiddenWS),
    ((m                , xK_Left       ), moveTo Prev HiddenWS),
    ((m                , xK_Right      ), moveTo Next HiddenWS),
    ((m .|. shiftMask  , xK_Up         ), shiftPrevScreen),
    ((m .|. shiftMask  , xK_Down       ), shiftNextScreen),
    ((m .|. shiftMask  , xK_Left       ), shiftToPrev),
    ((m .|. shiftMask  , xK_Right      ), shiftToNext),
    ((m                , xK_z          ), toggleWS),

    ((m .|. altMask    , xK_Left       ), rotFocusedUp     >> centerMouse ()),
    ((m .|. altMask    , xK_Right      ), rotUnfocusedDown >> centerMouse ()),

    ((m                , xK_a          ), spawnHere myEditor),
    ((m                , xK_s          ), spawnHere myBrowser),
    ((m                , xK_f          ), spawnHere myFilemgr),
    ((m                , xK_k          ), spawnHere myOnboard),

    ((m                , xK_g          ), spawnHere myLock)
    ] ++ [
    ((m .|. e          , key           ), windows (f ws))
    | (key, ws) <- zip [xK_1..xK_9] myWS
    , (e, f)    <- [(0, greedyView), (shiftMask, viewShift)]
    ]

anyMask xs = do
    ((mask, key), action) <- xs
    extraMask             <- [0, controlMask, altMask, controlMask .|. altMask]
    return ((mask .|. extraMask, key), action)
-- }}}
-- logHook {{{
xmobarCommand (S s) = unwords ["xmobar",
    "-x", show s,
    "-t", template s,
    "-i", "`echo $HOME`/.xmonad/xpm",
    "~/.xmonad/.xmobarrc"
    ]
    where
    template 0  = "\"  %time%}{" ++ common ++ "\""
    template s_ = "\"  %multicpu% · %memory% · %dynnetwork%}%date%{" ++ common ++ "\""
    common = "%kbd% · %wired% · %wireless% · %bluetooth% · %volume% · %battery% · %workspaces%  "

getPipeName () = do
  homePath <- getHomeDirectory
  return $ homePath ++ "/.xmonad/pipe-workspaces"

allPPs () = sequence_ [dynamicLogWithPP pp | pp <- [ppWorkspaces]]
color c = xmobarColor c ""

ppWorkspaces = def
    { ppCurrent           = \s -> color "red" s
    , ppVisible           = color "pink"
    , ppHidden            = color grey
    , ppHiddenNoWindows   = color dark
    , ppOrder             = \(wss:_layout:_title:_) -> [wss]
    , ppSort              = getSortByIndex
    , ppOutput            = \s -> pipeName >>= (\path -> writeFile path s)
    }
    where pipeName = getPipeName ()
-- }}}
-- startupHook {{{
-- }}}
