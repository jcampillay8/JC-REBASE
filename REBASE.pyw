from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox

root = Tk()
root.title("READ ENGLISH BOOK AND STUDY ENGLISH (REBASE)")
root.resizable(width=True,height=True)
root.iconbitmap("North2.ico")

archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt",encoding="utf8")
resolucion_pantalla=archivotexto_nombre_resolucion_pantalla.read()
archivotexto_nombre_resolucion_pantalla.close()

size=float(resolucion_pantalla)

size_options=["1920x1200","1680x1050","1440x900"]

miCanvas=Canvas(root, width=1920*size, height=1200*size)
miCanvas.pack()

my_img=None

camino_carpeta_images="images/"

archivotexto_nombre_fondo_panatalla=open("memory/nombre_fondo_pantalla.txt",encoding="utf8")

fondo_pantalla = camino_carpeta_images+archivotexto_nombre_fondo_panatalla.read()

archivotexto_nombre_fondo_panatalla.close()

background_image = PhotoImage(file=str(fondo_pantalla))
background_label = Label(root, image=background_image).place(relwidth=1, relheight=1)

def home():
#------------------------------- Titulo Pagina Inicio -------------------------------------------

    titulo=Label(background_label, text="WELCOME TO REBASE", font=("Bookman Old Style",round(30*size)),bg="#e8dabd")
    titulo.place(x=650*size, y=0*size)
    titulo=Label(background_label, text=" READ ENGLISH BOOK AND STUDY ENGLISH", font=("Bookman Old Style",round(30*size)),bg="#e8dabd")
    titulo.place(x=430*size, y=60*size)
    titulo=Label(background_label, text=" PLEASE, CHOOSE AN OPTION", font=("Bookman Old Style",round(30*size)),bg="#e8dabd")
    titulo.place(x=573*size, y=120*size)
    
#1 ------------------------------- Ventana Modo Lectura -------------------------------------------
#1 ------------------------------- Funciones Modo Lectura -------------------------------------------
    def window_read():
        global my_img
        root.withdraw()
        ventana_lectura=Toplevel()
        #ventana_lectura.state(newstate='normal')
        ventana_lectura.geometry("1800x1100")
        my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
        my_label = Label(ventana_lectura, image=my_img).place(relwidth=1, relheight=1)

#1 ------------------------------- Botones Modo Lectura -------------------------------------------
        button_quit = Button(ventana_lectura, text="Exit Program",font=("Bookman Old Style",10,"bold") , command=root.quit)
        button_quit.place(x=800, y=900)

#1 ------------------------------- Titulo Modo Lectura -------------------------------------------
        titulo=Label(ventana_lectura, text="READING MODE REBASE", font=("Bookman Old Style",30),bg="#e8dabd")
        titulo.place(x=650, y=0)


#2 ------------------------------- Ventana Modo Estudio -------------------------------------------
    def window_study():
        return
#3 ------------------------------- Ventana Configuración -------------------------------------------
#3 ------------------------------- Funciones Configuracióm -------------------------------------------
    def configuracion():
        global my_img
        root.withdraw()
        ventana_configuracion=Toplevel()
        if size == 1:
                screen_size="1920x1200"
        elif size == 0.875:
                screen_size="1680x1050"
        elif size == 0.75:
                screen_size="1440x900"
        
        ventana_configuracion.geometry(screen_size)
        my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
        my_label = Label(ventana_configuracion, image=my_img).place(relwidth=1, relheight=1)

        def cambiar_fondo():
                recoger_nombre_fondo_pantalla=imagen_eleccion.get()
                archivotexto_nombre_fondo_panatalla=open("memory/nombre_fondo_pantalla.txt","w")
                archivotexto_nombre_fondo_panatalla.write(recoger_nombre_fondo_pantalla)
                archivotexto_nombre_fondo_panatalla.close()
                messagebox.showinfo("REABSE","*** El fondo de pantalla ha sido cambiado por ***\n\n"+imagen_eleccion.get()+"\n\n*** Cierre el programa y vuela a abrirlo ***")

        def size_selection():
                global size
                #election_size = Label(ventana_configuracion, text=clicked.get())
                if clicked.get() == "1920x1200":
                        size=1
                elif clicked.get() == "1680x1050":
                        size=0.875
                elif clicked.get() == "1440x900":
                        size=0.75
                
                archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt","w")                
                
                resolucion_pantalla=archivotexto_nombre_resolucion_pantalla.write(str(size))
                archivotexto_nombre_resolucion_pantalla.close()
                messagebox.showinfo("REABSE","*** El fondo de pantalla ha sido cambiado por ***\n\n"+clicked.get()+"\n\n*** Cierre el programa y vuela a abrirlo ***")

                
#3 ------------------------------- Titulo Modo Lectura -------------------------------------------
        titulo=Label(ventana_configuracion, text="SET CONFIGURATION REBASE", font=("Bookman Old Style",round(30*size)),bg="#e8dabd")
        titulo.place(x=round(600*size), y=(10*size))      

        clicked = StringVar()
        clicked.set(size_options[0])
        drop= OptionMenu(ventana_configuracion, clicked, *size_options)
        drop.place(x=round(400*size), y=round(600*size))
    
#3 ------------------------------- Botones Configuración -------------------------------------------

        boton_aplicar_fondo_pantalla=Button(ventana_configuracion, text=("APPLY WALLPAPER"),font=("Bookman Old Style",round(12*size),"bold"),width=round(25*size),height=round(1*size), command=cambiar_fondo)
        boton_aplicar_fondo_pantalla.place(x=round(1200*size), y=round(300*size))
        
        boton_written=Button(ventana_configuracion, text=("READ BOOK/TEXT"),font=("Bookman Old Style",round(10*size),"bold"),width=round(25*size),height=round(1*size), command=window_read)
        boton_written.place(x=round(490*size), y=round(900*size))
        boton_listen=Button(ventana_configuracion, text=("STUDY ENGLISH"),font=("Bookman Old Style",round(10*size),"bold"), width=round(25*size),height=round(1*size),command=window_study)
        boton_listen.place(x=round(1060*size), y=round(900*size))
        
        button_quit = Button(ventana_configuracion, text="Exit Program",font=("Bookman Old Style",round(10*size),"bold") , command=root.quit)
        button_quit.place(x=round(839*size), y=round(970*size))

        boton_size_selection=Button(ventana_configuracion, text="Select Size Resolution", command=size_selection)
        boton_size_selection.place(x=round(1200*size), y=round(600*size))

#3 ------------------------------- Cuadro de texto Configuración -------------------------------------------

        imagen_eleccion=Entry(ventana_configuracion,width=round(50*size), borderwidth=round(5*size), justify="center")
        imagen_eleccion.place(x=round(400*size), y=round(300*size))
        imagen_eleccion.config(font=("Bookman Old Style",round(18*size)))

#3------------------------------- Etiquetas Ventana Configuración -------------------------------------------

        texto_set_image_label=Label(ventana_configuracion,text="Set Image's Name Here: ")
        texto_set_image_label.place(x=round(100*size),y=round(300*size))
        texto_set_image_label.config(bg="#FACC2E", width=round(20*size), font=("Bookman Old Style",round(15*size),"bold"))

        texto_set_image_label=Label(ventana_configuracion,text="Set Resolution Here: ")
        texto_set_image_label.place(x=round(100*size),y=round(600*size))
        texto_set_image_label.config(bg="#FACC2E", width=round(20*size), font=("Bookman Old Style",round(15*size),"bold"))
        
#------------------------------- Botones Funciones Ventana inicio -------------------------------------------
    boton_written=Button(background_label, text=("READ BOOK/TEXT"),font=("Bookman Old Style",round(15*size),"bold"),width=round(25*size),height=round(2*size), command=window_read)
    boton_written.place(x=230*size, y=400*size)
    boton_listen=Button(background_label, text=("STUDY ENGLISH"),font=("Bookman Old Style",round(15*size),"bold"), width=round(25*size),height=round(2*size),command=window_study)
    boton_listen.place(x=1245*size, y=400*size)
    button_quit = Button(background_label, text="Exit Program",font=("Bookman Old Style",round(10*size),"bold") , command=root.quit)
    button_quit.place(x=839*size, y=970*size)

    boton_configuracio=Button(background_label, text="SET CONFIGURATION",font=("Bookman Old Style",round(10*size),"bold"), width=round(20*size) , command=configuracion)
    boton_configuracio.place(x=800*size, y=900*size)
    boton_configuracio.config(bg="#FACC2E")

home()

root.mainloop()











