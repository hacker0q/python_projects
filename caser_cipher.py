alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
B=input("do you want to encrypt or decrypt the code ")
text=input("enter the orignal text ").lower()
shift_amount=int(input("enter the shift amount "))
def encrypt(orignal_text,shift):
    display=""
    for letter in orignal_text:
        if letter ==" " :
            display+=" "
        else :
            A=alphabet.index(letter)
            A+=shift
            if A > 25 :
                A-=26
            display+=alphabet[A] 
    print(display)
def decrypt(orignal_text,shift):
    display=""
    for letter in orignal_text:
        if letter==" ":
           display+=" "
        else :
            A=alphabet.index(letter)
            A-=shift
            if A < 0 :
                A+=26
            display+=alphabet[A]
    print(display)
if B=="encrypt":
    encrypt(orignal_text=text,shift=shift_amount)
else:
    decrypt(orignal_text=text,shift=shift_amount)



   


        



