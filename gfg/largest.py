# largest number in one swap
class Solution:
    def largestSwap(self, num):
        s = list(str(num))
        n = len(s)
        
        suff_max = n - 1
        swap_a = swap_b = -1
        
        for i in range(n - 2, -1, -1):
            if s[i] > s[suff_max]:
                suff_max = i
            elif s[i] < s[suff_max]:
                swap_a = i
                swap_b = suff_max
        
        if swap_a != -1:
            s[swap_a], s[swap_b] = s[swap_b], s[swap_a]
        
        return ''.join(s) 