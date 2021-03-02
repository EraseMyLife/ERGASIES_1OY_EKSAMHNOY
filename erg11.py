import json

#Open, reads file and
file = open("dictionary.txt", "r")
openedfile = file.read()

diction = json.loads(openedfile)
file.close()

#Creating an empty (for now) sequence dictionary
sequency_dictionary = {}

#Filling the sequence dictionary
#Basically if our key's value is a dictionary we want   
#to start over and call the function again, till we
#don't have a dictionary to work with
def LookForKeys(diction):
    for keys, value in diction.items():
        if type(value) is dict:
            LookForKeys(value)
#If the key exists, increase it's sequence by 1
            if (keys in sequency_dictionary):
                sequency_dictionary[keys] += 1
#If it doesn't, set it to 1
            else:
                sequency_dictionary[keys]=1
#Same thing for these lines of code
        elif (keys in sequency_dictionary):
            sequency_dictionary[keys] += 1
        else:
            sequency_dictionary[keys]=1
        if type(value) is list:
            for i in range(len(value)):
                if type(value[i]) is dict:
                    LookForKeys(value[i])

#Calling the function
LookForKeys(diction)

#Using the anonymous function lambda and printing
#every key that has the same value as the max one
KeyValues = max(sequency_dictionary.items(), key=lambda x: x[1])
MaxKeyList = list()
for key, value in sequency_dictionary.items():
    if value == KeyValues[1]:
        MaxKeyList.append(key)
print("The keys with the max value are: ", MaxKeyList)
