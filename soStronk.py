import pytest                                           #for unit testing
m=int(input())                                          #number of players in each side
lst=[]

'''--------taking input from console till blank line is entered------'''

while True:
    data =input()
    if data =="":
        break
    else:
        lst.append(list(data.split()))
l=len(lst)


'''------------------------if m equals no of players-------------------'''

if(l<=m):
    print("Match is not possible")
    exit()

    
'''------------------------finding the subsets---------------------------'''
                                                        #with the help of binary numbers for numbers of players in each side

binop=[]                                                #stores binary number which satisfies the condition
                                                        #i.e no. of players in each side
dic={}
for i in range(1,(2**l)-1):
    bnum=bin(i).replace("0b",'')
    acc=0
    for k in bnum:
        if k=='1':
            acc+=1
    if(acc==m):
        binop.append(bnum.zfill(l))
dic={}                                                  #stores score as a 'key' and team names as a 'value'
avg_scores=[]
for i in binop:
    acc=0
    name=''                                             #stores the name of whole team
    score=0                                             #stores the score of whole team
    for j in i:
        if(j=='1'):
            name+=lst[acc][0]+','
            score+=round(int(lst[acc][1])/m,2)          #computing average
        acc+=1
    avg_scores.append(score)
    dic[score]=name[:-1]
    
'''--------------------printing the quality of matches--------------------'''
avg_scores.sort()
while len(avg_scores)!=0:
    tmp=(len(avg_scores)/2)-1
    a=avg_scores[int(tmp)]
    b=avg_scores[int(tmp+1)]
    avg_scores.remove(a)
    avg_scores.remove(b)
    print(dic[a],"(",a,") vs ",dic[b],'(',b,')')
