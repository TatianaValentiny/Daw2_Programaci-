import datetime
import sys

class Nota:
    def __init__(self,memo,tags):
        self.memo = memo
        self.date = datetime.date.today()
        self.tags = tags
        
    def match(self, filter):
            return filter in self.memo or filter in self

class Llibreta:
    def _init_(self,notes = []):
        self.notes = notes

    def search(self, filter):
         return [note for note in self.notes if Nota.match(filter)]
           
    def new_note(self, memo, tags=""): 
        self.notes.append(Nota(memo, tags)) 
        
class Menu:
    def __init__(self):
        self.llibreta = Llibreta()
        self.botons = {
                "1": self.mostrar,
                "2": self.buscar,
                "3": self.crearN,
                "4": self.surt
                }
        
    def mostrarMenu(self):
        print("""
                Bloc de notes by Tatiana
                1.- Mostrar Notes
                2.- Buscar
                3.- Crear Nota
                4.- Sortir
                """
            )
        
    def activar(self):
        while True:
            self.mostrarMenu()
            choice = input("Tria una opció ")
            action = self.botons.get(choice)
            if action:
                action()
            else:
                print("{0} Valor incorrecte".format(choice))
        
    def mostrar(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))
        
    def buscar(self):
        filter = input("Buscar notes per:")
        notes = self.notebook.search(filter)
        self.mostrar(notes) 
        
    def crearN(self):
        memo = input("Escriu la teva nota: ")
        self.notebook.new_note(memo)
        print("Nota creada amb exit.")
            
    def surt(self):
        print("Tancant sessio...")
        sys.exit(0)
        
Menu().activar()