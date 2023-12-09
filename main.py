from utils import getLinksFromDocx, download

# locatia folderului in care se vor descarca melodiile
DIR = "C:\\Users\\ionut\\Tools\\cncMusicTools\\music"
# Locatia documentului cu linkurile
DOC = "C:\\Users\\ionut\\Documents\\cr.docx"

links, docLinks = getLinksFromDocx(DOC)
downloadCount = 1

for link in links:
    download(link=link, path=DIR)
    downloadCount += 1

print(f"Done downloading: {downloadCount}")
