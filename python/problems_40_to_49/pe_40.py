def num_of_steps(n:int):
    ret = 0
    while(n>0):
        ret=ret+1
        n=n//10

    return ret

def get_digit(char_num,number):
    value = int(number // (10**char_num))%10
    return value


def get_digit_nth_digit(n:int):
    n_i=0
    n_i_step=0
    number=0
    while(n_i<n):
        number=number+1
        n_i_step = num_of_steps(number)
        n_i = n_i + n_i_step

    char_num = n_i-n

    ret = get_digit(char_num,number)

    return ret

mult=1
nk=1
for i in range(7):
    mult = mult * get_digit_nth_digit(nk)
    nk=nk*10
print(mult)