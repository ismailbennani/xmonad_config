![Screenshot](screenshot.jpg)

This is my personal config files, feel free to use them as you like.

They are tested with 1 and 2 monitors, but they should work with more since they are based on [dmwit's screen count independent config](https://wiki.haskell.org/Xmonad/Config_archive/dmwit%27s_xmonad.hs).

All the files in this repo should go under `~/.xmonad`.

# Usage

(Installation procedure tested on a fresh install of Ubuntu 18.10)

### `xmonad`

```
apt install xmonad suckless-tools
```

### `xmobar`

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
