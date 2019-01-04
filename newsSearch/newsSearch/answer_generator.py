class AnsGenerator:
    def __init__(self, input):
        self.input = input

    def getAnsList(self):
        return "normal", None

class NormalGenerator(AnsGenerator):
    def __init__(input):
        AnsGenerator.__init__(input)
