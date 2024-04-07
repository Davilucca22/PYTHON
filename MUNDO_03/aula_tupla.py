lanche = ('hamburguer','suco','pizza','pudim')
for c in lanche:
    print(f'{c}',end=' ')

print()
print(f'essa tupla tem {len(lanche)} itens')

print(30*'-')

a = (1,2,5)
b = (9,3,5,4,6)
c = a + b 
print(c)
print(c.index(5,3))

print(30*'-')

#tuplas aceitam diversos tipos

exempl = ('lucca',18,'m',76)
print(exempl)
del(exempl)
print(exempl)
