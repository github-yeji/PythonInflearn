# 사용자로부터 참석하는 인원의 수를 받아 해당하는 인원의 수의 따라서
# 치킨은 인원당 1마리, 맥주는 인원당 2병, 케익은 인원당 4개를 출력하는
# 프로그램을 작성하시오.

#iput()함수는 사용자로부터 입력값을 받지만 문자열 형태로 저장
#문자열을 숫자로 바꾸기 위해서 int()함수를 사용
number = int(input("참석자 수를 입력하시오: "))
print(type(number))
chickens = number
beeers = number*2
cakes = number*4
print("치킨의 수:", chickens)
print("맥주의 수:", beeers)
print("케익의 수:", cakes)