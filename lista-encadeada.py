lista = {}

def exibeLista():
    if not lista:
        print('Lista vazia.')
        return
    elemento = lista

    while elemento != None:
        print(elemento['valor'], end=' ')
        elemento = elemento['proximo']

    print('.')

def adicionaNoFim(elemento):
    global lista
    if not lista:
        lista = { 'valor': elemento, 'proximo': None}
        return
    atual = lista
    while atual['proximo']:
        atual = atual['proximo']
    atual = atual['proximo'] = { 'valor': elemento, 'proximo': None}

exibeLista()
print('Adicionar o 5...')
adicionaNoFim(5)
exibeLista()
print('Adicionar o 8...')
adicionaNoFim(8)
exibeLista()
print('Adicionar o 13...')
adicionaNoFim(13)
exibeLista()