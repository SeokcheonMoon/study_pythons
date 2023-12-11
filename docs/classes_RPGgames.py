# functionn만 사용하여 적 캐릭터 만들기

# first enemy character 조건
name_first = "first"
health_first = 120
damage_first = 0

def attack(health, damage) :
    health = health - damage
    return health

damage_first = attack(health_first,5)

# second enemy character 조건
name_second = "second"
health_second = 200
damage_second = 0

damage_second = attack(health_second,10)

# function만 사용 시 제한 극복 -> class를 사용한다!! 공통적인 부분들을 class로 묶음.

class Enemy : 
    def __init__(self, name, health) : #내가 초기화시키고 싶은 변수를 위해 만듬. # 밖에서 들어오는 name,health
        self.name = name #---------------------------------------------------->#  왼쪽 self.name은 안에서 사용하는 name. 오른쪽 name은 위에서 온 name            윗줄과 해당줄의 name은 서로 다르다.
        self.health = health
        self.damage = 0
    
    def attack(self, damage) : #--------------------------class 안의 변수들이기 때문에 각각에 self.를 붙여줌.
        self.health = self.health - self.damage
        return self.health

    def function_name(self) : 
        pass
        return 0
    
first_enemy = Enemy('first', 150) #--------------------------->>>자신의 자원(function과 변수같은 vaule)를 확인
second_enemy = Enemy('second', 300)
pass
