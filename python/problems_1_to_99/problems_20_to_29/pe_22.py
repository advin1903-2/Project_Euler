import csv

def pontuation_letter(letter):
    value=ord(letter)-64
    return value

def pontuation_string(string):
    count=0
    for letter in string:
        count=count+pontuation_letter(letter)
    return count

names_list=[]

with open("pe_data_22.txt") as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    data_read = [row for row in reader]
    names_list= data_read[0]
    del reader
    del data_read

names_list.sort()
total=0

for i in range(len(names_list)):
    name=names_list[i]
    value_name=pontuation_string(name)*(i+1)
    total=total+value_name

print(total)