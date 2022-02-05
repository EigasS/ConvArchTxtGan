
import tkinter
from tkinter.filedialog import askopenfilename

ventana = tkinter.Tk()
ventana.geometry("300x300")
ventana.title("Conv Arch Gan SICORE")


def explorarArchivos():
    flName = askopenfilename(title="Seleccione un archivo a convertir")
    def procesaLinea(linea):
        linea = linea[0:76] + '01' + linea[78:]
        return linea
    if __name__ == '__main__':
        fIn = open(flName,'r')
    fOut = open("destino.txt","w")
    for linea in fIn:
        linea = procesaLinea(linea)
        fOut.write(linea)
    fOut.close()
    fIn.close()
    label.configure(text="Conversion Exitosa", fg ="green")

boton= tkinter.Button(ventana, text = "Elegir", fg = "white", bg = "blue", padx= 20, pady =20, font = 10, command = explorarArchivos)
boton.pack(pady =50)

label = tkinter.Label(ventana, text = "Añadir Archivo", pady = 20, font = (20))
label.pack()
ventana.mainloop()



