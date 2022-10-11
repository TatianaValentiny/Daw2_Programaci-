def mostrar_menu(opcions):
    print('Tria una de les següents opcions:')
    for clau in sorted(opcions):
        print(f' {clau}) {opcions[clau][0]}')


#Falten objectes

def llegir_opcio(opcions):
    while (a := input('Opció: ')) not in opcions:
        print('Valor erroni, torna a intentar-ho')
    return a


def executar_opcio(opcio, opcions):
    opcions[opcio][1]()


def generar_menu(opcions, opcio_sortir):
    opcio = None
    while opcio != opcio_sortir:
        mostrar_menu(opcions)
        opcio = llegir_opcio(opcions)
        executar_opcio(opcio, opcions)
        print()


def menu_principal():
    opcions = {
        '1': ('Mostra Notes', MostrarNotes),
        '2': ('Buscar ', Buscar),
        '3': ('Afegir', Afegir),
        '4': ('Sortir', Sortir)
    }
    generar_menu(opcions, '4')

def MostrarNotes():
    print('Has triat la opció 1')

def Buscar():
    print('Has triat la opció 2')

def Afegir():
    print('Has triat la opció 3')

def Sortir():
    print('Sortint')

if __name__ == '__main__':
    menu_principal()
    
    