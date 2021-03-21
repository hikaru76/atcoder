import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())



def main():
	n = S()
	if len(n) == 1:
		print(0)
	else:
		flag = 0
		if len(n) % 2 == 1:
			flag = 1
		ans = 0
		for i in range(int((len(n) - flag)/2)-1):
			ans += 9 * 10 ** i
		if flag:
			n = str(10 ** int(len(n)-1)-1)
		a = int(n[:int(len(n)/2)])
		b = int(n[int(len(n)/2):])
		ans += a - 10 ** (int(len(n)/2)-1) + 1
		if b < a:
			ans -= 1
		print(ans)

if __name__ == "__main__":
	main()