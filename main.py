import os
import zipfile
from pathlib import Path
import urllib.request
import json


# Instructions for use in README file or: https://github.com/bhattarai333/UnityWebGLKongregateAPIIntegrator

# Thanks to AwesometacularVG for detailing how to use the HTML Shell here:
# https://www.kongregate.com/forums/1021798-game-programming-subforum/topics/614955-guide-uploading-unity-webgl-games-with-kongs-api


# https://stackoverflow.com/questions/14568647/create-zip-in-python
def zipfolder(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            print("Filename: %s DST: %s" % (filename, dst))
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print('zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname))
            if (filename == arcname):
                print("skipping %s" % filename)
                continue
            zf.write(absname, arcname)
    zf.close()


data_folder = Path(".")
data_file = data_folder / "info.json"
width = 1000
height = 600
username = "bhattarai333"
if data_file.exists():
    json_data = json.loads(data_file.read_text())
    width = json_data["width"]
    height = json_data["height"]
    username = json_data["username"]
    print("Width: %s Height: %s Username: %s" %(width, height, username))


build_folder = Path("Build/")
file_to_open = build_folder / "index.html"
indexHTML = file_to_open.read_text()

indexHTML = indexHTML.replace("Build/UnityLoader.js", "UnityLoader.js")
indexHTML = indexHTML.replace("Build/Build.json", "Build.json")
indexHTML = indexHTML.replace("Build/Template/anthill.png", "Template/anthill.png")
indexHTML = indexHTML.replace("href=\"http://www.kongregate.com\"",
                              "href=\"http://www.kongregate.com?referrer=%s\"" % username)

file_to_open.write_text(indexHTML)

source = file_to_open
destination = Path("Build/Build/index.html")

source.replace(destination)

folder_to_open = Path("Build/") / "Template/"
source = folder_to_open
destination = Path("Build/Build/Template/")
source.replace(destination)

zip_source = Path("Build/")
zip_destination = Path("Build/Additional_Files")
zipfolder(zip_source, zip_destination)

# https://raw.githubusercontent.com/bhattarai333/UnityWebGLKongregateAPIIntegrator/master/kongregate_shell_updated.html

shell_destination = Path("Build/kongregate_shell_updated.html")
with urllib.request.urlopen(
        "https://raw.githubusercontent.com/bhattarai333/UnityWebGLKongregateAPIIntegrator/master/kongregate_shell_updated.html") as url:
    shellHTML = url.read().decode()
    shellHTML = shellHTML.replace("width:800px;", "width:%spx;" % width)
    shellHTML = shellHTML.replace("height:400px;", "height:%spx;" % height)
    shell_destination.write_text(shellHTML)


