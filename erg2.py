import random
print("Δώσε τον ακέραιο όρο την ακολουθίας Fibonacci: ")
n = int(input(" "))
while n < 0:
    print("Ο όρος πρέπει να είναι θετικός αριθμός !")
    n = int(input(" "))
n1=1
n2=1
if (n<=2):
    print("Ο ", n,"ος όρος δεν είναι πρώτος.")
else:
    #Θα υπολογίσω την τιμή του όρου n της ακολουθίας.
    for i in range(n-2):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    #Και τώρα θα ελέγξω αν είναι πρώτος.
    j=0
    for i in range(20):
        k = random.randint(0,10000000000)
        if (( k ** n3 ) % n3 == (k % n3 )):
            j= j + 1
        else:
            print("Ο ", n,"ος όρος δεν είναι πρώτος.")
            break
    if (j==20):
        print("Ο", n,"ος όρος είναι πρώτος.")
   



