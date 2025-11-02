import csv

def triangle_number(n:int)->int:
        triangle_number = 1/2*(n)*(n+1)
        triangle_number = int(triangle_number)

        return triangle_number

def get_word_value(word:str)->int:
        str_size=len(word)
        sum=0
        for i in range(str_size):
                ## Sum the ascii value-64 because ascii value of A is 65
                sum = sum + (ord(word[i])-64)
        
        return sum

## In principle we will not have words with more than 45 letters in english
## So it is cool to make a list with the possible numbers up to 45*26
list=[]
val=0
n=1
while(val<45*26):
   val = triangle_number(n)
   list.append(val)
   n=n+1
del n,val

## So now, read word by word, and check if each word is or not a triangle word
triangle_words_count=0
# Open the CSV file
with open('pe_42_data.txt', 'r', newline='') as file:
    reader = csv.reader(file)
    # Loop through each row
    for row in reader:
        # Loop through each value in the row
        for value in row:
            if(get_word_value(value) in list):
                  triangle_words_count=triangle_words_count+1

print(triangle_words_count)


