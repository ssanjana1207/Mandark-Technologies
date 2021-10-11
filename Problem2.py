#square matrix along row or column

n = int(input("Enter Dimension of Square Matrix: "))
arr = input("Enter first row: ") 
arr2 =input("Enter Second row: ")
l = list(map(int,arr.split(' ')))
m = list(map(int,arr2.split(' ')))
c = input("Choose row or Colunm")

matrix1 = []

matrix1.append(l)
matrix1.append(m)


if (c=="row"):
    b = matrix1[::-1]  
    print('\nMatrix after changing column order:\n')
    for rows in b:
        print(*rows, sep=", ")
else:
    
    matrix2= []
    for i in range(len(matrix1)):
        matrix2.append(matrix1[i][::-1])
    for rows in matrix2:
        print(*rows, sep=", ")
    
