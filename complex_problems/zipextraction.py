import zipfile
import os


def extractzipfile(zipfilepath,extractfilepath):
    with zipfile.ZipFile(zipfilepath, 'r') as zipref:
        zipref.extractall(extractfilepath)

def cleanExtractedZip(extarctfilepath):
    for root, dirs , files in os.walk(extarctfilepath,topdown=False):
        for directory in dirs:
            dire=os.path.join(root,directory)
            if not os.listdir(dire):
                os.rmdir(dire)
        for file in files:
            filepath=os.path.join(root,file)
            if os.path.isdir(filepath):
                os.remove(filepath)
zippath='C:/Users/HP/Desktop/complex_problems/zipextraction/zipfile.zip'
extractpath='C:/Users/HP/Desktop/complex_problems/zipextraction/extracted'
extractzipfile(zippath,extractpath)
cleanExtractedZip(extractpath)