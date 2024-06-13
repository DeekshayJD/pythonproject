import zipfile
import os
currentDirectory=r"D:\Documents\zipfolder"
zipFileName=r"D:\Documents\newzip\temp.zip"
extractDirectory=r"D:\Documents"

#function to extract file from zip file

def extractzip(path_to_zipfile,directory_to_extract_to):
    with zipfile.ZipFile(path_to_zipfile,"r")as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
        print("extracted")

#function to zip files in the directory
def zipdir(dirpath,zippath):
    zipf=zipfile.ZipFile(zippath,mode="w")
    lenDirPath=len(dirpath)
    for root,_,files in os.walk(dirpath):
        #it yield a 3 tuple (dirpath,dirname,filename)
       for file in files:
         filepath=os.path.join(root,file)
         zipf.write(filepath,filepath[lenDirPath:])
       print("file zipped")
       zipf.close()

zipdir(currentDirectory,zipFileName)


#extractzip(zipFileName,extractDirectory)