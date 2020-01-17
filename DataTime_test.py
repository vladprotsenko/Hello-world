import datetime

year, month, day = (int(i) for i in input().split())
#with open('input.txt', 'r', encoding='utf-8 -sig' ) as fin:
#    z = fin.readline().split()
#    year = int(z[0])
#    month = int(z[1])
#    day = int(z[2])
#    deltan = int(fin.readline())
deltan = int(input())
data = datetime.date(year, month, day)
delta = datetime.timedelta(deltan)
rez_data = data + delta

print(int(rez_data.year), end=' ')
print(int(rez_data.month), end=' ')
print(int(rez_data.day))

#test change

print("hello GIT!")
#git remote add origin https://github.com/vladprotsenko/Hello-world.git
#git push -u origin master