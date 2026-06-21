import json

def jsonData(filePath):
    with open(filePath) as data:
        formatedData = json.load(data)
        return formatedData

