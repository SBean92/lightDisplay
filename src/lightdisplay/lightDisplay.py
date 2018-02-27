class lightDisplay:

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