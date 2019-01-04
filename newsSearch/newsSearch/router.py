import json

class Router:
    self.inputTypesFilePath = "./data/inputTypes.json"
    self.inputPatternsFilePath = "./data/inputPatterns.json"
    self.inputTypes = {}
    self.inputPatternsFile = {}
    def __init__():
        self.inputTypes = json.load(self.inputTypesFilePath)
        self.inputPatterns = json.load(self.inputPatternsFilePath)

    def getAnswerDir(input):
        if input in inputPatterns:
            return inputTypes[inputPatterns[input]]
        else:
            return None
