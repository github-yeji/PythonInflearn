#파이썬 터틀 모듈
import turtle

t=turtle.Pen()

##캔버스의 마우스 형태의 그림을 거북이 모양으로 바꾸어줌
t.shape("turtle")

##그림 색상을 파란색으로 바꾸어 줌
t.pencolor("blue")

##직선으로 100픽셀 만큼 선을 그려
t.forward(100)
##오른쪽으로 90도 만큼 방향을 바꾸어라
t.right(90)
##
t.forward(100)
