# tupla

latitude = '-28.2612'
longitude = '-52.4083'

pontos = (latitude, longitude)
print(pontos)
print(pontos[0])
print(pontos[1])

#pontos[0] = 'abc'
#print(pontos)

# recebe uma tupla como parametro, inves de dois parametros
# imutavel .. ou pode ser alterada apos declaracao
def processa_pontos(pontos):
    lat = pontos[0]
    lng = pontos[1]


    
