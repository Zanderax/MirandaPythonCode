import os

oldDir = "old"
newDir = "new"
deliminator = "_"
extension = ".txt"

for personName in os.listdir(oldDir):
    for fileName in os.listdir( os.path.join( oldDir, personName ) ):
        # Removing .txt Extension
        folderName = os.path.splitext(fileName)[0]
        
        # Remove Person Prefix
        folderName = folderName.split(deliminator)[1]
        
        oldPath = os.path.join( oldDir, personName, fileName)
        newPath = os.path.join( newDir, folderName, fileName)
        os.rename( oldPath, newPath )
