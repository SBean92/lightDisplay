class lightDisplay:

    lights = None

    def __init__(self, L):
        self.lights = [[False for x in range(L)] for x in range(L)]
    
    def action(self, cmd):
        if cmd == "turn on":
            #TO-DO
        elif cmd == "turn off":
            #TO-DO
        elif cmd == "switch":
            #TO-DO

    def count(self):
        #TO-DO