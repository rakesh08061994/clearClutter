import os
import shutil

audioExt = [".m4a",".flac",".mp3",".wav",".wma",".aac"]
videoExt = [".mp4",".mov",".wmv",".avi",".avchd",".flv",".f4v",".swf",".mkv",".webm"]
documentExt = [".doc",".docx",".txt",".pdf",".ppt",".pptx",".htm",".html",".rar",".zip","winrar"]
imageExt = [".psd",".xcf",".ai",".cdr",".svg",".tiff",".tif",".bmp",".jpg",".jpeg",".gif",".png"]

def createIfNotExixts(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

createIfNotExixts("Audios")
createIfNotExixts("Videos")
createIfNotExixts("Documents")
createIfNotExixts("Images")
createIfNotExixts("Others")

def clearClutter(source):
    sourceDir = os.listdir(source)


    dest = os.getcwd()

    for i in sourceDir:
        ext = os.path.splitext(i)
        if ext[1].lower() in audioExt:
            shutil.move(f"{source}/{i}",f"{dest}/Audios/{i}")

        if ext[1].lower() in videoExt:
            shutil.move(f"{source}/{i}",f"{dest}/Videos/{i}")

        if ext[1].lower() in documentExt:
            shutil.move(f"{source}/{i}",f"{dest}/Documents/{i}")

        
        if ext[1].lower() in imageExt:
            shutil.move(f"{source}/{i}",f"{dest}/Images/{i}")

        if (ext[1].lower() not in audioExt) and (ext[1].lower() not in videoExt) and (ext[1].lower() not in documentExt) and (ext[1].lower() not in imageExt) and os.path.isfile(i):
            shutil.move(f"{source}/{i}",f"{dest}/Others/{i}")

if __name__ == "__main__":

    source = os.getcwd()
    clearClutter(source)
