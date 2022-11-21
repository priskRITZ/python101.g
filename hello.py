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
