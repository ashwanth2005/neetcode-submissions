class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==2:
            return n
        else:
            curr=1
            nxt=2
            for i in range(2,n):
                curr,nxt=nxt,curr+nxt
            return nxt

