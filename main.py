import tkinter as tk
from tkinter import filedialog
from openai import OpenAI

archivo = None
ventana = tk.Tk()
ventana.title("D5Jo Music-Free")

# Crear frames para las secciones
frame_izquierdo = tk.Frame(ventana, bg="blue", width=100, height=100, relief=tk.GROOVE, bd=2)
frame_derecho = tk.Frame(ventana, bg="green", width=100, height=100, relief=tk.GROOVE, bd=2)

# Ubicar los frames en la ventana de forma horizontal con grid
frame_izquierdo.grid(row=0, column=0, sticky="nsew")
frame_derecho.grid(row=0, column=1, sticky="nsew")

# Dividir la sección izquierda en dos frames verticales
frame_izquierdo_arriba = tk.Frame(frame_izquierdo, bg="purple", width=100, height=100, relief=tk.GROOVE, bd=2)
frame_izquierdo_abajo = tk.Frame(frame_izquierdo, bg="orange", width=100, height=100, relief=tk.GROOVE, bd=2)

frame_izquierdo_arriba.pack(fill=tk.BOTH, expand=True)
frame_izquierdo_abajo.pack(fill=tk.BOTH, expand=True)

# Contenido para el frame izquierdo superior
etiqueta_archivo = tk.Label(frame_izquierdo_arriba, text="\n\n\n\n\n\n\nAquí sube tu música en .mp3", fg="white", bg="purple")
etiqueta_archivo.pack(padx=20, pady=20)  # Añadir la etiqueta al frame_izquierdo_arriba

def subir_audio():
    archivo = filedialog.askopenfilename(filetypes=[("Archivo de audio", ".mp3")])
    if archivo:
        etiqueta_archivo.config(text=f"Archivo seleccionado: {archivo}")

boton_subir = tk.Button(frame_izquierdo_arriba, text="Subir Archivo", command=subir_audio)
boton_subir.pack(padx=10, pady=10)  # Añadir un botón al frame_izquierdo_arriba

# Contenido para el frame izquierdo inferior
etiqueta_placeholder = tk.Label(frame_izquierdo_abajo, text="\n\n\n\n\n\n\nAquí sube la letra de tu música en .docx o .txt", fg="white", bg="orange")
etiqueta_placeholder.pack(padx=20, pady=20)  # Añadir etiqueta de relleno al frame_izquierdo_abajo

def subir_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivo de texto", ".docx .txt")])
    if archivo:
        etiqueta_placeholder.config(text=f"Archivo seleccionado: {archivo}")

boton_subir = tk.Button(frame_izquierdo_abajo, text="Subir Archivo", command=subir_archivo)
boton_subir.pack(padx=10, pady=10)  # Añadir un botón al frame_izquierdo_arriba

# Dividir la sección derecha en dos frames horizontales
frame_derecho_arriba = tk.Frame(frame_derecho, bg="coral", width=100, height=100)

opciones = ["Rock", "Blues", "Latino", "Jazz", "Pop", "Reggae", "Soul", "Funk", "R&B", "Country", "Hip Hop", "Metal", "Clásica"]
seleccion = tk.StringVar()
seleccion.set(opciones[0])

etiqueta_seleccion = tk.Label(frame_derecho_arriba, text="Género:", bg="coral")
etiqueta_seleccion.pack(padx=20, pady=20)

menu_seleccion = tk.OptionMenu(frame_derecho_arriba, seleccion, *opciones)
menu_seleccion.pack(padx=20, pady=20)  # Añadir menú de selección al frame_derecho_arriba


frame_derecho_abajo = tk.Frame(frame_derecho, bg="black", width=700, height=730, relief=tk.GROOVE, bd=2)

def enviar_mensaje():
    mensaje_usuario = campo_entrada.get()  # Obtener el texto del campo de entrada
    if mensaje_usuario:
        # Hacer la solicitud a la API de OpenAI
        client = OpenAI(api_key="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")
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": mensaje_usuario
                }
            ],
            model="gpt-3.5-turbo"
        )
        # Obtener la respuesta de ChatGPT
        respuesta_chatgpt = chat_completion.choices[0].message.content

        # Mostrar la conversación en el área de respuesta
        area_respuesta.insert(tk.END, f"Usuario: {mensaje_usuario}\n")
        area_respuesta.insert(tk.END, f"ChatGPT: {respuesta_chatgpt}\n\n")

# Crear campo de entrada para el usuario
campo_entrada = tk.Entry(frame_derecho_abajo, width=50)
campo_entrada.pack(padx=20, pady=10)

# Crear área para mostrar las respuestas de ChatGPT
area_respuesta = tk.Text(frame_derecho_abajo, height=20, width=50)
area_respuesta.pack(padx=20, pady=10)

# Botón para enviar mensaje a ChatGPT
boton_enviar = tk.Button(frame_derecho_abajo, text="Enviar", command=enviar_mensaje)
boton_enviar.pack(padx=20, pady=10)


frame_derecho_arriba.pack(fill=tk.BOTH, expand=True)
frame_derecho_abajo.pack(fill=tk.BOTH, expand=True)

# Ajustar el tamaño de las columnas
ventana.grid_columnconfigure(0, weight=1)  # Columna 0 con más peso
ventana.grid_columnconfigure(1, weight=2)  # Columna 1 con menos peso

ventana.mainloop()

#crear_ventana()
