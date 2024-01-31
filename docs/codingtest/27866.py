# https://www.acmicpc.net/problem/27866

# 문제
# 단어 
# $S$와 정수 
# $i$가 주어졌을 때, 
# $S$의 
# $i$번째 글자를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 영어 소문자와 대문자로만 이루어진 단어 
# $S$가 주어진다. 단어의 길이는 최대 
# $1\,000$이다.

# 둘째 줄에 정수 
# $i$가 주어진다. (
# $1 \le i \le \left|S\right|$)

# 출력
#  
# $S$의 
# $i$번째 글자를 출력한다.

str_text = input()
str_index = input()
index = int(str_index)
list_text = list(str_text)
print(list_text[index-1])