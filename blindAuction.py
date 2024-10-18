hilu='''               _   _             
                 | | (_)            
  __ _ _   _  ___| |_ _  ___  _ __  
 / _` | | | |/ __| __| |/ _ \| '_ \ 
| (_| | |_| | (__| |_| | (_) | | | |
 \__,_|\__,_|\___|\__|_|\___/|_| |_|
                                    
'''
print(hilu)
hi=0
name=""
d=True
papa={}
while d:
    A=input("What is your name?: ")
    B=int(input("What is your bid ? Rs. "))
    C=input("Are there any other bidders? ")
    if C=='yes':
        d=True
    else:
        d=False
    papa[A]=B
    print('\n'*100)
for i in papa:
    if papa[i]>hi:
        hi=papa[i]
        name=i
print( "the winner is",name,"with bid value:",hi)
        
