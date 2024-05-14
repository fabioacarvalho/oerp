import os
from importlib import import_module

"""
Este módulo importa todas as views que estão neste modulo
"""

# Obtenha o diretório atual do script
current_directory = os.path.dirname(__file__)

# Diretório que contém os arquivos que você deseja importar
directory_to_import = os.path.join(current_directory, 'views')

# Percorra todos os arquivos no diretório
for filename in os.listdir(directory_to_import):
    # Verifique se é um arquivo Python
    # if filename.endswith('_views.py'):
    if filename.endswith('.py') and filename != '__init__.py' and filename != 'views.py' and filename != 'urls.py':
        # Remova a extensão do arquivo
        module_name = filename[:-3]
        # Importe o módulo
        module = import_module(f'views.{module_name}')
