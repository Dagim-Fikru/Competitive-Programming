class Solution:
    def numberOfMatches(self, n: int) -> int:
        numOfMatches = 0
        while n>1:
            if n%2==0:
                numOfMatches+= n//2
                n = n//2
            else:
                numOfMatches+= n//2
                n = (n//2) + 1
        return numOfMatches
