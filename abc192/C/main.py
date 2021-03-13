import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def swap(s, i, j):
	return (s[:i] + s[j] + s[i+1:j] + s[i] +s[j+1:])

def calc(n):
	big = n
	small = n
	for i in range(len(n)):
		for j in range(i, len(n)):
			if ord(big[i]) < ord(big[j]):
				big = swap(big, i, j)
			if ord(small[i]) > ord(small[j]):
				tmp = small[i]
				tmp2 = small[j]
				small = swap(small, i, j)
	return (str(int(big) - int(small)))

def main():
	x, a = LS()
	for i in range(int(a)):
		x = calc(x)
	print(x)

if __name__ == "__main__":
	main()