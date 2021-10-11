import ipaddress

#Read the input file 
f = open("ipaddress.txt", "r")
print(f.read())

#convert decimal to integer

def binaryToDecimal(n):
	return int(n,2)


print(binaryToDecimal("11111111"))
print(binaryToDecimal("10101010"))
print(binaryToDecimal("01010101"))
print(binaryToDecimal("11001100"))

# print(binaryToDecimal(f))

