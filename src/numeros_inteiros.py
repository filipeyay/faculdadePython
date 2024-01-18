# Neste exercicio o programa deve fazer 2 numeros inteiros e um numero float

# 1-O resultado do dobro do primeiro numero com metade do segundo .
# 2-A soma do triplo do primeiro numero com o terceiro.
# 3-O terceiro numero elevado ao cubo.

# Nota(1)Números float são números com parte decimal/e a função 'float' permite que eu os armazene

# Nota(2)Tudo que o usuario enviar como resposta será interpretado como string(um tipo de texto)
# para reverter isso eu devo transformalo em um numero inteiro com a função int

numero_1 = int(input('Digite um número inteiro: '))
numero_2 = int(input('Digite outro número inteiro: '))
numero_3 = float(input('Digite um número float(um número decimal): '))

# O resultado é mostrado a partir de instruções de caracteres que o python consegue interpretar para
# poder fazer uma conta matematica

# 1-O resultado do dobro do primeiro com metade do segundo
resultado_1 = (numero_1 * 2) * (numero_2 / 2)

# Na instrução acima eu digo que o resultado vai imprimir a mutiplicação do primeiro numero dado pelo
# usuario por dois, em seguda ele vai dividir o segundo numero dado pelo usuario por 2
# e por ultimo vai mutiplicar os dois resultados

# 2-A soma do triplo do primeiro com o terceiro
resultado_2 = numero_1 * 3 + numero_3

# Na intrução acima outra conta matematica é feita, assim como na matematica os parenteses são usados
# para ajudar e organizar a ordem das contas e nesse caso não foi necessario o uso do mesmo

# 3-O terceiro numero elevado ao cubo
resultado_3 = numero_3 ** 3

# Na intrução acima a ultima conta é feita, onde os ** são usados para elevar o numero (no exemplo é elevado ao cubo(3))

print('\n')

# resultados
print(f'Resultado 1: {resultado_1}')
print(f'Resultado 2: {resultado_2}')
print(f'Resultado 3: {resultado_3}')
