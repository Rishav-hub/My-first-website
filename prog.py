list=[]
N, K = map(int ,input().split()) #will split both input in same line
for i in range(0,N):
    ip=int(input())
    list.append(ip)

list.sort()
list5=list[K:]
print(list)
print(list5)
print(sum(list5))
