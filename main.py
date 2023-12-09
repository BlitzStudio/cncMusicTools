from utils import getLinksFromDocx, download

# locatia folderului in care se vor descarca melodiile
DIR = "C:\\Users\\ionut\\Tools\\cncMusicTools\\music"
# Locatia documentului cu linkurile
DOC = "C:\\Users\\ionut\\Documents\\cr.docx"

links, docLinks = getLinksFromDocx("C:\\Users\\ionut\\Documents\\cr.docx")
downloadCount = 1

print("Done downloading:")
for link in links:
    download(link=link, path=DIR, downloadCount=downloadCount)
    downloadCount += 1
