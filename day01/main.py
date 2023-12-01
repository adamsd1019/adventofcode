def main():
    num_list = []
    numchar = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    # loop through lines of input.txt
    with open('input.txt') as file:
        for line in file.readlines():
            num = []
            # extract all spelled out numbers and their ending index
            for nc in numchar:
                if numchar[nc] in line:
                    if line.count(numchar[nc]) == 1:
                        num.append({'number': nc,
                                    'index': line.find(numchar[nc]) + (len(numchar[nc])-1)})
                    else:
                        found = 0
                        for i in range(0, line.count(numchar[nc])):
                            if found == 0:
                                num.append({'number': nc,
                                            'index': line.find(numchar[nc]) + (len(numchar[nc])-1)})
                                found += len(numchar[nc])
                            else:
                                num.append({'number': nc,
                                            'index': line.find(numchar[nc], found) + len(numchar[nc])-1})
                                found += len(numchar[nc])
            # extract all numbers and their index
            i = 0
            for char in line:
                if char.isnumeric():
                    num.append({'number': char,
                                'index': i})
                i += 1
            # order dict list by index value
            nums_ordered = []
            for i in num:
                nums_ordered.append(i['index'])
            # sort indices and make new number value list
            values = []
            for n in sorted(nums_ordered):
                for x in num:
                    if x['index'] == n:
                        values.append(x['number'])

            num_list.append(f'{values[0]}{values[len(num)-1]}')

            # grab first and last integer of each string, in that order, ignoring letters
            # combine them to form a two digit number
            # if there is only one integer in the string, repeat it to create the two digit number
 
    file.close()
    # return the sum of all the two digit integers
    print(sum(map(int, num_list)))

if __name__ == '__main__':
    main()