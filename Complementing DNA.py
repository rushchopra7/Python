if __name__ == "__main__":
    with open('rosalind_revc.txt','r') as input_file:
        strand = input_file.read().strip().upper()

    complement = {"A": "T", "C": "G", "G": "C", "T": "A"}
    reversed_strand = []
    for bases in reversed(strand):
        reversed_strand.append(complement[bases])

    print(''.join(reversed_strand))
