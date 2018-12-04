![Screenshot](screenshot.jpg)

This is my personal config files, feel free to use them as you like.

They are tested with 1 and 2 monitors, but they should work with more since they are based on [dmwit's screen count independent config](https://wiki.haskell.org/Xmonad/Config_archive/dmwit%27s_xmonad.hs).

All the files in this repo should go under `~/.xmonad`.

# Usage

(Installation procedure tested on a fresh install of Ubuntu 18.10)

### `xmonad` ([website](https://xmonad.org/))

```
apt install xmonad
```

### `xmobar` ([github](https://github.com/jaor/xmobar))

Requirements

```
apt install git cabal-install libasound2-dev libiw-dev libxpm-dev c2hs
cabal update
echo "export PATH=\$PATH:$HOME/.cabal/bin" >> ~/.profile
```

Install from sources

```
git clone https://github.com/jaor/xmobar.git
cd xmobar
cabal install --flags="all_extensions"
```

(you need to reload your `~/.profile` either by logging off and on or by running `export ~/.profile` in every terminal)

### Finally

Clone this repo in `~/.xmonad`

```
cd ~/
git clone https://github.com/ismailbennani/xmonad_config.git .xmonad
```

Log out from the current session and log back into XMonad.

* Optional: Applications I use in the configuration file:

  - `terminator` ([website](https://launchpad.net/terminator)): terminal emulator
  - `xdotool` ([github](https://github.com/jordansissel/xdotool)): fake keyboard/mouse input (used in `xmobad` and `libinput-gestures`)
  - `suckless-tools` ([website](http://tools.suckless.org/)): provides `dmenu`, a command launcher used by `xmonad` (super+p shortcut)
  - `gmrun` ([website](https://sourceforge.net/projects/gmrun/)): another command launcher (super+shift+p shortcut)
  - `xcompmgr` ([gitlab](https://gitlab.freedesktop.org/xorg/app/xcompmgr)): composition manager
  - `feh` ([website](https://feh.finalrewind.org/)): set wallpaper
  - `touchegg` ([github](https://github.com/JoseExposito/touchegg)) and `libinput-gestures` ([github](https://github.com/bulletmark/libinput-gestures)): touchpad and touchscreen gestures
  - `guake` ([github](https://github.com/Guake/guake)): drop-down terminal
  - `playerctl` ([github](https://github.com/acrisci/playerctl)): media players control
  - `onboard` ([website](https://launchpad.net/onboard)): onscreen keyboard

APT command to install (almost) everything

```
apt install terminator suckless-tools xdotool xcompmgr feh touchegg guake playerctl onboard
```

`atom` installation [here](https://atom.io/)

`libinput-gestures` installation [here](https://github.com/bulletmark/libinput-gestures)

You also need to put `touchegg.conf` in `~/.config/touchegg`.
