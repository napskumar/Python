#data = "Hi, How are you?"
#print (data)
print("************** Find Number of Vowels,Consonants,Uppercases & Lowercases ****************\n")
data = input("Enter a String :")
uppercase=0
lowercase=0
vowels=0
consonants=0

for chval in data:
    if str.isupper(chval):
        uppercase+=1
    elif str.islower(chval):
        lowercase+=1

    ch=str.lower(chval)

    if ch in "aeiou":
        vowels+=1
    elif ch in "bcdfghjklmnpqrstvwxyz":
        consonants+=1


print("\n\n")
print("*" * 20)
print("UPPERCASE  :",uppercase)
print("LOWERCASE  :",lowercase)
print("VOWELS     :",vowels)
print("CONSONANTS :",consonants)
print("Total Char :",len(data))
print("*" * 20)