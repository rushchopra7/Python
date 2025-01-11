if __name__ == '__main__':
    with open('rosalind_dna (2).txt','r') as input_file:
        file_counter = input_file.readline().strip()

    DNA_dictionary = {"A": 0, "C": 0, "G": 0, "T": 0}
    for base in file_counter:
        DNA_dictionary[base] += 1

    print(' '.join([str(value) for key, value in DNA_dictionary.items()]))

