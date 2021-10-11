def printAllKLength(a, l):

	n = len(a)
	b = ""
	printAllKLengthRec(a, b, n, l)

def printAllKLengthRec(set, b, n, l):
	if (l == 0) :
		print(b)
		return
	for i in range(n):
		c = b + set[i]
		printAllKLengthRec(set, c, n, l - 1)



string = input('Enter string of length three: ')

if (len(string) != 3):
    print("Error ! Enter String of Length Three")
else:
    
    a = list(str(string))
    l = len(a)
    printAllKLength(a, l)
