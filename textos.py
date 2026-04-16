frase = '   O curso de Lógica de Programação é supimpa!   '
#print(f'Primeira letra: {frase[0]}')
#print(f'Última letra: {frase[-1]}')
#print(f'Tamanho da frase: {len(frase)} caracteres')
#print()
#print(f'Maiúsculas: {frase.upper()}')
#print(f'Minúsculas: {frase.lower()}')
#print()
#print(f'Fatiando: {frase.lower()}')
#print(f'Fatiando: {frase.strip()}')
#print()
#print(f'Frase original: {frase}')
#print(f'Limpando: {frase.strip()}')
#print(f'Tamanho da string limpa: {len(frase.strip())}')

def analisarDeTexto(texto):
    palavras = texto.split()
    num_palavras = len(palavras)
    num_caractes = len(texto)
    num_caracteres_sem_espacos = num_caractes - texto.count(' ')
    return num_palavras, num_caractes, num_caracteres_sem_espacos

num_p, num_c, num_cse = analisarDeTexto(frase)
print(f'Num. palavras: {num_p}')
print(f'Num. caracteres: {num_c}')
print(f'Num. carateres sem espaços: {num_cse}')