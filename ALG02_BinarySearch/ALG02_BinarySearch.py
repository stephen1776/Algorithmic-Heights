'''
The problem is to find a given set of keys in a given array.

Given: Two positive integers n ≤ 105 and m ≤ 105, a sorted array A[1..n] of integers from −105 to 105
and a list of m integers −105 ≤ k1,k2,…,km ≤ 105.

Return: For each ki, output an index 1 ≤ j ≤ n s.t. A[j] = ki or "-1" if there is no such index.
'''
from bisect import bisect_left

def binarySearch(A, q, lo=0, hi=None):
    hi = hi if hi is not None else len(A)
    pos = bisect_left(A, q, lo, hi)
    return(pos + 1 if pos != hi and A[pos] == q else -1) # add 1 since Python index starts at 0



if __name__ == "__main__":
    with open('../data/rosalind_bins.txt') as f:
        n = int(f.readline().strip())
        m = int(f.readline().strip())
        A = [int(z) for z in f.readline().strip().split()]
        Q = [int(z) for z in f.readline().strip().split()]
        print(*[binarySearch(A, q) for q in Q])