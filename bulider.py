from abc import ABCMeta,abstractclassmethod

class Ibulider (ABCMeta):
    @staticmethod
    @abstractmethod 
    def get_result(Ibulder):
        "get the result"
    @staticmethod
    @abstractmethod 
    def creat_car():
        "this is car"
    @staticmethod
    @abstractmethod 
    def cerat_taxi():
        "this is taxi"
    @staticmethod
    @abstractmethod 
    def creat_bus():
        "this is bus"
    @staticmethod
    @abstractmethod 
    def get_result():
        "the concrete bulider"
class bulider (Ibulider):
   def __init__(self):
      self.product=product()

   def bulid_creat_car(self):
       self.product.creat.append("ferarri")
       return self
   def bulid_creat_taxi(self):
       self.product.creat.append("taxi")
       return self
   def bulid_creat_bus(self):
       self.product.creat.append("bus")
       return self
   