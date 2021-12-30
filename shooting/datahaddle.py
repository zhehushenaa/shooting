class people():



    def __init__(self,name,age):
        self.name=name
        self.age=age

    def readdata(self):
        i=0
        while True:
            print (self.name,self.age,i)
            i=i+1

