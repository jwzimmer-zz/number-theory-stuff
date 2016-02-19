#kaprekar constant 6174 kaprekar routine
#
    #From wikipedia:
    #Take any four-digit number, using at least two different digits. (Leading zeros are allowed.)
    #Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros       #if necessary.
    #Subtract the smaller number from the bigger number.
    #Go back to step 2.

#followed PEP8 more in this file

def kaprekar_routine(n, iterations=0):
    """Takes a positive integer n and returns how many iterations
    it took to get to 6174 (Kaprekar's constant)
    Input should be 4 or fewer digits and not a repdigit"""
    if n == 6174:
        return iterations
    else:
        strn = str(n)
        if len(strn) < 4:
            num0 = 4 - len(strn)
            str0 = "0"*num0
            strn = str0 + strn
        else:
            pass
        nlist = [int(x) for x in strn]
        #from small to large digits
        nlist.sort()
        #from large to small digits
        reversedlist = list(reversed(nlist))
        largen = ""
        for x in reversedlist:
            largen += str(x)
        largen = int(largen)
        smalln = ""
        for x in nlist:
            smalln += str(x)
        smalln = int(smalln)
        newn = largen - smalln
        iterations += 1
        #print n, newn, largen, smalln, iterations
        return kaprekar_routine(newn, iterations)

def main():
    print kaprekar_routine(124)
    
if __name__ == '__main__':
    main()
