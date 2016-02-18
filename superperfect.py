#kaprekar number 6147
#3435 digit to digit invariant
#http://www.naturalnumbers.org/composites.html
#6 is a perfect number which is a sum of prime factors and 1, it's probably unique because most numbers are composed of #relatively smaller prime factors so the sum and the number diverges, what is the pattern of the differences?
#

class primefactorsumsequence(object):
    def __init__(self, compositefile):
        self.compositefile = compositefile
        self.pfdict = {}
        self.outputseqfile = open('outputseqfile.txt','w')
        compositef = open(compositefile, 'r')
        # read and write to new file
        for line in compositef:
            