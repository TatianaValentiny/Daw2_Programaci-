from tkinter import *
from tkinter import messagebox as ms
from tkinter import filedialog as fd
from tkinter import scrolledtext as st

root=Tk()
root.title("Blok de notas")

frame=Frame()
frame.pack()

def acerca_de():
    ms.showinfo("About", "Copyright © 2020 Version 1.0")

def licencia():
    ms.showwarning("License", "Notepad \nLICENSE TERMS. \nThese license terms are an agreement between you and Notepad (or based on where you live, one of its affiliates). They apply to the company named above. The terms also apply to any Notepad services or updates for the company, except to the extent those have different terms.")

def update():
    ms.showinfo("Notepad", "There are currently no updates available")

def welcome():
    ms.showinfo("Benvingut", "")

def salir():
    valor=ms.askquestion("Sortir", "Segur que vols surtir")

    if valor =="yes":
        root.destroy()

def cerrar():
    valor = ms.askquestion("Tanca finestra", "Estas segur que vols tancar la finestra? Pedras tota la informacio que esta ecrita.") #true or false

    if valor == "yes":
        root.destroy()


text = st.ScrolledText(frame, font=("Arial", 12))
text.pack()


def abrirArchivo():
    archivo = fd.askopenfilename(title="Obrir arxiu", filetypes=(
        ("Todos los archivos", "*.*"), ("Archivos de Python", "*.py"), ("Archivos de texto", "*.txt")))
    arch1 = open(archivo, "r", encoding="utf-8")
    contenido=arch1.read()
    arch1.close()
    text.delete("1.0", END)
    text.insert("1.0", contenido)

def guardarArchivo():
    
    archivo = fd.asksaveasfilename(title="Guardar com",  filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")), defaultextension=".txt")
    arch1=open(archivo, "w", encoding="utf-8")
    arch1.write(text.get("1.0", END))
    arch1.close()
    ms.showinfo("Guardar com", "Este arxiu sa guardat correctament.")



barraMenu=Menu()
root.config(menu=barraMenu, width=300, height=300)



files=Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Menu", menu=files)
files.add_command(label="Nou arxiu")
files.add_command(label="Obrir arxiu", command=abrirArchivo)
files.add_separator()
files.add_command(label="Guardar")
files.add_command(label="Guardar com", command=guardarArchivo)
files.add_separator()
files.add_command(label="Sortir", command=salir)



root.mainloop()
