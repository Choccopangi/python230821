# demoFormat.py

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(5))

# 문자열 결합
for i in range(10):
    url = "https://www.multicampus.com/?page=" + str(i)
    print(url)

# 파일 쓰기
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 위 경로는 \\, 밑 경로는 \ 
# 위: \n,\t 등과 구분하기 위해 \ 2번 씀
# 밑: r(raw string notation) - 날 것 그대로 코딩하겠다

# 파일 읽기
f = open(r"c:\work\demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
f.close()

# 서식 지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000000))