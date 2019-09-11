import os
from pathlib import Path
import zipfile

# Thanks to AwesometacularVG for detailing how to use the HTML Shell here:
# https://www.kongregate.com/forums/1021798-game-programming-subforum/topics/614955-guide-uploading-unity-webgl-games-with-kongs-api?page=1


# https://stackoverflow.com/questions/14568647/create-zip-in-python
def zipfolder(src, dst):
    zf = zipfile.ZipFile("%s.zip" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print('zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname))
            zf.write(absname, arcname)
    zf.close()


data_folder = Path("Build/")
file_to_open = data_folder / "index.html"
indexHTML = file_to_open.read_text()

indexHTML = indexHTML.replace("Build/UnityLoader.js", "UnityLoader.js")
indexHTML = indexHTML.replace("Build/Build.json", "Build.json")
indexHTML = indexHTML.replace("Build/Template/anthill.png", "Template/anthill.png")

file_to_open.write_text(indexHTML)

source = file_to_open
destination = Path("Build/Build/index.html")

source.replace(destination)

folder_to_open = Path("Build/") / "Template/"
source = folder_to_open
destination = Path("Build/Build/Template/")
source.replace(destination)

zip_source = Path("Build/Build/")
zip_destination = Path("Build/Additional_Files")
zipfolder(zip_source, zip_destination)
