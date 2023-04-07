# CMaker

CMaker is a CMake qualitity-of-life tool. Strives to be unopinionated and customizable.
### Features:
- Customizable CMake templates with sane defaults
- Simple cmkr commands for building  and running
- Customizable project specific and template specific commands 

### Requirements:
- CMake
- Make
- Python3

### Additional Support:
- Ninja

## Setup
CMaker was developed primarily for Unix, however, using git bash (with some confirguring of CMake and make) or using WSL will give full functionality on Windows
- ### Unix
Path: ```~/.scripts/cmaker/```
- Bash:\
```mkdir ~/.scripts && cd ~/.scripts/ && git clone https://github.com/jonathanforhan/cmaker.git && echo 'export PATH="$HOME/.scripts/cmaker:$PATH"' >> ~/.bashrc```

- ### Windows
Path: ```C:\\Users\\%userprofile%\\.scripts\\cmaker\\```
<br><br>

- Powershell:\
```cd ~; mkdir .\.scripts; cd .\.scripts\; git clone https://github.com/jonathanforhan/cmaker.git```\
add ```C:\\Users\\%userprofile%\\.scripts\\cmaker\\``` to your enviornment variable path
