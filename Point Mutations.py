if __name__ == "__main__":
    with open('rosalind_hamm.txt','r') as input_file:
        first_strand = input_file.readline().strip()
        second_strand = input_file.readline().strip()
    dist = 0
    for base in range(len(first_strand)):
        if first_strand[base] != second_strand[base]:
            dist += 1
    print(dist)
