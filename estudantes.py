estudantes = {
    1: {'nome': 'Joana', 'idade': 45, 'curso': 'Computação'},
    2: {'nome': 'Ivan', 'idade': 70, 'curso': 'Matemática'},
    3: {'nome': 'Jaqueline', 'idade': 12, 'curso': 'Computação'}
}

cursos = { 'Computação', 'Matemática', 'Física' }

estudantes_cursos = {
    'Computação': {1, 3},
    'Matemática': {2}
}

def adicionarEstudante(matricula, nome, idade, curso):
    pessoa = { 'nome': nome, 'idade': idade, 'curso': curso }
    estudantes[matricula] = pessoa
    if curso not in estudantes_cursos:
        estudantes_cursos[curso] = set()
    estudantes_cursos[curso].add(matricula) 

print(estudantes_cursos)
adicionarEstudante(5, 'Jão', 89, 'Computação')
print(estudantes_cursos)
adicionarEstudante(6, 'Maria', 55, 'Física')
print(estudantes_cursos)

#print(f'Todas as pessoas matriculadas em algum curso: {estudantes_cursos['Matemática'] | estudantes_cursos['Computação']}')