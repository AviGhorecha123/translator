import os
import sys
import json
from googletrans import Translator

translator = Translator()
sourceFilePath = ''
sourceLanguage = 'en'
destinationLanguage = ''

try:
    os.mkdir('translated')
except:
    pass

try:
    destinationLanguage = str(sys.argv[1])
    sourceFilePath = str(sys.argv[2])
    sourceLanguage = str(sys.argv[3])
except:
    print('enter arguments\ntaking default values')
    sourceFilePath = 'sourceLanguage.json'
    destinationLanguage = 'en'


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
            listOfSentence[0:20], dest=destinationLang, src=sourceLang)
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

    except Exception as e:
        print("An exception occurred while saving file", e)


def main():
    try:
        contentToWrite = createObject(loadKeysFromFile(sourceFilePath)[
            0:20], translateJsonFile(loadValuesFromFile(sourceFilePath), sourceLang=sourceLanguage, destinationLang=destinationLanguage))
        saveToFile(
            f'translated/EnTo{destinationLanguage.capitalize()}.json', contentToWrite)
    except Exception as e:
        print('An exception occurred', e)


if __name__ == "__main__":
    main()
