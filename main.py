from tkinter import *
from math import *
# Configuración ventana principal
root = Tk()
root.title("Calculadora python")
root.resizable(0,0)
root.geometry("290x255")   
def tecla(t):
    global o
    o=o+str(t)
    entrada.set(o)
    
def result():
    global o 
    try:
        a=str(eval(o))#evalua una cadena como expresion de python retorna un resultado con el tipo analizado
        entrada.set(a) 
    except:
        entrada.set("")   
    o="" 

o=""   
entrada=StringVar()#Variable de control entrada asignada como tipo string 

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 20, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=0, pady=0)
label=Label(pantalla,width=40,height=2,bg="black", fg="white",borderwidth=0,textvariable=entrada)
label.grid(row=0, column=0)  
# Configuración botones
boton_1 = Button(root, text="1", command=lambda: tecla(1),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", command=lambda: tecla(2),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", command=lambda: tecla(3),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", command=lambda: tecla(4),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=0, padx=1, pady=2)
boton_5 = Button(root, text="5", command=lambda: tecla(5),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", command=lambda: tecla(6),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=2,column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", command=lambda: tecla(7),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", command=lambda: tecla(8),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", command=lambda: tecla(9),width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2").grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", command=result,width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".",command=lambda: tecla("."), width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+",command=lambda: tecla("+"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-",command=lambda: tecla("-"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*", command=lambda: tecla("*"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/",command=lambda: tecla("/"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

root.mainloop()