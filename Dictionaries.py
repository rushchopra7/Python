if __name__ == "__main__":
    with open('rosalind_ini6.txt','r') as input_file:
       str = input_file.readline().strip()

    result = {}
    for word in str.split(' '):
        if word not in result:
            result[word] = 0
        result[word] += 1

    for a,b in result.items():
        print(a,b)



