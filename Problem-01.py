import re

class map():
    def __init__(self):
        self.listOfHeadings = ["S", "W", "N", "E"]
        self.x = 0
        self.y = 0
        self.headingPosition = 2
    def changeHeading(self, newHeading):
        if newHeading == 'R':
            self.headingPosition = (self.headingPosition + 1) % 4
        else:
            self.headingPosition = (self.headingPosition - 1) % 4
    def doSteps(self, numOfSteps):
        if self.listOfHeadings[self.headingPosition] == 'N' :
            self.y += numOfSteps
        elif self.listOfHeadings[self.headingPosition] == 'E' :
            self.x += numOfSteps
        elif self.listOfHeadings[self.headingPosition] == 'S' :
            self.y -= numOfSteps
        else:
            self.x -= numOfSteps
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distance(self):
        return abs(self.x) + abs(self.y)

def findDir():
    f = open("input-01.txt", 'r')
    p = re.compile('[R|L]\d*')
    listOfDir = p.findall(f.read())
    print(listOfDir)
    return listOfDir

def findAns():

    m = map()

    dirs = findDir()

    for d in dirs:
        m.changeHeading(str(d[0]))
        m.doSteps(int(d[1::]))
    return m.distance()

print(findAns())