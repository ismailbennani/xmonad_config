#!/usr/bin/env python3

wired_xpm =\
[
    "\"                \",",
    "\"          .     \",",
    "\"         . .    \",",
    "\"        .   .   \",",
    "\"       .     .  \",",
    "\"      . .. .. . \",",
    "\"         . .    \",",
    "\"      .  . .    \",",
    "\"     . . . .    \",",
    "\"     . .  .     \",",
    "\"     . .        \",",
    "\"  . .. .. .     \",",
    "\"   .     .      \",",
    "\"    .   .       \",",
    "\"     . .        \",",
    "\"      .         \",",
]

from utils import writexpm
from os.path import expanduser
import sys, subprocess

def get_wired_interface():
    interfaces = subprocess.getoutput("ls /sys/class/net").split()
    interfaces = [i for i in interfaces if i[:2] == "en"]
    print("Wired interfaces:", interfaces, file=sys.stderr)

    for i in interfaces:
        active = subprocess.getoutput("cat /sys/class/net/%s/operstate" % i) == "up"
        if active:
            return " "+i

    return None

url = expanduser("~/.xmonad/xpm/wired_%s.xpm")

active_if = get_wired_interface()
print("Connected through", active_if, file=sys.stderr)

col = "white"

if active_if is None:
    active_if = ""
    col = "red"

out = "<icon=%%s/>%s" % active_if

print(out % writexpm(url, wired_xpm, col))
