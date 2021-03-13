import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	s = S()
	for i in range(len(s)):
		if not i%2==0 and s[i].islower():
			print('No')
			exit()
		elif not i%2==1 and s[i].isupper():
			print('No')
			exit()
	print("Yes")

if __name__ == "__main__":
	main()