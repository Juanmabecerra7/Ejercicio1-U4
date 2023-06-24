from tkinter import *
from tkinter import ttk, messagebox
class Aplicacion():
    __ventana =None
    __cantidadVestimenta = None
    __precioBaseVestimenta = None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("400x250")
        self.__ventana.configure(bg="beige")
        self.__ventana.title("Aplicacion")
        mainframe = ttk.Frame(self.__ventana, padding="6 6 24 24")
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe["borderwidth"]=2
        mainframe["relief"]="sunken"
        self.__cantidadVestimenta = StringVar()
        self.__cantidadAlimentos = StringVar()
        self.__cantidadEducacion =StringVar()
        self.__precioBaseVestimenta = StringVar()
        self.__precioBaseAlimentos = StringVar()
        self.__precioBaseEducacion = StringVar()
        self.__precioActualVestimenta = StringVar()
        self.__precioActualAlimentos = StringVar()
        self.__precioActualEducacion = StringVar()
        self.__IPC = StringVar()
        ttk.Label(mainframe, text="Item").grid(column=1, row=1, sticky=(N))
        ttk.Label(mainframe, text= "Cantidad").grid(column=2, row=1, sticky=(N))
        ttk.Label(mainframe, text="Precio Base Año").grid(column=3, row=1, sticky=(N))
        ttk.Label(mainframe, text="Precio Base Actual").grid(column=4, row=1, sticky=(N))
        ttk.Label(mainframe, text="Vestimenta").grid(column=1, row=2, sticky=(N))
        ttk.Label(mainframe, text="Alimentos").grid(column=1, row=3, sticky=(N))
        ttk.Label(mainframe, text="Educacion").grid(column=1, row=4, sticky=(N))
        #VESTIMENTA
        self.cantidadVestimentaEntry = ttk.Entry(mainframe, width=7, textvariable=self.__cantidadVestimenta)
        self.cantidadVestimentaEntry.grid(column=2, row=2 , sticky=(N))
        self.precioBaseVestimentaEntry =ttk.Entry(mainframe, width=7, textvariable=self.__precioBaseVestimenta)
        self.precioBaseVestimentaEntry.grid(column=3, row=2, sticky=N)
        self.precioActualVestimentaEntry = ttk.Entry(mainframe, width=7, textvariable=self.__precioActualVestimenta)
        self.precioActualVestimentaEntry.grid(column=4, row=2, sticky=N)
        #-----------------
        #ALIMENTOS
        self.cantidadAlimentosEntry = ttk.Entry(mainframe, width=7, textvariable=self.__cantidadAlimentos)
        self.cantidadAlimentosEntry.grid(column=2, row=3, sticky=(N))
        self.precioBaseAlimentosEntry =ttk.Entry(mainframe, width=7, textvariable=self.__precioBaseAlimentos)
        self.precioBaseAlimentosEntry.grid(column=3, row=3, sticky=N)
        self.precioActualAlimentosEntry = ttk.Entry(mainframe, width=7, textvariable=self.__precioActualAlimentos)
        self.precioActualAlimentosEntry.grid(column=4, row=3, sticky=N)
        #-------------------
        #EDUCACION
        self.cantidadEducacionEntry = ttk.Entry(mainframe, width=7, textvariable=self.__cantidadEducacion)
        self.cantidadEducacionEntry.grid(column=2, row=4, sticky=(N))
        self.precioBaseEducacionEntry =ttk.Entry(mainframe, width=7, textvariable=self.__precioBaseEducacion)
        self.precioBaseEducacionEntry.grid(column=3, row=4, sticky=N)
        self.precioActualEducacionEntry = ttk.Entry(mainframe, width=7, textvariable=self.__precioActualEducacion)
        self.precioActualEducacionEntry.grid(column=4, row=4, sticky=N)
        #--------------------
        #IPC
        ttk.Label(mainframe, textvariable=self.__IPC).grid(column=2, row=6, sticky=S)
        ttk.Label(mainframe, text="IPC %:").grid(column=1, row=5, sticky=S)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=6, pady=7)
        ttk.Button(mainframe, text="Exit",command=self.__ventana.destroy).grid(column=4, row=6, sticky=(S))
        ttk.Button(mainframe, text="Calcular IPC", command=self.calcular).grid(column=2, row=6, sticky=S)
        ttk.Button(mainframe, text="Limpiar", command=self.limpiar).grid(column=3, row=6, sticky=S)
        self.__ventana.mainloop()
        
    def calcular(self):
        try:
            valor1=float(self.cantidadVestimentaEntry.get())+float(self.cantidadEducacionEntry.get())+float(self.cantidadAlimentosEntry.get())
            valor2=float(self.precioActualVestimentaEntry.get())+float(self.precioActualEducacionEntry.get())+float(self.precioActualAlimentosEntry.get())
            valor3=float(self.precioBaseVestimentaEntry.get())+float(self.precioBaseEducacionEntry.get())+float(self.precioBaseAlimentosEntry.get())
            costoActual=float(valor1*valor2)
            costoBase=float(valor1*valor3)
            ipc = int(costoActual+costoBase)/100
            self.__IPC.set(ipc)
        except ValueError:
            messagebox.showerror(title="Error", message="Deben llenarse todos los campos con datos numericos")

    def limpiar(self):
        self.__cantidadVestimenta.set("")
        self.__cantidadEducacion.set("")
        self.__cantidadAlimentos.set("")
        self.__precioActualAlimentos.set("")
        self.__precioActualEducacion.set("")
        self.__precioActualVestimenta.set("")
        self.__precioBaseAlimentos.set("")
        self.__precioBaseEducacion.set("")
        self.__precioBaseVestimenta.set("")


def testAPP():
    mi_app = Aplicacion()

if __name__=="__main__":
    testAPP()