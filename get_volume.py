#!/usr/bin/env python3

sound_xpm = \
[
    [
        "\"                \",",
        "\"                \",",
        "\"      ..        \",",
        "\"     ....       \",",
        "\"    .....       \",",
        "\" ........       \",",
        "\".........       \",",
        "\".........       \",",
        "\".........       \",",
        "\".........       \",",
        "\" ........       \",",
        "\"    .....       \",",
        "\"     ....       \",",
        "\"      ..        \",",
        "\"                \",",
        "\"                \","
    ],
    [
        "\"                \",",
        "\"                \",",
        "\"      ..        \",",
        "\"     ....       \",",
        "\"    .....       \",",
        "\" ........       \",",
        "\"......... .     \",",
        "\".........  .    \",",
        "\".........  .    \",",
        "\"......... .     \",",
        "\" ........       \",",
        "\"    .....       \",",
        "\"     ....       \",",
        "\"      ..        \",",
        "\"                \",",
        "\"                \","
    ],
    [
        "\"                \",",
        "\"                \",",
        "\"      ..        \",",
        "\"     ....       \",",
        "\"    .....   .   \",",
        "\" ........    .  \",",
        "\"......... .   . \",",
        "\".........  .  . \",",
        "\".........  .  . \",",
        "\"......... .   . \",",
        "\" ........    .  \",",
        "\"    .....   .   \",",
        "\"     ....       \",",
        "\"      ..        \",",
        "\"                \",",
        "\"                \","
    ],
]

from utils import writexpm
from os.path import expanduser

def writesoundxpm(lvl, col):
    url = expanduser("~/.xmonad/xpm/sound_%d_%%s.xpm") % lvl

    return writexpm(url, sound_xpm[lvl], col)

import sys, subprocess

volcmd = "pamixer --get-volume"
print("> " + volcmd, file=sys.stderr)

vollvl = int(subprocess.getoutput(volcmd)) # [0,100]
print(vollvl, end=" ", file=sys.stderr)
print(vollvl, file=sys.stderr)

volmutecmd = "pamixer --get-mute"
print("> " + volmutecmd, file=sys.stderr)

# pamixer --get-mute returns false when sound is on and true otherwise ..
if vollvl == 0:
    col = "red"
else:
    vollvl = vollvl // 50 # [0,2]
    muted = subprocess.getoutput(volmutecmd) == "true"
    col = "red" if muted else "white"
print(muted, file=sys.stderr)

out = "<icon=%s/>"
toggle_vol = "<action=`xdotool key XF86AudioMute` button=1>%s</action>"
raise_vol = "<action=`xdotool key XF86AudioRaiseVolume` button=4>%s</action>"
lower_vol = "<action=`xdotool key XF86AudioLowerVolume` button=5>%s</action>"

print(lower_vol % raise_vol % toggle_vol % out % writesoundxpm(vollvl, col))
