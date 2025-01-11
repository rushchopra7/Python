if __name__ == '__main__':
    with open('rosalind_subs.txt', 'r') as input_file:
        first_strand = input_file.readline().strip()
        second_strand = input_file.readline().strip()
    strand = []

    for base in range(len(first_strand) - len(second_strand) + 1):
        if first_strand.startswith(second_strand, base):
            strand.append(base + 1)
    print(" ".join(map(str, strand)))
