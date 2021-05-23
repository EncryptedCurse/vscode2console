# vscode2console

Small Python utility that generates console color schemes from VSCode themes.


## Usage
```
python vscode2console.py <term | cmd | cyg | putty | gnome> <theme.json>
```
Console | Keyword
-|-
Windows Terminal | `term`
Command Prompt | `cmd`
Cygwin (mintty) | `cyg`
PuTTY | `putty`
GNOME Terminal | `gnome`

`<theme.json>` refers to an extension's theme definition JSON. As such, it can be found in `%USERPROFILE%\.vscode\extensions` on Windows or in `~/.vscode/extensions` on Linux/macOS.


## Theme installation

### Windows Terminal
 Manually append the contents of `term_<theme>.json` to the `schemes` array in `%LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json`.

### Command Prompt
1. Download Microsoft's [ColorTool](https://github.com/microsoft/terminal/tree/main/src/tools/ColorTool).
2. Place `cmd_<theme>.ini` in its `schemes` directory.
3. Execute `colortool.exe -b cmd_<theme>`.

### Cygwin
Append the contents of `cyg_<theme>.minttyrc` to `~/.minttyrc` either manually or by executing `cat cyg_<theme>.minttyrc >> ~/.minttyrc`.

### PuTTY
Execute `putty_<theme>.reg` and merge it with the Windows Registry.

### GNOME
Execute `gnome_<theme>.sh` in a Bash environment.
