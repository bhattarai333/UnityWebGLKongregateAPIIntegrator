# Unity WebGL Kongregate API Integrator
### Formats Unity WebGL builds with the HTML shell provided by Kongregate to interface with the Kongregate API

This is a tool to easily format the Kongregate HTML shell with the WebGL build of a Unity game in order to
quickly upload the game to Kongregate.

Thanks to AwesometacularVG for detailing how to use the HTML Shell [here](https://www.kongregate.com/forums/1021798-game-programming-subforum/topics/614955-guide-uploading-unity-webgl-games-with-kongs-api).

The program can be used by placing the main.py in the same directory as a folder named "Build" where Unity
will be placing the index.html, template folder and Build folders.

The following is an example of the file structure: 

![Example file structure](https://raw.githubusercontent.com/bhattarai333/UnityWebGLKongregateAPIIntegrator/master/filestructure.png)

You can place the info.json in the same folder as the main.py, but it is not required.

IMPORTANT: You must choose a folder named "Build" from Unity when building your project. You cannot build it to a different folder and then paste the files into the "Build" folder.

Once the build files are in the "Build" directory, the main.py can be run. It will edit your index.html according 
to AwesometacularVGs guide. It will then move the index.html file and Template folder into Unity's Build folder
and zip the Build folder into a zip file named "Additional_Files.zip". Finally, the updated Kongregate HTML shell
file is downloaded from this repository and placed along with the zip file.

The width and height in pixels are set at a default of 1000x650, and will still need to be edited according to your
game's dimensions.

To use the API, you have to create a GameObject in the first scene of your project and name it "KongregateAPI". 
Next you have to attach the KongregateAPI script which is found [here](https://docs.kongregate.com/docs/unity-api) to that gameobject.

If you want to use the Kongregate API, you will have to use the Kongregate preloader which can be found [here](https://github.com/kongregate/webgl-preloader).
You take the "Kongregate Preloader" folder, and put it into a folder called "WebGLTemplates" within your project's "Assets" folder. 
You then open the "Project Settings", scroll to "Player", choose HTML 5 and select the Kongregate preloader. Build normally
from there.

All calls to the Kongregate API will need to be changed from:
Application.ExternalCall("kongregate.stats.submit", "ExampleStatisticName", ExampleStatistic);
to
Application.ExternalCall("parent.kongregate.stats.submit", "ExampleStatisticName", ExampleStatistic);
