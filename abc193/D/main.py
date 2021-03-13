import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def calc_point(a_lis, b_lis):
	ap = 0
	bp = 0
	for i in range(9):
		ap += (i+1) * pow(10, a_lis[i])
		bp += (i+1) * pow(10, b_lis[i])
	return (ap, bp)

def main():
	k = I()
	a = S()
	b = S()
	cnt = 0
	cnt_all = 0
	a_lis = [0] * 9
	b_lis = [0] * 9
	for i in range(4):
		a_lis[int(a[i])-1] += 1
		b_lis[int(b[i])-1] += 1
	for i in range(9):
		a_lis[i] += 1
		for j in range(9):
			b_lis[j] += 1
			if a_lis[i] <= k and b_lis[j] <= k:
				ap, bp = calc_point(a_lis, b_lis)
				cnt_all += (k - a_lis[i] + 1) * (k - b_lis[i] + 1)
				if ap > bp or (ap == bp and i > j):
					cnt += (k - a_lis[i] + 1) * (k - b_lis[i] + 1)
			b_lis[j] -= 1
		a_lis[i] -= 1
	print(cnt/cnt_all)
		

if __name__ == "__main__":
	main()