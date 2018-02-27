class lightDisplay:

    lights = None

    def __init__(self, L):
        self.lights = [[False for x in range(L)] for x in range(L)]
        self.dimension = L
    
    def action(self, cmd, a, b, x, y):
        if cmd == "turn on":
            for i in range(a,x):
                for j in range(b,y):
                    self.lights[i][j] = True
        elif cmd == "turn off":
            for i in range(a,x):
                for j in range(b,y):
                    self.lights[i][j] = False
        elif cmd == "switch":
            for i in range(a,x):
                for j in range(b,y):
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
        print("There are",self.tCount,"lights on and",self.fCount,"lights off")
        #TO-DO: Add statements for when there are no lights on or all lighst on so on....
                
        