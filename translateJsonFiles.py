import os
import sys
import json
from googletrans import Translator

translator = Translator()
sourceFilePath = ''
sourceLanguage = 'en'
destinationLanguage = ''

try:
    os.mkdir('TranslatedJsonFiles')
except:
    pass

if(len(sys.argv) > 1):
    destinationLanguage = str(sys.argv[1])
else:
    print('taking default value for destination language arguments en')
    destinationLanguage = 'en'
if(len(sys.argv) > 2):
    sourceFilePath = str(sys.argv[2])
else:
    print('taking default value for source file path SourceFiles/SourceFileJson.json')
    sourceFilePath = 'SourceFiles/SourceFileJson.json'
if(len(sys.argv) > 3):
    sourceLanguage = str(sys.argv[3])
else:
    print('taking default value for source language en')
    sourceLanguage: 'en'


def loadValuesFromFile(filePath):
    try:
        file = open(filePath, "r", encoding='utf8')
        jsonFileValuesList = list((json.load(file)).values())
        return jsonFileValuesList
    except Exception as e:
        print('An exception occurred while reading json file', e)


def loadKeysFromFile(filePath):
    try:
        file = open(filePath, "r", encoding='utf8')
        jsonFileKeysList = list((json.load(file)).keys())
        return jsonFileKeysList
    except Exception as e:
        print('An exception occurred while reading json file', e)


def translateJsonFile(listOfSentence, sourceLang, destinationLang):
    try:
        translatedList = translator.translate(
            listOfSentence, dest=destinationLang, src=sourceLang)  # change listOfSentence[start:end] to slice
        return translatedList
    except Exception as e:
        print("An exception occurred while translating json file", e)


def createObject(listOfKeys, listOfValues):
    try:
        result = {listOfKeys[i]: listOfValues[i].text for i in range(
            len(listOfKeys))}
        return result
    except Exception as e:
        print("An exception occurred while creating object", e)


def saveToFile(fileName, contents):
    try:
        with open(fileName, 'w', encoding='utf8') as convert_file:
            convert_file.write((json.dumps(contents, ensure_ascii=False)))
            print(f"successfully created {fileName}")

    except Exception as e:
        print("An exception occurred while saving file", e)


def main():
    try:
        contentToWrite = createObject(loadKeysFromFile(sourceFilePath), translateJsonFile(  # change sourceFilePath[start:end] to slice
            loadValuesFromFile(sourceFilePath), sourceLang=sourceLanguage, destinationLang=destinationLanguage))
        saveToFile(
            f'TranslatedJsonFiles/{sourceLanguage.capitalize()}To{destinationLanguage.capitalize()}.json', contentToWrite)
    except Exception as e:
        print('An exception occurred', e)


if __name__ == "__main__":
    main()
