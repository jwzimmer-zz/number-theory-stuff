#kaprekar constant 6174 kaprekar routine
#
    #From wikipedia:
    #Take any four-digit number, using at least two different digits. (Leading zeros are allowed.)
    #Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros       #if necessary.
    #Subtract the smaller number from the bigger number.
    #Go back to step 2.

#followed PEP8 more in this file

#helper function for kaprekar_routine function
def add_0s_front_of_n(stringn, desirednlength):
    """takes string of n, desired length of n, puts 0s in front of n
    so that n will be desired length but will not change its value as an int"""
    num0 = desirednlength - len(stringn)
    str0 = "0"*num0
    stringn = str0 + stringn
    return stringn

#helper function for kaprekar_routine function
def make_int_from_list(numberlist):
    """takes a list of digits and returns a number composed of the elements of the list"""
    newint = ""
    for x in numberlist:
        newint += str(x)
    newint = int(newint)
    return newint

def kaprekar_routine(n, iterations=0):
    """Takes a positive integer n and returns how many iterations
    it took to get to 6174 (Kaprekar's constant)
    Input should be 4 or fewer digits and not a repdigit"""
    if n == 6174:
        return iterations
    else:
        strn = str(n)
        if len(strn) < 4:
            strn = add_0s_front_of_n(strn, 4)
        else:
            pass
        nlist = [int(x) for x in strn]
        #from small to large digits
        nlist.sort()
        #from large to small digits
        reversedlist = list(reversed(nlist))
        largen = make_int_from_list(reversedlist)
        smalln = make_int_from_list(nlist)
        newn = largen - smalln
        iterations += 1
        #print n, newn, largen, smalln, iterations
        return kaprekar_routine(newn, iterations)

#what happens if you use negative numbers? do you loop at 6174 still? How would that work?
def kaprekar_routine_negative(n, iterations=0):
    """Takes a negative integer n and looks for a loop,
    or returns how many iterations
    it took to get to (-)6174 (Kaprekar's constant)
    Input should be 4 or fewer digits and not a repdigit"""
    #i think i'll need to ADD numbers not subtract them since we want the length of the number to stay 4 or under
    #i'll need to store previous numbers in order to recognize repeating loops
    #i'll need to cut off from doing infinite recursions, since it's possible there won't be any equivalent
    #to kaprekar's constant, and if there are no loops and no constant, then the function would recurse forever
    #SOME PSEUDOCODE & COPYPASTA:
    #if n == -6174: # or n is in a loop:
        #return iterations
    #else:
        #stuff
    return None

def main():
    print kaprekar_routine(124)
    
if __name__ == '__main__':
    main()
