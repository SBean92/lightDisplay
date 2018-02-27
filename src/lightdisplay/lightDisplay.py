class lightDisplay:

    lights = None

    def __init__(self, L):
        self.lights = [[False for x in range(L)] for x in range(L)]
    
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
        #TO-DO