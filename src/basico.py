# variaveis
y = 1
x = y + 2
print(x)

# strings
x = "abc"
y = "de"
z = x + y
print (z)

z = z [1:3] # os numeros são referentes as letras, nesse caso 1 = a não vai ser mostrado no resultado. caso tivesse algum caractere antes do a ele tbm não seria mostrado//o numero da direita são as letras que devem aparecer
print (z)

# funções
def f(x):
    y = x+2
    return y
f(5)
print(f(5))

# if
x = 2
if x+1 == 3:
    print(x) # traduzindo ==> se x é igual a 2, então x+1 é igual 3? Se verdadeiro vai mostrar x no console.

# loops
for i in range(1, 100):
    if i%2 == 0:
        print(i) # mostra todos os numeros divididos por 2