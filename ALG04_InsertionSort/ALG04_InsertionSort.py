'''

'''

f = []
file = open("../data/rosalind_ins.txt", 'r')
f = file.read().split()
file.close()

A = [int(x) for x in f[1:]]
#A = [6, 10, 4, 5, 1, 2]

def insertionSort(A):
  currentValue = 0
  for i in range(1,len(A)):
    position = i
    while position >= 1 and A[position] < A[position - 1]:
      A[position], A[position - 1] = A[position - 1], A[position]
      currentValue += 1
      position = position - 1
  return currentValue

print(insertionSort(A))