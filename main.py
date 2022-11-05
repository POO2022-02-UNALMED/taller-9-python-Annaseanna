from tkinter import Tk, Button, Entry, Label

# Configuración ventana principal
root = Tk()
root.title("Calculadora python")
root.resizable(0,0)
root.geometry("290x255")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=0, pady=0)
label=Label(pantalla,width=40,height=2, bg="black", fg="white",borderwidth=0)
label.grid(row=0, column=0)
result=0
x=0
y=0     

def tecla(t):
    global x
    global y
    if x==0:
        x=t 
    if x!=0 and y==0:
        y=t
                       
def operacion():
    global result
    global x
    global y
    x=0
    y=0
    label.config(text=str(result))
    
def operador(o):
    global x
    global y
    global result
    if o=="+":
        result=x+y
    elif o=="-":
        result=x-y
    elif o=="*":
        result=x*y
    elif o=="/" and y!=0:
        result=x/y
    else:
        result=x/1  
    
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
boton_igual = Button(root, text="=", command=lambda: operacion(),width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2").grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".",command=lambda: operador("."), width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+",command=lambda: operador("+"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-",command=lambda: operador("-"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, command=lambda: operador("*"),text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/",command=lambda: operador("/"), width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2").grid(row=4, column=3, padx=1, pady=1)

root.mainloop()