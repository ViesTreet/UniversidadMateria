import subprocess
import time
import re
import os

timestamp = int(time.time())
print(timestamp)

# Crear carpeta si no existe
os.makedirs("2026-1/archivosPDF", exist_ok=True)

# Limpiar contenido (sin borrar la carpeta)
subprocess.run("rm -f 2026-1/archivosPDF/*", shell=True)

# Función para convertir sintaxis Obsidian
def convertir_obsidian(md_text):
    # Agregamos < > alrededor de la ruta para que Pandoc acepte los espacios
    return re.sub(r'!\[\[(.*?)(\|.*?)?\]\]', r'![](<\1>)', md_text)

result = subprocess.run(
    "ls -d 2026-1/*/",
    shell=True,
    capture_output=True,
    text=True
)

respuesta = result.stdout.strip().split("\n")

for res in respuesta:
    consulta = subprocess.run(
        f"ls '{res.strip()}'",
        shell=True,
        capture_output=True,
        text=True
    )

    archivos = consulta.stdout.strip().split("\n")

    for con in archivos:
        if con.endswith(".md") and "dib" not in con.lower():

            ruta_md = res + con
            print(ruta_md)

            # Leer archivo
            with open(ruta_md, "r", encoding="utf-8") as f:
                contenido = f.read()

            # Convertir sintaxis Obsidian
            contenido = convertir_obsidian(contenido)

            # Archivo temporal único (para evitar conflictos)
            temp_md = f"temp_{timestamp}.md"

            with open(temp_md, "w", encoding="utf-8") as f:
                f.write(contenido)

            nombre = con.replace(".md", "")

            subprocess.run(
                f"pandoc '{temp_md}' "
                f"-f gfm "
                f"--pdf-engine=xelatex "
                f"-o '2026-1/archivosPDF/{nombre}.pdf' "
                f"--resource-path='2026-1/Adjuntos'",
                shell=True
            )

            # Borrar temporal
            os.remove(temp_md)