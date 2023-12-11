from utils import getLinksFromDocx, download

# locatia folderului in care se vor descarca melodiile
DIR = ""
# Locatia documentului cu linkurile
DOC = ""

# se iau linkurile si nr de linkuri din document
links, docLinks = getLinksFromDocx(DOC)

downloadCount = 1

#
for link in links:
    download(link=link, path=DIR)
    downloadCount += 1

print(f"Done downloading: {downloadCount}")
