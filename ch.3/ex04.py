# 문자열에 대한 실습

# 큰 따옴표(double quotation)로 묶으면 문자열이 된다.
welcome = "Happy New Year 2022"
print(welcome)

# 작은 따옴표(single quotation)로 묶으면 문자열이 된다.
welcome='Happy New Year 2022'
print(welcome)

# 문자열을 만들때 시작을"으로 했는데 '으로 끝을 낸다면, EOL(End Of Line) 에러 발생
# 그 이유는 "로 시작을 했는데 끝에 "의 끝내용을 찾을 수 없다라고 하는 것이다
#welcome="Happy New Year 2022'
#print(welcome)


#welcome="Happy New Year 2022
#print(welcome)

#아래와 같이 ""안에 또 다른 ""이 들어있다면 컴파일러가 혼돈을 일으켜 틀린 문법이라고 인식함
#message="은혁이가 "안녕하세요"라고 인사했습니다."
#print(message)

message="은혁이가 '안녕하세요'라고 인사했습니다."
print(message)

#파이썬에서는 따옴표를 출력하고자 할떄, \를 이용한다.
#\가 따옴표 앞에 있느면 '는 특수한 의미를 잃어버리고 하나의 문자로 편승이 되어 문자열을 이룬다.
message = 'doesn\'t'
print(message)

message="\"Yes,\" I can do it"
print(message)