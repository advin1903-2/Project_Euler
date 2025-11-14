def return_number_of_letters_units(n):
    if n==1:
        return 3
    elif n==2:
        return 3
    elif n==3:
        return 5
    elif n==4:
        return 4
    elif n==5:
        return 4
    elif n==6:
        return 3
    elif n==7:
        return 5
    elif n==8:
        return 5
    elif n==9:
        return 4
    elif n==0:
        return 0
    
def return_number_of_letters_regular_decs(n):
    if n==2:
        return 6
    elif n==3:
        return 6
    elif n==4:
        return 5
    elif n==5:
        return 5
    elif n==6:
        return 5
    elif n==7:
        return 7
    elif n==8:
        return 6
    elif n==9:
        return 6

def return_number_of_letters_special_decs(n):
    if n==11:
        return 6
    elif n==12:
        return 6
    elif n==13:
        return 8
    elif n==14:
        return 7
    elif n==15:
        return 7
    elif n==16:
        return 7
    elif n==17:
        return 9
    elif n==18:
        return 9
    elif n==19:
        return 8
    elif n==10:
        return 3
    

count=11
helper=0

for number in range(1,1000):
    helper=number
    if helper//100!=0:
        count=count+return_number_of_letters_units(helper//100)+7
        helper=helper%100
        if helper!=0:
            count=count+3
            if helper>19:
                count=count+return_number_of_letters_regular_decs(helper//10)
                count=count+return_number_of_letters_units(helper%10)
            elif helper<10:
                count=count+return_number_of_letters_units(helper%10)
            else:
                count=count+return_number_of_letters_special_decs(helper)
    
    elif helper!=0:
        if helper>19:
            count=count+return_number_of_letters_regular_decs(helper//10)
            count=count+return_number_of_letters_units(helper%10)
        elif helper<10:
            count=count+return_number_of_letters_units(helper%10)
        else:
            print(helper)
            count=count+return_number_of_letters_special_decs(helper)

print(count)
