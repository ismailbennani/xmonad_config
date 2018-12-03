#!/usr/bin/env python3

bltxpm =\
[
    "\"       .        \",",
    "\"       ..       \",",
    "\"       ...      \",",
    "\"    .  ....     \",",
    "\"    .. . ...    \",",
    "\"     ... ...    \",",
    "\"      .....     \",",
    "\"       ...      \",",
    "\"       ...      \",",
    "\"      .....     \",",
    "\"     ... ...    \",",
    "\"    .. . ...    \",",
    "\"    .  ....     \",",
    "\"       ...      \",",
    "\"       ..       \",",
    "\"       .        \",",
]

def get_connected_device():
    btdevices = subprocess.getoutput("bt-device -l").split("\n")
    names = [dev.split()[0] for dev in btdevices]

    for dev in names:
        info = subprocess.getoutput("bt-device -i %s" % dev)
        for line in info.split("\n"):
            if line.strip()[:9] == "Connected" and line.strip()[11] == "1":
                return " " + dev

    return None

from utils import writexpm
from os.path import expanduser

def writebltxpm(col):
    url = expanduser("~/.xmonad/xpm/bluetooth_%s.xpm")

    return writexpm(url, bltxpm, col)

import sys, subprocess

status = subprocess.getoutput("bluetooth")[12:] == "on"
print("Enabled:", status, file=sys.stderr)

col = "white" if status else "red"

name = get_connected_device()
print("Connected to %s" % name, file=sys.stderr)

if name is None:
    name = ""

out = "<icon=%s/>%s"
toggle = "<action=`bluetooth toggle` button=1>%s</action>"
ctl = "<action=`terminator -e bluetoothctl` button=3>%s</action>"

print(ctl % toggle % out % (writebltxpm(col), name))
