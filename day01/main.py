import os

def main():
    num_list = []
    # loop through lines of input.txt
    with open('input.txt') as file:
        for line in file.readlines():
            num = []
            for char in line:
                if char.isnumeric():
                    num.append(char)
            # grab first and last integer of each string, in that order, ignoring letters
            # combine them to form a two digit number
            # if there is only one integer in the string, repeat it to create the two digit number
            num_list.append(f'{num[0]}{num[len(num)-1]}')
    # return the sum of all the two digit integers
    print(sum(map(int, num_list)))

if __name__ == '__main__':
    main()