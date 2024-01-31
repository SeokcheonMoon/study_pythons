# https://www.acmicpc.net/problem/10809

# 문제
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

a=0
b=1
c=2
d=3
e=4
f=5
g=6
h=7
i=8
j=9
k=10
l=11
m=12
n=13
o=14
p=15
q=16
r=17
s=18
t=19
u=20
v=21
w=22
x=23
y=24
z=25

list_alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

pass

str_text = input()                                          #baekjoon
text = list(str_text)                                       #['b', 'a', 'e', 'k', 'j', 'o', 'o', 'n']

answer_list = []
for x in range(len(list_alphabet)):
    answer_list.append(-1)

for index in range(len(text)):
    a=0
    if text[x] :
        a = a + 1
    else : 
        
text["b"]=1

인풋을 받고 list_alphabet 요소 전부 다를 baekjoon의 알파벳과 비교
리스트 알파벳 안에 백준의 b가 있으면 순서를 출력
나머지면 -1을 출력