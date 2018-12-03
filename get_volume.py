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

volcmd = "amixer -D pulse sget Master | grep 'Front Left:'"
print("> " + volcmd, file=sys.stderr)

cmdout = subprocess.getoutput(volcmd).strip()

print("\t%s" % cmdout, file=sys.stderr)

first_brack = cmdout.find("[")
second_brack = cmdout.find("]", first_brack)
vollvl = int(cmdout[first_brack+1:second_brack-1])
print("Level:", vollvl, file=sys.stderr)

third_brack = cmdout.find("[", second_brack)
fourth_brack = cmdout.find("]", third_brack)
muted = cmdout[third_brack+1:fourth_brack] == "off"
print("Muted:", muted, file=sys.stderr)

# pamixer --get-mute returns false when sound is on and true otherwise ..
if vollvl == 0:
    col = "red"
else:
    vollvl = vollvl // 50 # [0,2]
    col = "red" if muted else "white"

out = "<icon=%s/>"
toggle_vol = "<action=`xdotool key XF86AudioMute` button=1>%s</action>"
raise_vol = "<action=`xdotool key XF86AudioRaiseVolume` button=4>%s</action>"
lower_vol = "<action=`xdotool key XF86AudioLowerVolume` button=5>%s</action>"

print(lower_vol % raise_vol % toggle_vol % out % writesoundxpm(vollvl, col))
