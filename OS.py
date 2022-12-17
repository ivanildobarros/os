import os

# Retorna o caminho até o diretório atual
os.getcwd()

# Retorna uma lista de arquivos e pastas do diretório atual
os.listdir()

# Criar pasta
os.mkdir('Pasta')

# Renomear arquivo
os.rename('teste2.txt', 'teste.txt')

# Remover arquivo
os.remove('teste.txt')

# Remover pasta
os.rmdir('Pasta')

# string com comando do sistema
cmd = 'date'
os.system(cmd)