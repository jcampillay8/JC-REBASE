from tkinter import *
from PIL import Image, ImageTk
import os
from tkinter import messagebox
from PyDictionary import PyDictionary
from google_trans_new import google_translator

root = Tk()
root.title("READ ENGLISH BOOK AND STUDY ENGLISH (REBASE)")
root.resizable(width=True,height=True)
root.iconbitmap("North2.ico")

archivotexto_nombre_resolucion_pantalla=open("memory/resolucion_pantalla.txt",encoding="utf8")
resolucion_pantalla=archivotexto_nombre_resolucion_pantalla.read()
archivotexto_nombre_resolucion_pantalla.close()

size=float(resolucion_pantalla)

size_options=["1920x1200","1680x1050","1440x900"]

save_words_setence_options=["SENTENCE","WORD"]

lista_textos=os.listdir(r"texto_lectura")

miCanvas=Canvas(root, width=1920*size, height=1200*size)
miCanvas.pack()

my_img=None
#texto_ENG=None

lista_texto=[]

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
    def window_read():
        global my_img
        global save_words_setence_options
        

        root.withdraw()
        ventana_lectura=Toplevel()
        if size == 1:
                screen_size="1920x1200"
        elif size == 0.875:
                screen_size="1680x1050"
        elif size == 0.75:
                screen_size="1440x900"
        ventana_lectura.geometry(screen_size)
        my_img = ImageTk.PhotoImage(Image.open(fondo_pantalla))
        my_label = Label(ventana_lectura, image=my_img).place(relwidth=1, relheight=1)

        texto_contiene_titulo=open("memory/titulo_texto.txt",encoding="utf8")
        almacena_titulo=texto_contiene_titulo.read()
        texto_contiene_titulo.close()

        texto_contiene_page_marker=open("memory/page_marker.txt",encoding="utf8")
        almacena_page_marker=texto_contiene_page_marker.read()
        texto_contiene_page_marker.close()

        clicked_read=StringVar()
        clicked_read.set(save_words_setence_options[0])

        drop_read_save=OptionMenu(ventana_lectura,clicked_read, *save_words_setence_options)
        drop_read_save.place(x=round(310*size),y=round(820*size))
        drop_read_save.config(width=round(20*size), font=("Book Old Style", round(10*size),"bold"))

        clicked_texto=StringVar()
        clicked_texto.set(lista_textos[0])

        drop_text=OptionMenu(ventana_lectura,clicked_texto, *lista_textos)
        drop_text.place(x=round(1100*size), y=round(120*size))
        drop_text.config(width=round(20*size), font=("Book Old Style", round(10*size),"bold"))

#1 ------------------------------- Funciones Modo Lectura -------------------------------------------
        def texto_inicio():
                num_lista=contador.get()
                camino_texto_lectura="texto_lectura/"+almacena_titulo
                abrir_texto_inicio=open(camino_texto_lectura, encoding="utf8")
                for line in abrir_texto_inicio:                
                        line=line.split(".")
                        line=line[int(num_lista)]
                        line=line[1:]
                        texto_ENG.insert(END, line)
                abrir_texto_inicio.close
        def ingresar_texto():
                
                texto_nuevo=nombre_texto.get()
                camino_texto_lectura="texto_lectura/"+texto_nuevo
                abrir_texto=open(camino_texto_lectura, encoding="utf8")
                lectura_libro_texto=abrir_texto.read()
                abrir_texto.close

                texto_contiene_titulo2=open("memory/titulo_texto.txt","w")
                texto_contiene_titulo2.write(nombre_texto.get())
                texto_contiene_titulo2.close()
                
                messagebox.showinfo("REABSE","*** El texto ha sido cambiado por ***\n\n"+nombre_texto.get()+"\n\n******")

        def spanish_translate_text():
                cntrl=0
                while cntrl==0:
                        num_lista=contador.get()
                        camino_texto_lectura="texto_lectura/"+almacena_titulo
                        abrir_texto=open(camino_texto_lectura, encoding="utf8")
                        
                        try:
                                for line in abrir_texto:
                                        line=line.rstrip("\n")                
                                        line=line.split(".")
                                        linea_Esp=line[int(num_lista)]
                                        translator=google_translator()
                                        translation=translator.translate(linea_Esp,lang_src="en", lang_tgt="es")
                                        texto_ESP.insert(END, translation)
                        except:
                                texto_ESP.insert(END,0)
                        abrir_texto.close()
                        recoger_respuesta=int(texto_ESP.get(1.0,END))
                        if recoger_respuesta == 0:
                                cntrl+=0
                                texto_ESP.delete(1.0,END)
                        else:
                                cntrl+=1
                                

        def next_line():
                texto_ESP.delete(1.0,END)
                texto_ENG.delete(1.0,END)
                cuadro_save_words_setence.delete(0,END)
                dictionary_text.delete(0,END)
                num_lista=contador.get()
                siguiente=int(num_lista)+1
                contador.delete(0,END)
                contador.insert(0,siguiente)

                camino_texto_lectura="texto_lectura/"+almacena_titulo
                abrir_texto_inicio=open(camino_texto_lectura, encoding="utf8")

                for line in abrir_texto_inicio:                
                        line=line.split(".")
                        line=line[siguiente]
                        line=line[1:]
                        texto_ENG.insert(END, line)
                abrir_texto_inicio.close

        
        def previous_line():
                texto_ESP.delete(1.0,END)
                texto_ENG.delete(1.0,END)
                cuadro_save_words_setence.delete(0,END)
                dictionary_text.delete(0,END)
                num_lista=contador.get()
                anterior=int(num_lista)-1
                contador.delete(0,END)
                contador.insert(0,anterior)

                camino_texto_lectura="texto_lectura/"+almacena_titulo
                abrir_texto_inicio=open(camino_texto_lectura, encoding="utf8")

                for line in abrir_texto_inicio:                
                        line=line.split(".")
                        line=line[anterior]
                        line=line[1:]
                        texto_ENG.insert(END, line)
                abrir_texto_inicio.close
        
        def english_dictionary():

                dictionary_word=PyDictionary()
                meaning_word = dictionary_text.get()
                result=dictionary_word.meaning(meaning_word)                                                
                messagebox.showinfo("REABSE","*** DICTIONARY  ***\n\n"+str(result)).options
        
        def page_marker():
                
                marcador_pagina=open("memory/page_marker.txt","w")
                marcador_pagina.write(contador.get())
                messagebox.showinfo("English Assitant","*** El marcador de página ***\n\n"+contador.get()+"\n\n*** ha sido guardado ***")
                marcador_pagina.close()

        def save_word_sentence():
                #global save_words_setence_options
                if clicked_read.get() == "SENTENCE":
                        
                        sentencia_para_estudiar=open("memory/sentencias_para_estudiar.txt","w")
                        sentencia_para_estudiar.write("\n")
                        sentencia_para_estudiar.write(cuadro_save_words_setence.get())
                        messagebox.showinfo("English Assitant","*** La Sentencia ***\n\n"+cuadro_save_words_setence.get()+"\n\n*** fue incluida ***")
                        sentencia_para_estudiar.close()

                elif clicked_read.get() == "WORD":
                        palabra_para_estudiar=open("memory/palabras_para_estudiar.txt","w")
                        palabra_para_estudiar.write("\n")
                        palabra_para_estudiar.write(cuadro_save_words_setence.get())
                        messagebox.showinfo("English Assitant","*** La Palabra ***\n\n"+cuadro_save_words_setence.get()+"\n\n*** fue incluida ***")
                        palabra_para_estudiar.close()

#1 ------------------------------- Botones Modo Lectura -------------------------------------------
        
        button_save_word_setence=Button(ventana_lectura,text="SAVE WORD/SENTENCE ",font=("Bookman Old Style",round(10*size),"bold"), command=save_word_sentence)
        button_save_word_setence.place(x=round(800*size),y=round(size*780))
        button_save_word_setence.config(width=20)

        button_spanish_translate_text=Button(ventana_lectura,text="VER TRADUCCIÓN ",font=("Bookman Old Style",round(12*size),"bold"), command=spanish_translate_text)
        button_spanish_translate_text.place(x=round(70*size),y=round(size*600))
        button_spanish_translate_text.config(bg="#FACC2E", width=15)

        button_texto_inicio=Button(ventana_lectura,text="DAR INICO ",font=("Bookman Old Style",round(12*size),"bold"),command=texto_inicio)
        button_texto_inicio.place(x=round(70*size),y=round(size*300))
        button_texto_inicio.config(bg="#FACC2E", width=15)
        
        button_page_marker=Button(ventana_lectura, text="PAGE MARKER",font=("Bookman Old Style",round(10*size),"bold"),width=12 , command=page_marker)
        button_page_marker.place(x=round(350*size), y=round(460*size))
        button_page_marker.config(bg="#FACC2E")
        
        button_english_dictionary=Button(ventana_lectura, text="ENGLISH DICTIONARY",font=("Bookman Old Style",round(10*size),"bold"),width=20 , command=english_dictionary)
        button_english_dictionary.place(x=round(970*size), y=round(460*size))
        
        button_ingresar_texto=Button(ventana_lectura,text="APPLY NEW TEXT",font=("Bookman Old Style",round(10*size),"bold") , command=ingresar_texto)
        button_ingresar_texto.place(x=round(550*size), y=round(120*size))

        button_next_line=Button(ventana_lectura, text="NEXT",font=("Bookman Old Style",round(10*size),"bold"),width=12 , command=next_line)
        button_next_line.place(x=round(750*size), y=round(460*size))

        button_previous_line=Button(ventana_lectura, text="PREVIOUS",font=("Bookman Old Style",round(10*size),"bold"),width=12 , command=previous_line)
        button_previous_line.place(x=round(550*size), y=round(460*size))

        button_quit = Button(ventana_lectura, text="Exit Program",font=("Bookman Old Style",round(10*size),"bold") , command=root.quit)
        button_quit.place(x=round(800*size), y=round(930*size))

#1 ------------------------------- Cuadro texto Modo Lectura -------------------------------------------

        cuadro_save_words_setence=Entry(ventana_lectura, width=round(75*size), borderwidth=round(5*size), justify="left")
        cuadro_save_words_setence.place(x=round(510*size), y=round(820*size))
        cuadro_save_words_setence.config(font=("Bookman Old Style",round(12*size),"bold"))

        nombre_texto=Entry(ventana_lectura, width=round(35*size), borderwidth=round(5*size), justify="center")
        nombre_texto.place(x=round(700*size), y=round(120*size))
        nombre_texto.config(font=("Bookman Old Style",round(12*size),"bold"))
        nombre_texto.insert(0,almacena_titulo)
        #recoger_nombre_texto=nombre_texto.get()

        dictionary_text=Entry(ventana_lectura, width=round(25*size), borderwidth=round(5*size), justify="center")
        dictionary_text.place(x=round(1170*size), y=round(460*size))
        dictionary_text.config(font=("Bookman Old Style",round(12*size),"bold"))

        texto_ENG=Text(ventana_lectura, width=round(100*size), height=round(4*size), font=("Helvetica",round(16*size)),borderwidth=round(5*size))
        texto_ENG.place(x=round(280*size),y=round(260*size))
        #texto_ENG.insert(END, lista_texto[])

        texto_ESP=Text(ventana_lectura, width=round(100*size), height=round(4*size), font=("Helvetica",round(16*size)),borderwidth=round(5*size))
        texto_ESP.place(x=round(280*size),y=round(560*size))

        contador = Entry(ventana_lectura, width=5, borderwidth=5, justify="center")
        contador.place(x=round(680*size) , y=round(460*size))
        contador.config(font=("Bookman Old Style",round(10*size),"bold"))
        contador.insert(0,almacena_page_marker)
                
#1 ------------------------------- Titulo Modo Lectura -------------------------------------------
        titulo=Label(ventana_lectura, text="READING MODE REBASE", font=("Bookman Old Style",round(30*size)), bg="#e8dabd")
        titulo.place(x=round(650*size), y=round(10*size))
        titulo_texto=Label(ventana_lectura, text="TITLE OF THE TEXT",font=("Bookman Old Style",round(15*size),"bold"),bg="#FACC2E")
        titulo_texto.place(x=round(785*size), y=round(70*size))

#1------------------------------- Etiquetas Modo Lectura -------------------------------------------

        text_save_as=Label(ventana_lectura,text="SAVE AS",font=("Bookman Old Style",round(12*size),"bold"))
        text_save_as.place(x=round(320*size),y=round(size*780))
        text_save_as.config(bg="#FACC2E", width=15)

        

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
                messagebox.showinfo("REABSE","*** El fondo de pantalla ha sido cambiado por ***\n\n"+imagen_eleccion.get()+"\n\n*** Cierre el programa y vuela a abrirlo para ver cambios ***")

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
                messagebox.showinfo("REABSE","*** La resolucion de pantalla ha sido cambiado a ***\n\n"+clicked.get()+"\n\n*** Cierre el programa y vuela a abrirlo para ver cambios ***")

                
#3 ------------------------------- Titulo Modo Lectura -------------------------------------------
        titulo=Label(ventana_configuracion, text="SET CONFIGURATION REBASE", font=("Bookman Old Style",round(30*size)),bg="#e8dabd")
        titulo.place(x=round(600*size), y=(10*size))      

        clicked = StringVar()
        clicked.set(size_options[0])
        
        drop= OptionMenu(ventana_configuracion, clicked, *size_options)
        drop.place(x=round(400*size), y=round(600*size))
        drop.config(width=round(80*size), font=("Bookman Old Style",round(10*size),"bold"))
    
#3 ------------------------------- Botones Configuración -------------------------------------------

        boton_aplicar_fondo_pantalla=Button(ventana_configuracion, text=("APPLY WALLPAPER"),font=("Bookman Old Style",round(12*size),"bold"),width=round(25*size),height=round(1*size), command=cambiar_fondo)
        boton_aplicar_fondo_pantalla.place(x=round(1200*size), y=round(300*size))
        
        boton_read=Button(ventana_configuracion, text=("READ BOOK/TEXT"),font=("Bookman Old Style",round(10*size),"bold"),width=round(25*size),height=round(1*size), command=window_read)
        boton_read.place(x=round(490*size), y=round(900*size))
        boton_study=Button(ventana_configuracion, text=("STUDY ENGLISH"),font=("Bookman Old Style",round(10*size),"bold"), width=round(25*size),height=round(1*size),command=window_study)
        boton_study.place(x=round(1060*size), y=round(900*size))
        
        button_quit = Button(ventana_configuracion, text="Exit Program",font=("Bookman Old Style",round(10*size),"bold") , command=root.quit)
        button_quit.place(x=round(839*size), y=round(970*size))

        boton_size_selection=Button(ventana_configuracion, text=("APPLY SIZE RESOLUTION"),font=("Bookman Old Style",round(12*size),"bold"),width=round(25*size), command=size_selection)
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











