import os

# Carpetas a crear
folders = ["data", "notebook", "src"]

# Contenido de archivos
gitignore_content = """# Ignorar entorno virtual
env/

# Ignorar credenciales sensibles
.env
"""

readme_content = """# Project_2

Descripción breve del proyecto.
"""

requirements_content = """# Requisitos base para análisis de datos
pandas
numpy
matplotlib
seaborn
scikit-learn
statsmodels
openpyxl
plotly
ipywidgets
dotenv
requests

# Para notebooks en VS Code
jupyterlab
ipykernel
"""

# Crear carpetas
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Crear .gitignore
with open(".gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore_content)

# Crear README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

# Crear requirements.txt
with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write(requirements_content)

print("✅ Estructura del proyecto creada con éxito")
