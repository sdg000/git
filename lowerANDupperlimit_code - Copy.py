'''
1.Write a script to take in a lower limit and an upper limit.
And based on the users selection, provide all the even or odd
numbers within that range.

2.enter a new range:  then display odd or even values following that.
if not , then exit.
'''


#SECOND EDIT BEING COMMITED

LowerL=input('enter a lower limit:  ')

UpperL=input('enter upper limit:  ')

RangeOption=raw_input('do you prefer your range odd or even ?   ODD/EVEN ')


if LowerL%2!=0 and RangeOption=='ODD':
    print range(LowerL,UpperL,2)

elif LowerL%2==0 and RangeOption=='ODD':
    print range(LowerL+1,UpperL,2)

elif LowerL%2==0 and RangeOption=='EVEN':
    print range(LowerL,UpperL,2)

elif LowerL%2!=0 and RangeOption=='EVEN':
    print range(LowerL+1,UpperL,2)

else:
    print('your ranges are stupid')


RESTART =raw_input('wanna go again ?   YES/NO ')

if RESTART=='YES':
    print('I would have to call something to make the whole process start again. AM TOO TIRED')

elif RESTART=='NO':
    exit()

else:
    print('your ranges are stupid')




    
