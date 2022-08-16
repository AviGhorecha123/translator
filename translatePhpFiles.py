import re
import os
import sys
from googletrans import Translator

translator = Translator()
sourceFilePath = ''
sourceLanguage = 'en'
destinationLanguage = ''

try:
    os.mkdir('TranslatedPhpFiles')
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
    print('taking default value for source file path SourceFiles/SourceFilePhp.php.txt')
    sourceFilePath = 'SourceFilePhp.php.txt'
if(len(sys.argv) > 3):
    sourceLanguage = str(sys.argv[3])
else:
    print('taking default value for source language en')
    sourceLanguage: 'en'


def saveToFile(fileName, contents):
    try:
        with open(fileName, 'w', encoding='utf8') as convert_file:
            convert_file.write(contents)
            print(f"successfully created {fileName}")

    except Exception as e:
        print("An exception occurred while saving file", e)


def translateString(stringToTranslate, sourceLang, destinationLang):
    try:
        translatedString = translator.translate(
            stringToTranslate,  src=sourceLang, dest=destinationLang).text
        return translatedString
    except Exception as e:
        print("An exception occurred while translation", e)


# def getValuesAndKeys(fileName):
#     try:
#         file = open(fileName, "r", encoding='utf8').read()
#         findLeft = re.compile(r"\['(.*)'\]")
#         findRight = re.compile(r"\= \'(.*)\'")
#         keys = findLeft.findall(file)
#         values = findRight.findall(file)
#         return keys, values
#     except Exception as e:
#         print("An exception occurred while getting values and keys", e)

def translate(matchObj):
    try:
        translatedString = translateString(
            matchObj.group(0), sourceLang=sourceLanguage, destinationLang=destinationLanguage)
        return translatedString
    except Exception as e:
        print("An exception occurred during translation", e)


def replace():
    try:
        file = open(f'SourceFiles/{sourceFilePath}',
                    "r", encoding='utf8').read()
        fileStr = re.sub(r"\= \'(.*)\'", translate, file)
        return fileStr
    except Exception as e:
        print("An exception occurred during replacing content", e)


def main():
    try:
        translatedFile = replace()
        saveToFile(
            f"TranslatedPhpFiles/{sourceLanguage.capitalize()}To{destinationLanguage.capitalize()}.php.txt", translatedFile)

        # fileStr = ''
        # keys, values = getValuesAndKeys(f'SourceFiles/{sourceFilePath}')
        # fileStr += '<?php\n'
        # for i in range(len(keys)):
        #     fileStr += f"$lang['{keys[i]}'] = '{translateString(values[i],sourceLang=sourceLanguage,destinationLang=destinationLanguage)}';\n"
        # fileStr += '?>'

    except Exception as e:
        print("An exception occurred", e)


if __name__ == "__main__":
    main()
