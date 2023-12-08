import tkinter as tk
from tkinter import filedialog
#import openai

def subir_archivo():
    archivo = filedialog.askopenfilename()
    if archivo:
        etiqueta_archivo.config(text=f"Archivo seleccionado: {archivo}")

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("D5Jo Music")

    # Crear frames para las secciones
    frame_izquierdo = tk.Frame(ventana, bg="blue", width=100, height=100)
    frame_derecho = tk.Frame(ventana, bg="green", width=100, height=100)

    # Ubicar los frames en la ventana de forma horizontal con grid
    frame_izquierdo.grid(row=0, column=0, sticky="nsew")
    frame_derecho.grid(row=0, column=1, sticky="nsew")

    # Dividir la sección izquierda en dos frames verticales
    frame_izquierdo_arriba = tk.Frame(frame_izquierdo, bg="purple", width=100, height=100)
    frame_izquierdo_abajo = tk.Frame(frame_izquierdo, bg="orange", width=100, height=100)

    frame_izquierdo_arriba.pack(fill=tk.BOTH, expand=True)
    frame_izquierdo_abajo.pack(fill=tk.BOTH, expand=True)

    # Contenido para el frame izquierdo superior
    etiqueta_archivo = tk.Label(frame_izquierdo_arriba, text="Sube tu música en .mp3", fg="white", bg="purple")
    etiqueta_archivo.pack(padx=20, pady=20)  # Añadir la etiqueta al frame_izquierdo_arriba

    boton_subir = tk.Button(frame_izquierdo_arriba, text="Subir Archivo", command=subir_archivo)
    boton_subir.pack(padx=10, pady=10)  # Añadir un botón al frame_izquierdo_arriba

    # Contenido para el frame izquierdo inferior
    etiqueta_placeholder = tk.Label(frame_izquierdo_abajo, text="Sube la letra de tu música", fg="white", bg="orange")
    etiqueta_placeholder.pack(padx=20, pady=20)  # Añadir etiqueta de relleno al frame_izquierdo_abajo

    boton_subir = tk.Button(frame_izquierdo_abajo, text="Subir Archivo", command=subir_archivo)
    boton_subir.pack(padx=10, pady=10)  # Añadir un botón al frame_izquierdo_arriba

    # Dividir la sección derecha en dos frames horizontales
    frame_derecho_arriba = tk.Frame(frame_derecho, bg="red", width=100, height=100)

    opciones = ["Opción 1", "Opción 2", "Opción 3"]
    seleccion = tk.StringVar()
    seleccion.set(opciones[0])

    etiqueta_seleccion = tk.Label(frame_derecho_arriba, text="Has seleccionado: ", bg="red")
    etiqueta_seleccion.pack(padx=20, pady=20)

    menu_seleccion = tk.OptionMenu(frame_derecho_arriba, seleccion, *opciones)
    menu_seleccion.pack(padx=20, pady=20)  # Añadir menú de selección al frame_derecho_arriba


    frame_derecho_abajo = tk.Frame(frame_derecho, bg="yellow", width=700, height=730)

    frame_derecho_arriba.pack(fill=tk.BOTH, expand=True)
    frame_derecho_abajo.pack(fill=tk.BOTH, expand=True)

    # Ajustar el tamaño de las columnas
    ventana.grid_columnconfigure(0, weight=1)  # Columna 0 con más peso
    ventana.grid_columnconfigure(1, weight=2)  # Columna 1 con menos peso

    ventana.mainloop()

crear_ventana()



