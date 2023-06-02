def checking_card(number:str):
    number=number[::-1]
    for i in range(len(number)):
        if i%2==1:
            if  int(number[i])*2 >=10:
                number[i]=str(int(number[i])*2)[0]+str(int(number[i])*2)[1]
            # else: number[i]=int(number[i])*2

    print(number)

if __name__=="__main__":
    checking_card('1294')
