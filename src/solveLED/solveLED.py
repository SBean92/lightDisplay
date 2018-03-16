import urllib.request
import re
import sys

class lightDisplay:
    lights = None
    def __init__(self, L):
        self.lights = [[False for x in range(L)] for y in range(L)]
        self.dimension = L
    
    def action(self, cmd, x_1, y_1, x_n, y_n):
        if cmd == "turn on":
            for i in range(x_1,x_n+1):
                for j in range(y_1,y_n+1):
                    self.lights[i][j] = True
        elif cmd == "turn off":
            for i in range(x_1,x_n+1):
                for j in range(y_1,y_n+1):
                    self.lights[i][j] = False
        elif cmd == "switch":
            for i in range(x_1,x_n+1):
                for j in range(y_1,y_n+1):
                    if self.lights[i][j] == True:
                        self.lights[i][j] = False
                    elif self.lights[i][j] == False:
                        self.lights[i][j] = True

    def count(self):
        self.tCount = 0
        self.fCount = 0
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.lights[i][j] == True:
                    self.tCount += 1
                elif self.lights[i][j] == False:
                    self.fCount += 1
        if self.tCount == 0:
            print("There are no lights on")
        elif self.fCount == 0:
            print("There are no lights off")
        elif self.tCount == 1:
            print("There is one light on and",self.fCount,"lights off")
        elif self.fCount == 1:
            print("There are",self.tCount,"lights on and one light off")
        else:
            print("There are",self.tCount,"lights on and",self.fCount,"lights off")

def main():
    x = sys.argv[1:]
    data = urllib.request.urlopen(x[0])
    lineSem = 0
    for line in data:
        if lineSem == 0:
            lineSem += 1
            gridLED = lightDisplay(int(line.decode('utf-8')))
        else:
            p = re.match(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*", line.decode('utf-8'))
            if p != None:
                cmd = p.group(1)
                x_0 = p.group(2)
                y_0 = p.group(3)
                x_n = p.group(4)
                y_n = p.group(5)
                if int(x_0) < 0 or int(y_0) < 0 or int(x_0) > int(x_n) or int(y_0) > int(y_n) or int(x_n) > gridLED.dimension or int(y_n) > gridLED.dimension:
                    print("Dimensions out of range, skipping line")
                else:
                    gridLED.action(cmd,int(x_0),int(y_0),int(x_n),int(y_n))
            else:
                print("Invalid Command, skipping line")
    gridLED.count()


if __name__ == '__main__':
    main()