from math import *
# 파이썬에서의 자료현(Data-type)
# int형을 출력
print(type(17))
#float형을 출력
print(type(10.777999))
#str 형을 출력
print(type("안녕하세요"))

#반지름이 r인 구의 부피는 4/3 * PI * r^3
#반지름이 5인 구의 부피를 구하는 프로그램
r=5.0
#volume=4.0/3.0*pi*(r**3)
volume=4.0/3.0*pi* pow(r, 3)
print("구의 부피", volume)
#문자열 + float은 타입 일치가 안되어 문자열을 생성할 수 없음
#해결하기 위한 방안은 문자열 즉 숫자로 변환 되지 않는 문자열에다가 int()를
#사용하면 error 를 발생시키고, 아울러 +연산이 이루어 지지 않음을 알 수가 있다
#하여 이때는 실수값을 str()를 이용하여 문자열로 변환을 하면 + 연산이 이루어진다
print("구의 부피" + str(volume))
#구의 겉넓이의 공식: 4*pi*r^2
outer_area=4*pi*pow(r,2)
print("구의 겉넓이", outer_area)