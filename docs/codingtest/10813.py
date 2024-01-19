# https://www.acmicpc.net/problem/10813

# 문제
# 도현이는 바구니를 총 N개 가지고 있고, 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있다. 바구니에는 공이 1개씩 들어있고, 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 들어있다.

# 도현이는 앞으로 M번 공을 바꾸려고 한다. 도현이는 공을 바꿀 바구니 2개를 선택하고, 두 바구니에 들어있는 공을 서로 교환한다.

# 공을 어떻게 바꿀지가 주어졌을 때, M번 공을 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

# 둘째 줄부터 M개의 줄에 걸쳐서 공을 교환할 방법이 주어진다. 각 방법은 두 정수 i j로 이루어져 있으며, i번 바구니와 j번 바구니에 들어있는 공을 교환한다는 뜻이다. (1 ≤ i ≤ j ≤ N)

# 도현이는 입력으로 주어진 순서대로 공을 교환한다.

# 출력
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호를 공백으로 구분해 출력한다.
def ball_count() :
    str_bucket_count, str_ball_cycle = input().split()              # 5, 4

    bucket_count = int(str_bucket_count)
    ball_cycle = int(str_ball_cycle)

    ball_count = []

    for x in range(1,bucket_count+1):                                       # 5번
        ball_count.append(x)
        pass


    for y in range(ball_cycle) :                                            # 4회
        str_bucket_first, str_bucket_second = input().split()
        bucket_first = int(str_bucket_first)-1
        bucket_second = int(str_bucket_second)-1

        
        bucket_refirst =  ball_count[bucket_first]
        ball_count[bucket_first] = ball_count[bucket_second]
        ball_count[bucket_second] = bucket_refirst
        pass
    ball_count = " ".join(map(str,ball_count))
    print(ball_count)

    return
ball_count()