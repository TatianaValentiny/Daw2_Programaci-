import datetime
import sys

class Note:
    def __init__(self,memo,tags):
        self.memo = memo
        self.date = datetime.date.today()
        self.tags = tags
        
    def match(self, filter):
            return filter in self.memo or filter in self

class Notebook:
    def _init_(self,notes = []):
        self.notes = notes

    def search(self, filter):
         return [note for note in self.notes if Note.match(filter)]
           
    def new_note(self, memo, tags=""): 
        self.notes.append(Note(memo, tags)) 
        
class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.botons = {
                "1": self.mostrar,
                "2": self.buscar,
                "3": self.crearN,
                "4": self.surt
                }
        
    def mostrarMenu(self):
        print("""
                La meva Notebook
                1.- Mostrar Notes
                2.- Buscar
                3.- Crear Nota
                4.- Sortir
                """
            )
        
    def activar(self):
        while True:
            self.mostrarMenu()
            choice = input("Que vols fer? ")
            action = self.botons.get(choice)
            if action:
                action()
            else:
                print("{0} Valor incorrecte".format(choice))
        
    def mostrar(self, notes=None):
        with open ("Nota.txt") as file_object:
            llegir = file_object.read()
            print(llegir)
        
    def buscar(self):
        filter = input("Buscar notes per:")
        notes = self.notebook.search(filter)
        self.mostrar(notes) 
        
    def crearN(self):
        arxiu = open("Nota.txt", "w")
        nom = input("Posa el nom de la nota: ")
        arxiu.write(nom + '\n')
        arxiu.close()

    def surt(self):
        print("Tancant sessi0...")
        sys.exit(0)
        
Menu().activar()