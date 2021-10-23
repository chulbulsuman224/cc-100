class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("started") 
    def stop(self):
        print("stop")

audi=Car("a6","red","audi",80)
print(audi.start())
print(audi.stop())

