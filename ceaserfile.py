#ceaser cipher
#encription code: e(x)=(x+n)mod26
#decription code: d(x)=(x-n)mod26

string=input("Enter the message which u want to enter \n")
file=open("cipherinput.txt","w")

file.write(string)
#file writng is completed

small_alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
	      'n','o','p','q','r','s','t','u','v','w','x','y','z']
big_alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
	    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

key=int(input("Enter the key (1-26)\n"))
cipher=""
plain=""
#ciphertext starts as empty string

for i in string:
    if i in big_alph:
        cipher += big_alph[(big_alph.index(i) + key) % len(big_alph)]
    elif i in small_alph:
        cipher += small_alph[(small_alph.index(i) + key) % len(small_alph)]
    else:
        cipher += i
for i in cipher:
    if i in big_alph:
        plain += big_alph[(big_alph.index(i) - key) % len(big_alph)]
    elif i in small_alph:
        plain += small_alph[(small_alph.index(i) - key) % len(small_alph)]
    else:
        plain+=i
print("cipher text:",cipher)
file.write("cryptograohic")
file.write(cipher)
print("Plain text:",plain)

file.write("plain")
file.write(plain)
    # Determine character index, add shift, wrap, 
		# determine new character
		# For capital letters

input("press enter to exit")    
file.close
