if __name__ == "__main__":
    n = int(input('Digite um numero: '))
    x = 1/n
    for i in range(1, 101):
        x = (n+1) * x-1
    print(x)
