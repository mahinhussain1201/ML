# empty class
class Bike:
    pass

class Car:
    # constructor
    # self takes the reference of the obj
    def __init__(self,window,door,engine):
        '''
        # public variables
        self.windows=window
        self.doors=door
        self.engine_type=engine
        '''
        '''
        # protected variables
        # in protected overriding can only be from subclass
        self._windows=window
        self._doors=door
        self._engine_type=engine
        '''
        #private variables, cannot be accessed
        self.__windows=window
        self.__doors=door
        self.__engine_type=engine
    
    def self_driving(self):
        return 'This is a {}' .format(self.engine_type)
    
class Truck(Car):
    def __init__(self,window,door,engine,hp):
        super().__init__(window,door,engine)
        self.hp=hp
    
car1=Car(4,5,'Petrol')
car2=Truck(2,2,"EV",500)
dir(car1)
print(car1._Car__windows) # private
# car1.windows public
# car1._windows protected