def checking_card(number:str):
    number=list(reversed(number))

    for i in range(len(number)):
        if i%2==1:
            if  int(number[i])*2 >=10:
                two_numbers=list(str(int(number[i])*2))
                number[i]= int(two_numbers[0])+int(two_numbers[1])
            else: number[i]=int(number[i])*2
    s=0
    for i in range(1,len(number)): s+=int(number[i])
    c=10-((s%10)%10)
    if str(c)==number[0]: return True
    return False

if __name__=="__main__":
    print(checking_card("2358"))
