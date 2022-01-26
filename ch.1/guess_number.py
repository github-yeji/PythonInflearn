print("숫자 게임 시작합니다.")
number = 62
#input()는 사용자로부터 값을 입력 받기 위해서 사용된다.
exact_num=input("1에서 100사이으 숫자를 추측해보세요.")
print(exact_num)
#문자열로 넘어온 값을 int()를 이용하여 숫자로 바꿔주고 있다.
guess = int(exact_num)

if guess == number :
    print("정답입니다")
else :
    print("오답입니다")
print("게임이 종료 되었습니다")