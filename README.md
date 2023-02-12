# CMaker

CMaker is a CMake qualitity-of-life tool. Strives to be unopinionated and customizable.
### Features:
- Customizable CMake templates with sane defaults
- Simple cmkr commands for building  and running
- Customizable project specific and template specific commands 

## Setup
CMaker is designed for a Unix terminal interface. If you use windows I reccomend making git bash your terminal in VScode or using WSL, as an alternative all commands can be overridden to use powershell in ```scripts.cmaker```
- ### Unix
Path: ```~/.scripts/cmaker/```
- Bash:\
```mkdir ~/.scripts && cd ~/.scripts/ && git clone https://github.com/jonathanforhan/cmaker.git && echo 'export PATH="$HOME/.scripts/cmaker:$PATH"' >> ~/.bashrc```

- ### Windows
Path: ```C:\\Users\\%userprofile%\\.scripts\\cmaker\\```
<br><br>

- Powershell:\
```cd && mkdir .scripts && cd .scripts/ && git clone https://github.com/jonathanforhan/cmaker.git```\
add ```C:\\Users\\%userprofile%\\.scripts\\cmaker\\``` to your enviornment variable path

## Use
**cmkr** is the command used for all cmaker functionality
- **new** ***{Project Name}*** - creates a new build evniornment with basic CMake requirements\
- **build** - CMake build scripts, flag either *--debug* or *--release*, default is *--debug*
- **run** - the same as build but it executes the binary
- **add**
    - **class** ***{Class Name}*** - generates .hpp and .cpp class templates, if you are in the root project directory they will be automatically  placed in src directory.
    - **cmakelists** - generate an empty CMakeLists.txt file in cwd.
    - ***{Dependancies}*** - I'm working to offer a wide range of 'out of the box' .cmake files. PRs with more dependancies would be amazing. When ```cmkr add {dependancy}```is called the .cmake file will be added to the cmake/ directory and the applicable ```find_package()``` command will be added to the root CMakeLists.txt under ```#CMAKER_FIND```. The ```CMAKE_MODULE_PATH``` is also automatically added to the root CMakeLists.txt file under ```#CMAKER_SET```
-**clean** - clears the build folder, ```cmkr clean --all``` clears the build folder as well as bin folder

## Scripting
- CMaker offers project specific, customizable scripting through declarations in the scripts.cmaker file.\
```myscript="echo 'add a keyword and command to execute, then call script with cmkr (keyword)'"```\
Scripting is localized to one ```scripts.cmaker``` file and called with ```cmkr {keyword}``` 
- CMaker parses scripts **first** meaning that **all cmkr commands can be overridden**
- Comments are written in the scripts.cmaker file with and prefixed ```#```

## Templating
- When ```cmkr new``` is called it looks in the ```$HOME/.scripts/cmaker/templates/``` directory and recursively copies everything in that folder. You can edit or add any file to the ```$HOME/.scripts/cmaker/templates/``` directory to customize your build process.
- The files under ```.cmakerignore/``` are the templates that are not to be copied on initialization, these include the class templates, and supported ```.cmake``` files and their corresponding ```.docs``` files.
- ```.docs``` files explain how to implement the package into your project, cite the source of the ```.cmake``` file, and any other relevant information.
- You can edit the templates as you please and their changes will be applied. The only caveat is that if you add new templates under the ```.cmakerignore/``` directory you need to add your own script to copy them in the ```scripts.cmaker``` file.

## File Output
- Running ```cmkr build``` and ```cmkr run``` with either the ```--debug``` or ```--release``` flags will create debug or release directories in the ```bin``` folder and save your binaries there. to change the output simply add a ```-DOUTPUT:STRING=${PATH}``` to your cmake command where ${PATH} is your disired output path. Note this is using ```cmake``` command and not the ```cmkr``` command. To use ```cmkr``` just add the cmake command to the ```scripts.cmaker``` file with desired cmkr keyword

## Any Issues With Privileges
Some distros have problems with privileges, if this is you run ```cd ~/.scripts/ && sudo bash && chmod 775 ./cmaker/**```

## Plans for the Future
- Add a ```cmkr new {Project} from {Template}``` feature that allows for different templating for different builds. These templates will be directories in the Template Folder
