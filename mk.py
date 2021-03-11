import sys
import os

directoryname = sys.argv[1]
problemname = '@'
os.mkdir(directoryname)
for _ in range(6):
	problemname = chr(ord(problemname) + 1)
	os.mkdir(directoryname + '/' + problemname)
	f = open(directoryname + '/' + problemname + '/main.py', 'w')
	f.write('import bisect,collections,copy,heapq,itertools,math,numpy,string\n\
import sys\ndef I(): return int(sys.stdin.readline().rstrip())\n\
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))\n\
def S(): return sys.stdin.readline().rstrip()\n\
def LS(): return list(sys.stdin.readline().rstrip().split())\n\
\n\
\n\
\n\
def main():\n\
	\n\n\
if __name__ == "__main__"\n\
	main()')
	f.close