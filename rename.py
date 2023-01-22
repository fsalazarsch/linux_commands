import os

# Define la ruta de la carpeta que deseas procesar
folder_path = "C:\\laragon\\www\\linux_commands\\img"


# Itera sobre todos los archivos en la carpeta especificada
for filename in os.listdir(folder_path):
    # Obtiene la ruta completa del archivo
    file_path = os.path.join(folder_path, filename)
    # Comprueba si el archivo es un archivo regular
    if os.path.isfile(file_path):
        # Renombra el archivo con su nombre en minúsculas
        new_name = filename.lower()
        os.rename(file_path, os.path.join(folder_path, new_name))

