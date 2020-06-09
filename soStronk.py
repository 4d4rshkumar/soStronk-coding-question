'''----------------------ALGORITHM-------------------------------------
1. Take input from user for number of players in a team
2. Define an empty list
3. Use while loop for data till it encounters "" i.e user inputs nothing
        take input from user for name and score
        append in the defined list
4. Check if no. of data is more then or equal to number of players in team or length is 3
    if this happens match-making is not possible
5. Pass the players, array of name and score and length of array in subset function
    this function chooses the unique subsets if length given in players

    this function works as converting numbers from 1- (2 raise to power length of array )-1 to binary
    then wherever it finds sum of 1's in binary equals to players in team it appends to a binop list
6. A new dictionary is created and name of persons in team and their average score is stored, score is the
    key in dictionary.
7. then function returns the processed data
8.  All the keys are taken and sorted
9. From sorted keys middle 2 keys are taken and shown output and then removed from the list
10. this process is repeated till the list is empty

'''
def subset(m,lst,l):
    '''------------------------finding the subsets---------------------------'''
    # with the help of binary numbers for numbers of players in each side

    binop = []  # stores binary number which satisfies the condition
    # i.e no. of players in each side
    for i in range(1, (2 ** l) - 1):
        bnum = bin(i).replace("0b", '')
        acc = 0
        for k in bnum:
            if k == '1':
                acc += 1
        if (acc == m):
            binop.append(bnum.zfill(l))
    dic = {}  # stores score as a 'key' and team names as a 'value'
    for i in binop:
        acc = 0
        name = ''  # stores the name of whole team
        score = 0  # stores the score of whole team
        for j in i:
            if (j == '1'):
                name += lst[acc][0] + ','
                score += round(int(lst[acc][1]) / m, 2)  # computing average
            acc += 1
        dic[name[:-1]] = score
    return dic





players = int(input())  # number of players in each side
arr= []

'''--------taking input from console till blank line is entered------'''

while True:
    data = input()
    if data == "":
        break
    else:
        arr.append(list(data.split()))
length = len(arr)

'''------------------------if m equals no of players-------------------'''

if (length <= players or (players==2 and length==3) or length==3 and length%2==0):
    print("Match is not possible")
    exit()
required_data=subset(players,arr,length)
'''--------------------printing the quality of matches--------------------'''
avg_scores=[]
for i in required_data:
    avg_scores.append(required_data[i])
avg_scores.sort()



def get_key(val):
    for key, value in required_data.items():
         if val == value:
             return key


while len(avg_scores) != 0:
    tmp = (len(avg_scores) / 2) - 1
    a = avg_scores[int(tmp)]
    b = avg_scores[int(tmp + 1)]
    avg_scores.remove(a)
    avg_scores.remove(b)
    try:
        print(get_key(a), "(", a, ") vs ",end='')
        check=get_key(a).split(',')
        required_data.pop(get_key(a))
        name=''
        score=''
        removed={}
        '''---------------------to check same player does not encounter himself in opposition------------------'''
        for i in check:
            to_ck=get_key(b)
            if i in to_ck:
                removed[to_ck]=b
                required_data.pop(get_key(b))

        print(get_key(b), '(', b, ')')
        required_data.pop(get_key(b))
        for i in removed:
            required_data[i]=removed[i]
    except:
        print("MATCH NOT POSSIBLE!")
