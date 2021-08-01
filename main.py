import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n = I()
	a = LI()
	ans = 1000000000000
	for i in range(2**(n-1)+1,2 ** n):
		li = []
		sub = []
		for j in range(n):
			sub.append(a[j])
			if ((i >> j) & 1):
				li.append(sub)
				sub = []
		for lis in li:
			print(lis)
			xorlis = []
			if len(lis) != 1:
				tmp = bin(lis[0])
				for j in range(1,len(lis)):
					tmp = bin(int(tmp[2:]) | lis[j])
				xorlis.append(int(tmp[2:]))
			else:
				xorlis.append(lis[0])
		print(xorlis)
		tmpans = bin(xorlis[0])
		if len(xorlis) != 1:
			for j in range(1,len(xorlis)):
				tmpans = bin(int(tmpans[2:]) | xorlis[j])
		ans = min(ans, int(tmpans[2:], base=2))
	print(ans)

if __name__ == "__main__":
	main()