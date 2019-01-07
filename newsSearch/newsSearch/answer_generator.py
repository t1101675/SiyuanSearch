# -*- coding: UTF-8 -*-
class AnsGenerator:
    def __init__(self, input):
        self.input = input

    def getAnsList(self):
        if self.input == u"付若琳":
            print "OK"
            return "html", "ruolin.html"
        return "normal", None

class NormalGenerator(AnsGenerator):
    def __init__(input):
        AnsGenerator.__init__(input)
