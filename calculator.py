hi='''___________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
'''
print(hi)
def add(n1,n2):
    return n1+n2
def subtracrt(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
yo=True
D="n"
while yo:
    if D=="y":
        A=E
    elif D=="n":      
        A=int(input("what 's the first number"))
    B=(input("enter the operation"))
    C=int(input("enter the second number"))
    dic={"+":add,"-":subtracrt,"*":multiply,"/":divide}
    if B=="+" :
        E=(dic["+"](A,C))
        print(E)
    elif B=="-" :
        E=(dic["-"](A,C))
        print(E)
    elif B=="*" :
        E=(dic["*"](A,C))
        print(E)
    elif B=="/" :
        E=(dic["/"](A,C))
        print(E)
    D=input(f"Type 'y' to continue calculating with {E} ")
