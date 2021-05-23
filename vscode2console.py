import sys
import json
from os import path


modes = {
    'term': {
        'ext': 'json'
    },
    'cmd': {
        'ext': 'ini'
    },
    'cyg': {
        'ext': 'minttyrc'
    },
    'putty': {
        'ext': 'reg'
    },
    'gnome': {
        'ext': 'sh'
    }
}

if (len(sys.argv) != 3
        or not any(mode in sys.argv for mode in modes.keys())
        or not path.exists(sys.argv[2])):
    print('[error] invalid argument(s)')
    acceptedModes = ' | '.join(modes.keys())
    print(
        f'[usage] {sys.argv[0]} <{acceptedModes}> <theme.json>')
    exit(1)


def hex2rgb(src):
    hexSrc = src.lstrip('#')
    rgbSrc = list(int(hexSrc[i:i+2], 16) for i in (0, 2, 4))
    return rgbSrc

def hex2rgba(src):
    hexSrc = src.lstrip('#')
    rgbaSrc = list(int(hexSrc[i:i+2], 16) for i in (0, 2, 4, 6))
    if rgbaSrc[3] > 1: rgbaSrc[3] /= 100
    return rgbaSrc

def rgba2rgb(bg, src):
    rgbBg = hex2rgb(bg)
    rgbSrc = hex2rgba(src)

    r = int(((1 - rgbSrc[3]) * rgbBg[0]) + (rgbSrc[3] * rgbSrc[0]))
    g = int(((1 - rgbSrc[3]) * rgbBg[1]) + (rgbSrc[3] * rgbSrc[1]))
    b = int(((1 - rgbSrc[3]) * rgbBg[2]) + (rgbSrc[3] * rgbSrc[2]))

    return '#%02x%02x%02x' % (r, g, b)

def rgbList(colorHex):
    return str(hex2rgb(colorHex)).strip('[]').replace(' ', '')


colorMap_term = {
    'cursorColor':                'terminalCursor.foreground',
    'selectionBackground':        'terminal.selectionBackground',
    'background':                 'terminal.background',
    'foreground':                 'terminal.foreground',
    'black':                      'terminal.ansiBlack',
    'blue':                       'terminal.ansiBlue',
    'cyan':                       'terminal.ansiCyan',
    'green':                      'terminal.ansiGreen',
    'purple':                     'terminal.ansiMagenta',
    'red':                        'terminal.ansiRed',
    'white':                      'terminal.ansiWhite',
    'yellow':                     'terminal.ansiYellow',
    'brightBlack':                'terminal.ansiBrightBlack',
    'brightBlue':                 'terminal.ansiBrightBlue',
    'brightCyan':                 'terminal.ansiBrightCyan',
    'brightGreen':                'terminal.ansiBrightGreen',
    'brightPurple':               'terminal.ansiBrightMagenta',
    'brightRed':                  'terminal.ansiBrightRed',
    'brightWhite':                'terminal.ansiBrightWhite',
    'brightYellow':               'terminal.ansiBrightYellow'
}

colorMap_cmd = {
    'DARK_BLACK':                 'terminal.ansiBlack',
    'DARK_BLUE':                  'terminal.ansiBlue',
    'DARK_CYAN':                  'terminal.ansiCyan',
    'DARK_GREEN':                 'terminal.ansiGreen',
    'DARK_MAGENTA':               'terminal.ansiMagenta',
    'DARK_RED':                   'terminal.ansiRed',
    'DARK_WHITE':                 'terminal.ansiWhite',
    'DARK_YELLOW':                'terminal.ansiYellow',
    'BRIGHT_BLACK':               'terminal.ansiBrightBlack',
    'BRIGHT_BLUE':                'terminal.ansiBrightBlue',
    'BRIGHT_CYAN':                'terminal.ansiBrightCyan',
    'BRIGHT_GREEN':               'terminal.ansiBrightGreen',
    'BRIGHT_MAGENTA':             'terminal.ansiBrightMagenta',
    'BRIGHT_RED':                 'terminal.ansiBrightRed',
    'BRIGHT_WHITE':               'terminal.ansiBrightWhite',
    'BRIGHT_YELLOW':              'terminal.ansiBrightYellow'
}

colorMap_cyg = {
    'BackgroundColour':           'terminal.background',
    'ForegroundColour':           'terminal.foreground',
    'CursorColour':               'terminalCursor.foreground',
    'Black':                      'terminal.ansiBlack',
    'BoldBlack':                  'terminal.ansiBrightBlack',
    'Red':                        'terminal.ansiRed',
    'BoldRed':                    'terminal.ansiBrightRed',
    'Green':                      'terminal.ansiGreen',
    'BoldGreen':                  'terminal.ansiBrightGreen',
    'Yellow':                     'terminal.ansiYellow',
    'BoldYellow':                 'terminal.ansiBrightYellow',
    'Blue':                       'terminal.ansiBlue',
    'BoldBlue':                   'terminal.ansiBrightBlue',
    'Magenta':                    'terminal.ansiMagenta',
    'BoldMagenta':                'terminal.ansiBrightMagenta',
    'Cyan':                       'terminal.ansiCyan',
    'BoldCyan':                   'terminal.ansiBrightCyan',
    'White':                      'terminal.ansiWhite',
    'BoldWhite':                  'terminal.ansiBrightWhite'
}

# https://stackoverflow.com/a/50757144
colorMap_putty = {
    'Colour0':                    'terminal.foreground',       # foreground
    'Colour1':                    'terminal.foreground',       # bold foreground
    'Colour2':                    'terminal.background',       # background
    'Colour3':                    'terminal.background',       # bold background
    'Colour4':                    'terminalCursor.background', # cursor text
    'Colour5':                    'terminalCursor.foreground', # cursor color
    'Colour6':                    'terminal.ansiBlack',
    'Colour7':                    'terminal.ansiBrightBlack',
    'Colour8':                    'terminal.ansiRed',
    'Colour9':                    'terminal.ansiBrightRed',
    'Colour10':                   'terminal.ansiGreen',
    'Colour11':                   'terminal.ansiBrightGreen',
    'Colour12':                   'terminal.ansiYellow',
    'Colour13':                   'terminal.ansiBrightYellow',
    'Colour14':                   'terminal.ansiBlue',
    'Colour15':                   'terminal.ansiBrightBlue',
    'Colour16':                   'terminal.ansiMagenta',
    'Colour17':                   'terminal.ansiBrightMagenta',
    'Colour18':                   'terminal.ansiCyan',
    'Colour19':                   'terminal.ansiBrightCyan',
    'Colour20':                   'terminal.ansiWhite',
    'Colour21':                   'terminal.ansiBrightWhite'
}

colorMap_gnome = {
    'background-color':           'terminal.background',
    'foreground-color':           'terminal.foreground',
    'highlight-background-color': 'terminal.selectionBackground',
    'cursor-foreground-color':    'terminalCursor.foreground',
    0:                            'terminal.ansiBlack',
    1:                            'terminal.ansiRed',
    2:                            'terminal.ansiGreen',
    3:                            'terminal.ansiYellow',
    4:                            'terminal.ansiBlue',
    5:                            'terminal.ansiMagenta',
    6:                            'terminal.ansiCyan',
    7:                            'terminal.ansiWhite',
    8:                            'terminal.ansiBrightBlack',
    9:                            'terminal.ansiBrightRed',
    10:                           'terminal.ansiBrightGreen',
    11:                           'terminal.ansiBrightYellow',
    12:                           'terminal.ansiBrightBlue',
    13:                           'terminal.ansiBrightMagenta',
    14:                           'terminal.ansiBrightCyan',
    15:                           'terminal.ansiBrightWhite'
}

mode = sys.argv[1]
colorMap = globals()[f'colorMap_{mode}']

with open(sys.argv[2]) as f:
    vsCodeTheme = json.load(f)

themeName = vsCodeTheme['name']
fileName = '{}_{}.{}'.format(mode, themeName.lower().replace(' ', '_'), modes[mode]['ext'])

for srcColor, vsColor in colorMap.items():
    try:
        colorMap[srcColor] = vsCodeTheme['colors'][vsColor]
    except KeyError:
        print('[error] invalid color map')
        exit(1)

    # most consoles don't allow alpha values, so they must be converted
    if len(colorMap[srcColor]) == 9:
        colorMap[srcColor] = rgba2rgb(vsCodeTheme['colors']['terminal.background'], colorMap[srcColor])

with open(fileName, 'w') as f:
    if mode == 'term':
        theme = {'name': themeName}
        theme.update(colorMap)
        json.dump(theme, f, indent=4)

    elif mode == 'cmd':
        from configparser import ConfigParser
        theme = ConfigParser()
        theme.optionxform = str

        theme.add_section('table')
        for colorName, colorHex in colorMap.items():
            theme.set('table', colorName, rgbList(colorHex))

        theme.add_section('info')
        theme.set('info', 'name', themeName)
        theme.set('info', 'author', vsCodeTheme['author'])

        theme.write(f)

    elif mode == 'cyg':
        for colorName, colorHex in colorMap.items():
            f.write('{}={}\n'.format(colorName, rgbList(colorHex)))

    elif mode == 'putty':
        # registry file header
        f.write('''Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\Default%20Settings]
''')

        for colorName, colorHex in colorMap.items():
            f.write('"{}"="{}"\n'.format(colorName, rgbList(colorHex)))

    elif mode == 'gnome':
        palette = str(list(colorMap.values())[4:])
        f.write(f'''#!/bin/bash

PROFILE=$(gsettings get org.gnome.Terminal.ProfilesList default)
PROFILE=${{PROFILE:1:-1}}
SCHEMA="org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$PROFILE/"

declare -A VALS
VALS[use-theme-colors]=false
VALS[highlight-colors-set]=true
VALS[background-color]="{colorMap['background-color']}"
VALS[foreground-color]="{colorMap['foreground-color']}"
VALS[highlight-background-color]="{colorMap['highlight-background-color']}"
VALS[cursor-foreground-color]="{colorMap['cursor-foreground-color']}"
VALS[palette]="{palette}"

for KEY in "${{!VALS[@]}}"; do
  gsettings set $SCHEMA "$KEY" "${{VALS[$KEY]}}"
done
''')


print(f'[done] saved to {fileName}')
