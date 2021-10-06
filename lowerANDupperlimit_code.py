#Write a script to take in a lower limit and an upper limit.
#And based on the users selection, provide all the even or odd
#numbers within that range.


#enter a new range:  then display odd or even values following that.

#if not , then exit.

'''
VARIABLES TO DECLARE
LowerL
UpperL
odd_range
even_range
'''

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
    print('I would have to call something to make the whole process start again')

if RESTART=='NO':
    print('Thank you for making my job easier...off to play')

exit()


    

'''
choice=raw_input('do you want odd or even range btn ur limits ? ' )

if choice=='odd':
    print(odd_range())

elif choice=='even':
    print(even_range())




# 1 if start is odd (n%2!=0),  then step by 2 regardless of END VALUE. to get ODD range

# 3 if start is even (n%2=0), then step by 2 regardless of END VALUE. to get EVEN range

# 4 if start is odd, increase by one and step by 2 to get EVEN RANGES

# 2 if start is even, increase by one and step by 2 to get ODD RANGES




#even number display

for i in lower_limit:
    print(lower_limit,+1)

#if lower_limit%2==0:
    

"""
llimit
ulimit
oddrange
evenrange

newrange
newllmit
newulimit
noodrange
nevenrange



def even_range():
    return range(LowerL,UpperL,2)

def odd_range():
    return range(LowerL,UpperL,3)

'''
