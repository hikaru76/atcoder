import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	a,b,c = LI()
	if a > b:
		print('Takahashi')
	elif b > a:
		print('Aoki')
	elif c == 0:
		print('Aoki')
	else:
		print('Takahashi')

if __name__ == "__main__":
	main()