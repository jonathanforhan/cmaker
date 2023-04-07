## Use
**cmkr** is the command used for all cmaker functionality
- **new** ***{Project Name}*** - creates a new build evniornment with basic CMake requirements
    - **from** - adding **from** as in ```cmkr {Project Name} from {CustomTemplate}``` allows for templating for each project structure
- **build** - CMake build scripts, flag either *--debug* or *--release*, default is *--debug*
- **add**
    - **cxx** ***{File Name}*** - generates source and header files for C++ class
    - **c** ***{File Name}*** - generates source and header files for C files

## Scripting
- CMaker offers project specific, customizable scripting through declarations in the cmaker-config.json file.\

## Templating
- When ```cmkr new``` is called it looks in the ```$HOME/.scripts/cmaker/templates/``` directory and recursively copies everything the default folder, adding another folder in the templates folder will allow to call ```cmkr new {Project} from {Template}``` You can edit or add any file to the ```$HOME/.scripts/cmaker/templates/``` directory to customize your build process.
- The files under ```.cmaker/``` are the templates that are *not* to be copied on initialization, these include the class templates, and supported ```.cmake``` files and their corresponding ```.docs``` files.
- ```.docs``` files explain how to implement the package into your project, cite the source of the ```.cmake``` file, and any other relevant information.
- You can edit the templates as you please and their changes will be applied. The only caveat is that if you add new templates under the ```.cmaker/``` directory you need to add your own script to copy them in the ```scripts.cmaker``` file.

## File Output
- Running ```cmkr build``` with either the ```--debug``` or ```--release``` flags will create debug or release directories in your specified output path in your cmaker-config
