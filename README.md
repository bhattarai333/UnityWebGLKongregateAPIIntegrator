# Unity WebGL Kongregate API Integrator
###Formats Unity WebGL builds with the HTML shell provided by Kongregate to interface with the Kongregate API

This is a tool to easily format the Kongregate HTML shell with the WebGL build of a Unity game in order to
quickly upload the game to Kongregate.

Thanks to AwesometacularVG for detailing how to use the HTML Shell [here](https://www.kongregate.com/forums/1021798-game-programming-subforum/topics/614955-guide-uploading-unity-webgl-games-with-kongs-api).

The program can be used by placing the main.py in the same directory as a folder named "Build" where Unity
will be placing the index.html, template folder and Build folders.

The following is an example of the file structure:

Any Folder
├── main.py
├── Build
│   ├── index.html
│   ├── Template
│   ├── Build

Once the build files are in the "Build" directory, the main.py can be run. It will edit your index.html according 
to AwesometacularVGs guide. It will then move the index.html file and Template folder into Unity's Build folder
and zip the Build folder into a zip file named "Additional_Files.zip". Finally, the updated Kongregate HTML shell
file is downloaded from this repository and placed along with the zip file.

The width and height in pixels are set at a default of 1000x650, and will still need to be edited according to your
game's dimensions.

All calls to the Kongregate API will need to be changed from:
Application.ExternalCall("kongregate.stats.submit", "ExampleStatisticName", ExampleStatistic);
to
Application.ExternalCall("parent.kongregate.stats.submit", "ExampleStatisticName", ExampleStatistic);
