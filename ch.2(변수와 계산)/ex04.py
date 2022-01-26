#한 사람이 돈이 5000원이 있는데 사탕의 가격이 120원이라면 최대로 살 수 있는
#사탕의 수를 알아보는 프로그램

mymoney=5000
candyPrice=120
#최대로 살 수 잇는 사탕의 개수
# /를 하나로 넣으면 실수, //를 넣으면 정수가 출력
numCandies = mymoney// candyPrice
print("최대로 살 수 있는 사탕의 개수 : ", numCandies)

#사탕을 구입하고 남은 돈
change = mymoney%candyPrice
print("최대로 살 수 있는 사탕을 구입하고 남은 돈 : ", change)

