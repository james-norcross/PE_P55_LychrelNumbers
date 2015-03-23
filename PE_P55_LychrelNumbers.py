## Author: James Norcross
## Date: 3/20/15
## Purpose: Project Euler Problem 55
## Description: Finds the count of Lychrel numbers below 10000

def isLychrelNumber(n):
    count = 0

    n_str = str(n)
    n_rev_str = n_str[-1: -(len(n_str)+1) : -1]
    n_rev = int(n_rev_str)

    while(count < 50):
        
        n = n + n_rev

        n_str = str(n)
        n_rev_str = n_str[-1: -(len(n_str)+1) : -1]
        n_rev = int(n_rev_str)
        
        if(n == n_rev):
            return False
        
        else:
            count += 1

    return True


LychrelCount = 0

for n in range(1,10000):
    if(isLychrelNumber(n)):
        LychrelCount += 1

print "The number of Lychrel numbers below 10000 is %d" % LychrelCount
    
            
            
