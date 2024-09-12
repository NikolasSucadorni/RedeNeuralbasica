import numpy as np

entradas = np.array([[0,0],[0,1],[1,0],[1,1]])
saidas = np.array([0,0,0,1])
saidas = np.array([0,1,1,1])

pesos = np.array([0.0,0.0])
taxaAprendizagem = 0.1 

def stepfunction(sum):
    if sum >= 1:
        return 1
    else:
        return 0


def calculoSaida(registro):
    s = registro.dot(pesos)
    return stepfunction(s)

def treinar():
    erroTotal = 1
    while(erroTotal != 0):
        erroTotal=0
        for i in range(len(saidas)):
            saidaCalculada= calculoSaida(np.asarray(entradas[i]))
            erro = saidas[i] - saidaCalculada
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j]+(taxaAprendizagem*entradas[i][j]*erro)
                print(f'Pesos Atualizados:{str(pesos)}')
            print(f'Total de erros:{str(erroTotal)}')   
        print('Rede Neural treinada!')    
            

treinar()
print(calculoSaida(entradas[0]))
print(calculoSaida(entradas[1]))
print(calculoSaida(entradas[2]))
print(calculoSaida(entradas[3]))