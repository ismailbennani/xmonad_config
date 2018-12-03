import os, os.path

def writexpm(xpm_url, xpm, col):
    xpm_url = xpm_url % col

    if not os.path.exists(xpm_url):
        os.makedirs(os.path.dirname(xpm_url), exist_ok=True)

        content = \
        [ "/* XPM */",
          "static char * xpm[] = {",
          "\"16 16 2 1\",",
          "\" 	c None\",",
          "\".	c %s\"," % col
        ] + xpm + [ "}" ]

        file = "\n".join(content)

        with open(xpm_url, "w+") as f: f.write(file)

    return xpm_url
