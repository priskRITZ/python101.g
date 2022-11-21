#22.11.21
print("Hello World!")

food = "Python's favorite food is perl"
print(food)

say = '"Python is very easy." he says.'
print(say)

food1 = "\"Python\'s favorite food is perl.\" he says."
print(food1)

multiline1 = """
Life is too short
You need python
"""
print(multiline1)

head = "Python"
tail = " is fun!"
print(head + tail)

a = "python"
print(a*2)

print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short"
len(a)

a = "Life is too short, You need Python"
len(a)

b = a[0]+a[1]+a[2]+a[3]
b
a[-6:-1]
a[-6:] #마지막 문자는 -1인데 a[-6:-1] 은 마지막이 안나오니 그냥 생략으로 하면 나옴
a[:]

a = "20010231Rainy"
date = a[:8]
weather = a[8:]
date
weather

year = a[:4]
month = a[4:6]
day = a[6:8]

year
month
day

a = "Pithon"
a[:1] + "y" + a[2:]

"I eat %d apples." % 3
"I eat %s apples." % "three"

number = 3
"I eat %d apples." % number

number = "three"
"I eat %s apples." % number

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." %(number, day)

"Error is %d%s%%." %(9,8)
"Error is %d%s%%." %(9,"O")

"%10s" % "hi"
"%-10sjane." % 'hi'
"%0.4f" % 3.42135234
"%0.3f" % 0.9999

"%10.5f" % 3.42134234

"I eat {0} apples".format(3)
"I eat {0} apples".format("five")
number = 3
"I eat {0} apples".format(number)
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number,day)

"I ate {number} apples. so I was sick for {day} days.".format(number=3, day="five")

"{0:<10}".format("hi")

"{0:>10}".format("priskRITZ")
"{0:^10}".format("hi")
"{0:!^20}".format("ALERT")
"{0:!<20}".format("wassup")

y = 3.42134234
"{0:0.4f}".format(y)
#z = "3.42134234"
#z[0:6]

"{{ and }}".format()

name="홍길동"
nameadd="전"
age=30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'

f'나는 지금 {age}살 이고 내년이면 {age+1}살이 된다.'
f"내 이름은 {name}인데, '전'을 더하면 {name + nameadd}이다."

d = {'name':'홍길동','age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

d1={'name':"홍길동",'age':30}
f'나의 이름은 {d1["name"]}입니다. 나이는 올해 {d["age"]}이고, 내년에는 {d1["age"]+1}입니다.'

f'{"hi":<10}'
f'{"hi":>10}'
f'{"hi":^10}'
f'{"alert":!^20}'

y=3.42134234
f'{y:0.4f}'
f'{y:10.4f}'
f'{y:>10.4f}'
f'{y:<10.4f}'

f'{{ and }}'

a = "hobby"
a.count('h')

a.find("h")
a.find('')

a = "Life is too short"
a.index("L")

",".join('abcd')
"-".join(a)

a.upper()
a.lower()

a.strip()

a.replace("Life", "Your leg")

p = "Pithon"
p
p.replace("i","y")

a.split()
b = "name:age:address:phone"
b.split(":")

#List

odd = [1,3,5,7,9]
odd

a = []
b = [1,2,3]
c = ['Life', 'is', 'too', 'short']
d = [1,2,'Life','is']
e = [b, c]
f = ["abc", e]
g = [1,2,3,'A','B']

g[3]+g[4]

b

b[0]
b[0]+b[1]

c = ['Life', 'is', 'too', 'short']
c[0]
c[:1]
#c[0]은 'Life' 로 출력, c[:1]은 ['Life'] 로 출력

a=[1,2,3,['a','b','c']]
a[-1][0]
a[:]

a=[1,2,3]
b=[4,5,6]
a+b

len(a)

a
#a[2]+"hi"
str(a[2])+"hi"

print(str(a[2])+"hi")

a = [1,2,3]
del a[1]
a[:]

a = [1,2,3,['a','b','c']]
del a[-1]
a
a=[1,2,3]
b=['a','b','c']
c=[4,5,6]
a
a.append(b)
del a[-1]
a.append(c)
del a[-1]
#d = list()
d
d = a+c+c

d.sort()
d

s = [3, 8, 5,['c', 'a', 'b']]
s[:3].sort()
s[3].sort()
s

k = [7,3,5,['d','c','a']]
k
k[:3].sort()
k
k[3].sort()
k

k[3].reverse()
k[:3].reverse()
k

a = [2,3,4]
a.insert(0,1)
a[-1]
len(a)
a.insert(9,6)
#list의 최대길이 이상의 길이에 숫자를 넣으면 걍 맨마지막에 넣는거
a
a.remove(6)
# .remove(x)는 배열의 몇번째를 없애는게아니라 첫번째 x 데이터를 지우는거 
a = [1,2,3]
a.pop()
a.pop(2)
a

a = [1,1,2,3,4]
a.count(1)

a.extend([4,5])
a.reverse()
a
a.remove(1)

b = [6,7]
a = [4,1,2,5,3]
a.extend(b)
a
a.sort()
a

#tuple

t1 = ()
t2 = (1,)
t2
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a','b',('ab','cd'))

del t1[0]
#튜플은 값을 설정후 못바꿈

t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
t3 = t1 + t2
#튜플을 정렬하려면 함수를 만들어서 새로 정의해야함 못바꾸니까
#튜플은 요솟값을 변경할수 없기 때문에 sort, insert, remove, pop과 같은 내장 함수가 없다.

#dictionary

a = {1: 'hi'}
a
a = { 'a': [1,2,3]}
a['b'] = [4,5,6]
a
a = {1: 'a'}
a[2] = 'b'
a
del a['b']
a

grade = {'pey':10, 'julliet': 99}
grade['julliet']

a = {1:'a',2:'b'}
a[1]

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
a.keys()
a.values()

a.items()
a.clear()
a
a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
a.get('name')
a['name']
#a.get('x') 방식은 'x'가 딕셔너리에 존재안해도 오류없이 none을 리턴함. False라는 뜻

a.get('nokey','foo') # 딕셔너리에 존재안해도 디폴트값 리턴방식

'name' in a
'namee' in a

# set

s1 = set([1,2,3])
s1

s2 = set("Hello")
s2

#set은 unordered, no duplicate

#set을 인덱싱하려면 list나 tuple로 변환

s1 = set([1,2,3])
l1 = list(s1)
s1[0]
l1[0]
t1 = tuple(s1)
t1

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

l1=[]
l1 = list(s1)
l2 = list(s2)
l3 = l1+l2
l3
l3.sort()
l3

s1&s2
s1.intersection(s2)
s1.intersection(s1)
s1&s1

s3 = set([1,2,3])
s4 = set([4,5,6])

s1 | s2
s1.union(s2)

s1
s2
s1-s2
s1.difference(s2)
s2.difference(s1)

s1 = set([1,2,3])
s1.add(4)
s1
s1.update([4,4,5,6,6,7,8,9])
s1
#set 에 add 나 update에 중복값 입력해도 하나만 추가됨

s1 = set([1,2,3])
s1.remove(2)
s1 = set([1,1,1,2,2,2,2,3,3,3,4,4,4,5])
#set에 다 지우려면 어캐하는진 몰겠음

# bool

