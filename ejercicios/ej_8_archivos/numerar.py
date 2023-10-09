with open ('numerar.py','rt') as archivo:
    for i, linea in enumerate(archivo, 1):
        print(f'{i}: {linea}', end='')
