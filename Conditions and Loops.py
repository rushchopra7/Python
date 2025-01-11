if __name__ == '__main__':
    with open('rosalind_ini4.txt','r') as input_file:
        numbers = input_file.readline().strip()
        a,b = map(int,numbers.split())
    sum_odd = 0
    if a<b:
        for nums in range(a,b+1):
            if nums % 2 == 1:
                sum_odd += nums

    print(f"The sum of odd positive integers between {a} and {b} is: {sum_odd}")

