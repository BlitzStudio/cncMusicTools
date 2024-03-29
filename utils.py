import json
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT
import yt_dlp


# primeste path ul catre documentul cu melodii si extrage din acesta toate linkurile
# DO NOT TOUCH: nu stiu cum functioneza
def getLinksFromDocx(path):
    docx = Document(path)
    links = []
    rels = docx.part.rels
    for rel in rels:
        if rels[rel].reltype == RT.HYPERLINK:
            links.append(rels[rel]._target)
    print(f"Linkuri in document: {len(links)}")
    links = getValidLinks(links)
    # print(f"Linkuri de youtube in document: {len(links)}")
    return [links, len(links)]


# primeste un array cu linkuri pe care il parcurge si extrage doar linkurile de youtube
# in cazul in care se implementeza download(YtId,path) v-a returna un array[id]
def getValidLinks(array):
    return array
    pass


# nu este folosita
def printStatus(stream, chuck, bytes_remaining):
    print(stream)
    print(chuck)
    print(bytes_remaining)


def printComplete(stream, file):
    print(f"{stream.downloadCount}:{stream.title}")


# descarca in format mp3 linkul in folderul selectat precizat
def download(link, path):
    ydl_opts = {
        "format": "bestaudio/best",
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        "postprocessors": [
            {  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
        "retries": 3,
        "outtmpl": f"{path}/%(title)s.%(ext)s",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ytdl:
        ytdl.download(link)
