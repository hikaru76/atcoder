import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	s = S()
	flag = 0
	tmp = s[0]
	for i in s:
		if i != tmp:
			flag = 1
	if flag:
		print('Lost')
	else:
		print('Won')

if __name__ == "__main__":
	main()