#8/9 -- No entra en parcial

#OBJETOS : instancia particular de una CLASE
    #tipo
    #representacion interna
    #procedimientos

#CLASE : --> plano ('cascara')
    #nombre
    #atributos (data attributes) -> estados
    #metodos (procedural attributes)

class nombre: #definicion de clase
    def __init__(self, atributo1, atributo2): #definicion de atributos
        self.atributo1 = atributo1         #__init__ constructor
        self.atributo2 = atributo2 #self para especificar que se trabaja sobre si mismo
    def metodo1(self): #definicion de metodos
        return 2*self.atributo1
    def metodo2(self):
        return 2*self.atributo2

'''ejemplo'''
class Circulo:
    def __init__(self, radio): #definicion de atributos
        self.radio = radio #__init__ constructor
    def area(self): #definicion de metodos
        return 3.14*self.radio **2 #self para especificar que se trabaja sobre si mismo!!
    def preimeter(self):
        return 2*3.14*self.radio
    
#acceder a atributos objeto.atributo
#acceder a metodo objeto.metodo()