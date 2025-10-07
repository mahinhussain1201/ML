class Car:
    def __init__(self,window,door,engine):
        self.windows=window
        self.doors=door
        self.engine_type=engine
        
    def drive(self):
        print("The person drive the car")
        
class Audi(Car):
    def __init__(self,window,door,engine,enable_ai) :
        super().__init__(window,door,engine)
        self.enable_ai=enable_ai  
        
    def self_drive(self):
        print("Audi has self drive") 
        
    # __str__() defines how the object should look when printed.
    def __str__(self):
        return f"Audi: {self.windows} windows, {self.doors} doors, {self.engine_type} engine, AI: {self.enable_ai}"

        
car=Car(4,5,'Petrol')
Q7 = Audi(4, 5, "Diesel", False)
print(Q7)

    