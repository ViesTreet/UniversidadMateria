import tkinter as tk
from tkinter import filedialog
import subprocess
from pdf2image import convert_from_path
from time import time

carpetaAdj = "2026-2/Adjuntos/"
rutaInput = None
rutaOutput = None

def convert_ppt_to_pdf():
    global rutaInput
    nombreArchivo = str(rutaInput).strip().split("/")
    nombreArchivo = nombreArchivo[-1].strip().split(".")
    nombreArchivo = nombreArchivo[0]
    cmd = ["libreoffice", "--headless", "--convert-to", "pdf", rutaInput, "--outdir", carpetaAdj]
    subprocess.run(cmd, check=True)
    rutaInput = f"{carpetaAdj}{nombreArchivo}.pdf"

def get_file_path_input():
    file_path = filedialog.askopenfilename(filetypes=[("archivo",("*.pdf","*ppt","*pptx"))])
    
    if file_path:
        global rutaInput
        rutaInput = file_path
    

def get_file_path_input_output():
    file_path = filedialog.askopenfilename(filetypes=[("archivo","*.md")])
    
    if file_path:
        global rutaOutput
        rutaOutput = file_path
    
def general_convert():
    tempStamp = int(time())
    if(rutaInput != None and rutaOutput != None):
        if ".pdf" in rutaInput:
            imagenes = convert_from_path(rutaInput)
        else:
            convert_ppt_to_pdf()
            imagenes = convert_from_path(rutaInput)
            subprocess.run(["rm", rutaInput], check=True)


        with open(rutaOutput, "a", encoding="utf-8") as f:
            for i, imagen in enumerate(imagenes):
                imagen.save(f'{carpetaAdj}{tempStamp}_{i+1}.png', 'PNG')
                f.write(f"![[{tempStamp}_{i+1}.png]]\n\n")

    

root = tk.Tk()
root.title("Agregar materia al obsidian")
root.geometry("400x200")

btn = tk.Button(root, text="Agregar materia", command=get_file_path_input)
btn.pack(pady=20)
btn = tk.Button(root, text="Obsidian", command=get_file_path_input_output)
btn.pack(pady=0)
btn = tk.Button(root, text="Ejecutar", command=general_convert)
btn.pack(pady=20)


root.mainloop()
