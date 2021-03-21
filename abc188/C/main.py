import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n = I()
	a = LI()
	first = a[:int(2**n/2)]
	second = a[int(2**n/2):]
	winf = max(first)
	wins = max(second)
	ans = winf if winf < wins else wins
	print(a.index(ans)+1)

if __name__ == "__main__":
	main()