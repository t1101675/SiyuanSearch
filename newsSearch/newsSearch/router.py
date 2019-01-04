import json

class Router:
    def __init__(self):
        self.inputPatternsFilePath = "./data/inputPatterns.json"
        self.inputTypesFilePath = "./data/inputTypes.json"
        self.inputTypes = json.load(self.inputTypesFilePath)
        self.inputPatterns = json.load(self.inputPatternsFilePath)

    def getAnswerDir(self, input):
        if input in inputPatterns:
            return inputTypes[inputPatterns[input]]
        else:
            return None
