class Man():
    def __init__(self,name,wife):
        self.name=name
        self.wife=wife
    def setWifename(self,newname):
        self.wife=newname
    def getName(self):
        print(f"the name of my wife is {self.wife}")
mans=Man('obura','stella')
mans.getName()
mans.setWifename('obura')
mans.getName()

class Bettle():
    def __init__(self,power,run):
        self.power=power
        self.run=run
        
    def setPower(self,extras):
        self.power=extras
    def getPower(self):
         print(f"my new power is {self.power}")
bee=Bettle('telekinetic','miles')
bee.getPower()
bee.setPower('diving')
bee.getPower()

class Mango():
    def __init__(self,name,colour):
        self._name=name
        self.__colour=colour
    def getcolour(self):
        print(f"the colour of my mango is {self.__colour}")
woma=Mango('jemba','yellow')
woma.getcolour()
        