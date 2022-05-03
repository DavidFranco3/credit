def isvalid(n):
    t=0
    for x,y in enumerate(reversed(n)):
        y=int(y)
        if x%2==1:
            y=y*2
            if y>=10:
                t+=y//10+y%10
            else:
                t+=y
        else:
            t+=y
    return t%10==0

def cardtype(n):
    a=int(n[0]);b=int(n[0:2])
    if b>49 and b<56:return '**MASTERCARD'
    if b==34 or b==37:return '**AMEX'
    if a==4: return '**VISA'
    return 'NONE--'

NC="5465407274645021"

while NC!='0':
    NC=input("Enter credit card#:")
    if isvalid(NC)==True:
        print(cardtype(NC))
    else:
        print("INVALID...")