if __name__ =='__main__':
    with open('rosalind_ini3.txt','r') as input_file:

        string = input_file.readline().strip()
        numbers = input_file.readline().strip()
        no1, no2, no3, no4 = map(int,numbers.split())

    string1 = string[no1:no2 + 1]
    string2 = string[no3:no4 + 1]
    resulting_string = f"{string1} {string2}"

print(resulting_string)
