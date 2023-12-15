from cx_Freeze import setup, Executable

# Lista de archivos a incluir durante el proceso de congelación
include_files = ['tulips.docx']

# Configuración para cx_Freeze
options = {
    'build_exe': {
        'include_files': include_files,
    },
}

# Definición del ejecutable
executables = [Executable('flower.py')]

# Llamada a la función setup
setup(
    name='FlowerProgram',
    version='1.0',
    description='Your Flower Program Description',
    options=options,
    executables=executables,
)
