import math

def are_complementar(a, b):
    n = a+b
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return 0

    return 1

def f(T, N):
    is_complementar = [0 for _ in range(N*N)]
    for i in range(N):
        for j in range(N):
            if is_complementar[i*N+j]==0:
                for a in range(N):
                    for b in range(N):
                            if are_complementar(T[i][j], T[a][b])==1 and (i!=a or j!=b):
                                is_complementar[i*N+j]=is_complementar[a*N+b] = 1

    for i in range(N*N):
        if is_complementar[i]==0:
            T[i//N][i%N] = 0

    return T



N=3
T = [[1, 1, 1],
     [1, 1, 17],
     [1, 1, 1]]

print(f(T, N))

