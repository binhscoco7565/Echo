# Echo
Echo is a basic utility used to launch useful tools for adding/fixing features in Windows, written in Python using [DearPyGui](https://github.com/hoffstadt/DearPyGui).

### Current usage
While the current state of the application is extremely basic at the moment, changes are made often and so you should watch out for any new updates, whether bug fixes or new tools :)

### Releases
Check out the [releases](https://github.com/tuxy/Echo/releases) page

### Build and run

In Powershell, clone the repository and enter directory:
```ps
git clone https://github.com/binhscoco7565/echo; cd echo
```
Install dependencies
```ps
pip install -r requirements.txt
```
...and run the application
```ps
python main.py
```
### Credits
This application relies on many other codebases and hard work. Most notably is the work of the community in the library [DearPyGui](https://github.com/hoffstadt/DearPyGui) based on [DearImGui](https://github.com/ocornut/imgui). Without this, this project would've been dead almost immediately. Functionality is also based off of:
* The work of Chris Titus Tech in [winutil](https://github.com/ChrisTitusTech/winutil)
* (Unimplemented) scripts from the questionably named [privacy.sexy](https://privacy.sexy)  
* Extensive use of the [scoop](https://scoop.sh) package manager, enabling many of the features in this app.
* ...and the community that also supported this project with their own code or donations.