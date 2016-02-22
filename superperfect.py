#mills constant theta^3^n generates primes
#3435 digit to digit invariant
#Note the lists of prime factorizations for composite numbers came from http://www.naturalnumbers.org/composites.html
#6 is a perfect number which is a sum of prime factors and 1, it's probably unique because most numbers are composed of #relatively smaller prime factors so the sum and the number diverges, what is the pattern of the differences?
#
#
import re

class primefactorsumsequence(object):
    def __init__(self, compositefile):
        self.compositefile = compositefile
        self.pfdict = {}
        self.outputCompositeFileName = 'outputseqfileComposite.txt'
        self.explainerComposite = "These are the positive composite integers (0 and 1 not being prime or composite) up\                         to n\n\
                        and the difference between n and the sum of n's prime factors\n\
                        *1 is not included as a factor, even though it is included for perfect numbers\n\
                        *The factors are summed individually, not as powers...\n\
                        meaning that if n=25, the sum is 5 + 5 = 10, not 5^2 = 25\n\n\
                        === Every line has the format ===\n\
                        n --> n - sum(n's prime factors)\n"
        compositef = open(compositefile, 'r')
        # read and write to new file
        for line in compositef:
            # will match numbers followed by a word boundary 
            pattern = re.compile(r'\d+\b')
            matches = re.findall(pattern, line)
            if len(matches) > 1:
                self.pfdict[int(matches[0])] = sum([int(x) for x in matches[1:]])
                #print self.pfdict[matches[0]], matches[0], matches
            else:
                pass
                #print matches
                
    def addPrimes(self):
        """adding the prime numbers to a dict"""
        self.outputPrimeFileName = 'outputseqfilePrimes.txt'
        primesdict = {}
        self.primesdict = primesdict
        explainer = "These are the positive integers from 2 to n\n\
                        and the difference between n and the sum of n's prime factors\n\
                        *1 is not included as a factor, even though it is included for perfect numbers\n\
                        *The factors are summed individually, not as powers...\n\
                        meaning that if n=25, the sum is 5 + 5 = 10, not 5^2 = 25\n\n\
                        === Every line has the format ===\n\
                        n --> n - sum(n's prime factors)\n"
        self.explainerPrimes = explainer
        maxComp = max(self.pfdict.keys())
        for i in xrange(2, maxComp+1):
            if self.pfdict.has_key(i):
                self.primesdict[i] = self.pfdict[i]
            else:
                self.primesdict[i]=i
            #print i, self.primesdict[i]
        return self.primesdict, self.explainerPrimes, self.outputPrimeFileName
        
    def add1Factor(self):
        """adding 1 to a dict since 1 is included in factors for perfect numbers"""
        self.output1FileName = 'outputseqfile1.txt'
        dict1 = {}
        self.dict1 = dict1
        explainer = "These are the positive integers from 2 to n\n\
                        and the difference between n and the sum of n's prime factors\n\
                        *1 is included as a factor, because it is included for perfect numbers\n\
                        *The factors are summed individually, not as powers...\n\
                        meaning that if n=25, the sum is 5 + 5 = 10, not 5^2 = 25\n\n\
                        === Every line has the format ===\n\
                        n --> n - sum(n's prime factors)\n"
        self.explainer1 = explainer
        maxComp = max(self.pfdict.keys())
        for i in xrange(2, maxComp+1):
            if self.pfdict.has_key(i):
                self.dict1[i] = self.pfdict[i]+1
            else:
                self.dict1[i]=i+1
            #print i, self.primesdict[i]
        return self.dict1, self.explainer1, self.output1FileName
        
    def powerSum(self):
        #make sequence of diffs with factors to the power e.g. + 5^2 = 25 instead of + 5 + 5 = 10
        pass
    
    def writeOutputFile(self, someDict, explainer, filename):
        outputseqfile = open(filename, 'w')
        outputseqfile.write(explainer)
        for i in sorted(someDict.keys()):
            newline = str(i) + " --> " + str(i - someDict[i]) + "\n"
            outputseqfile.write(newline)
        return None
    
    def writeAllOutputFiles(self):
        self.writeOutputFile(self.pfdict, self.explainerComposite, self.outputCompositeFileName)
        a,b,c = self.addPrimes()
        self.writeOutputFile(a, b, c)
        a,b,c = self.add1Factor()
        self.writeOutputFile(a, b, c)
        #add seq powerSum      
            
def main():
    pfss = primefactorsumsequence('compositesto133.txt')
    pfss.writeAllOutputFiles()

if __name__ == '__main__':
    main()
            