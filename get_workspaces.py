#!/usr/bin/env python3

from sys import stderr
import os.path

editor_xpm = \
[
    "\"                \",",
    "\"                \",",
    "\"................\",",
    "\".              .\",",
    "\".              .\",",
    "\".  ..........  .\",",
    "\".              .\",",
    "\".              .\",",
    "\".  ..........  .\",",
    "\".              .\",",
    "\".              .\",",
    "\".  ....        .\",",
    "\".              .\",",
    "\"................\",",
    "\"                \",",
    "\"                \","
]

browser_xpm = \
[
    "\"                \"",
    "\"                \"",
    "\"................\"",
    "\".              .\"",
    "\". ...  ..  ..  .\"",
    "\".  .. ...  ..  .\"",
    "\".  .. ... ..   .\"",
    "\".  .. ......   .\"",
    "\".  .... ....   .\"",
    "\".   ... ....   .\"",
    "\".   ... ...    .\"",
    "\".   ...  ..    .\"",
    "\".              .\"",
    "\"................\"",
    "\"                \"",
    "\"                \""
]

console_xpm = \
[
    "\"                \",",
    "\"                \",",
    "\"................\",",
    "\".              .\",",
    "\".              .\",",
    "\".  .           .\",",
    "\".   .          .\",",
    "\".    .  .....  .\",",
    "\".   .          .\",",
    "\".  .           .\",",
    "\".              .\",",
    "\".              .\",",
    "\".              .\",",
    "\"................\",",
    "\"                \",",
    "\"                \","
]

pdf_xpm = \
[
    "\"                \",",
    "\"                \",",
    "\"................\",",
    "\".              .\",",
    "\".              .\",",
    "\".  ..    .  .. .\",",
    "\". .  .   . .   .\",",
    "\". .  .   . .   .\",",
    "\". ...  ... ... .\",",
    "\". .   .  . .   .\",",
    "\". .   .  . .   .\",",
    "\". .    ... .   .\",",
    "\".              .\",",
    "\"................\",",
    "\"                \",",
    "\"                \", "
]

mail_xpm = \
[
    "\"                \",",
    "\"                \",",
    "\"................\",",
    "\"...          ...\",",
    "\". ..        .. .\",",
    "\".  ..      ..  .\",",
    "\".   ..    ..   .\",",
    "\".    ..  ..    .\",",
    "\".     ....     .\",",
    "\".      ..      .\",",
    "\".              .\",",
    "\".              .\",",
    "\".              .\",",
    "\"................\",",
    "\"                \",",
    "\"                \","
]

from utils import writexpm
from os.path import expanduser

def writeworkspacexpm(xpm, name, col):
    url = expanduser("~/.xmonad/xpm/%s_%%s.xpm") % name

    return writexpm(url, xpm, col)

def ws_renaming(name, col):
    if name == "editor" :
        return "<action=xdotool key super+ampersand><icon=%s/></action>"\
                % writeworkspacexpm(editor_xpm, "editor", col)
    if name == "browser":
        return "<action=xdotool key super+eacute><icon=%s/></action>"\
                % writeworkspacexpm(browser_xpm, "browser", col)
    if name == "pdf"    :
        return "<action=xdotool key super+quotedbl><icon=%s/></action>"\
                % writeworkspacexpm(pdf_xpm, "pdf", col)
    if name == "console":
        return "<action=xdotool key super+apostrophe><icon=%s/></action>"\
                % writeworkspacexpm(console_xpm, "console", col)
    if name == "misc1"  :
        return "<action=xdotool key super+parenleft><fc=%s>α</fc></action>"\
                % col
    if name == "misc2"  :
        return "<action=xdotool key super+minus><fc=%s>β</fc></action>"\
                % col
    if name == "misc3"  :
        return "<action=xdotool key super+egrave><fc=%s>γ</fc></action>"\
                % col
    if name == "misc4"  :
        return "<action=xdotool key super+underscore><fc=%s>δ</fc></action>"\
                % col
    if name == "music"  :
        return "<action=xdotool key super+ccedilla><fc=%s>♫</fc></action>"\
                % col
    if name == "mail"   :
        return "<action=xdotool key super+agrave><icon=%s/></action>"\
                % writeworkspacexpm(mail_xpm, "mail", col)


def make_name(col,name):
    if name[:5] != "show_":
        return ""

    return ws_renaming(name[5:], col)

workspaces = open(expanduser("~/.xmonad/pipe-workspaces"), "r").read().strip()
ws_decls = workspaces.split()

ws_formatted = []

for ws in ws_decls:

    begcolpos = ws.find("=") + 1
    endcolpos = ws.find(">", begcolpos)
    color = ws[begcolpos:endcolpos]

    begnamepos = endcolpos + 1
    endnamepos = ws.find("<", begnamepos)
    name = ws[begnamepos:endnamepos]

    ws_formatted.append((color, name))

final = [make_name(ws_formatted[i][0], ws_formatted[i][1])
         for i in range(10)]

print(" ".join(final))
