if __name__ == "__main__":
    with open('rosalind_ini5.txt','r') as input_file:
        filing = input_file.readlines()

    for x in range(len(filing)):
        if x % 2 == 1:
            print(filing[x].strip())
