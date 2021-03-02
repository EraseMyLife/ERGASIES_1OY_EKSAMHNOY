import random

#Ζητάω τη πλευρά από το χρήστη
print("Δώσε την ακέραια πλευρά του τετραγώνου: ")
x = int(input(" "))
while (x < 4):
    print("Η πλευρά πρέπει να είναι ακέραιος θετικός αριθμός, μεγαλύτερος του 3!")
    x = int(input(" "))

#Βρίσκω το πλήθος των μισών θέσεων
if ((x**2)%2!=0):
    half = round((x**2)/2)+1
else:
    half = round((x**2)/2)

SumOfOnes = 0
#Γεμίζω τις μισές θέσεις με 0 και τις άλλες μισές με 1
for times in range(100):
	table = []
    #Μετράω το πλήθος των 1 και 0
	sum1 = 0
	sum0 = 0

	for i in range(x):
		lista = []
		for j in range(x):
			numb = random.randint(0,1)
			if (numb == 1 and sum1 < half):
				lista.append(numb)
				sum1 = sum1 + 1
			elif (numb == 0 and sum0 < ((x**2)-half)):
				lista.append(numb)
				sum0 = sum0 + 1
			elif (sum1 == half):
				lista.append(0)
			elif (sum0 == ((x**2)-half)):
				lista.append(1)
			
		table.append(lista)

	for w in range(x):
		print(table[w], sep="\n")

	#Ψάχνω να βρω τις 4άδες
	orizontia = 0
	katheta = 0
	diagwnia = 0
  
	for i in range(x):
		for j in range(x-3):
			if (table[i][j]==1 and table[i][j+1]==1 and table[i][j+2]==1 and table[i][j+3]==1):
				orizontia = orizontia + 1

	for j in range(x):
		for i in range(x-3):
			if (table[i][j]==1 and table[i+1][j]==1 and table[i+2][j]==1 and table[i+3][j]==1):
				katheta = katheta + 1

	for i in range(x-3):
		for j in range(x-3):
			if (table[i][j]==1 and table[i+1][j+1]==1 and table[i+2][j+2]==1 and table[i+3][j+3]==1):
				diagwnia = diagwnia + 1

	for j in range(x-1,2,-1):
		for i in range(x-3):
			if (table[i][j]==1 and table[i+1][j-1]==1 and table[i+2][j-2]==1 and table[i+3][j-3]==1):
				diagwnia = diagwnia + 1

	SumOfOnes = SumOfOnes + orizontia + katheta + diagwnia

MO = SumOfOnes / 100
print("Ο Μέσος Όρος των 4άδων είναι: ", MO)
