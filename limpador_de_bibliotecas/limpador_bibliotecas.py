import subprocess

# Obtém a lista de bibliotecas instaladas globalmente
pip_list = subprocess.check_output(["pip", "freeze"]).decode("utf-8").strip().split("\n")

# Itera sobre a lista e desinstala cada biblioteca
for package in pip_list:
    subprocess.call(["pip", "uninstall", "-y", package.split("==")[0]])