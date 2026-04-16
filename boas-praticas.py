def f(notas):
    media = sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 6:
        return "Aprovado"
    else: 
        return "Reprovado"