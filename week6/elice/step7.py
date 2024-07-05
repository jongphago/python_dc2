# [미션] STEP 7 수수께끼 업그레이드 하기

import random


def check(correct, answer):
    global score, chance
    # 공백을 제거합니다.
    answer = None
    if answer == correct:
        print("맞았습니다.\n")
        score += chance
        # 다음 문제로 넘어가기 전에 기회를 3으로 초기화합니다.
        chance = None
    else:
        if chance > 1:
            # 기회를 하나 줄입니다.
            pass
            print(
                "틀렸습니다. 이번 문제를 맞출 수 있는 기회는 %d번 남았습니다." % chance
            )
            answer = input(qst)
            check(correct, answer)
        else:
            print("틀렸습니다. 다음 문제입니다. \n")
            # 다음 문제로 넘어가기 전에 기회를 3으로 초기화합니다.
            chance = None


score = 0
chance = 3

bank = [
    ["똑똑한 사람을 가장 많이 만날 수 있는 곳은? ", "화장실"],
    [
        "공부시간에 교실에서 모두 공부하는데 유일하게 공부를 하지 않아도 혼나지 않는 사람은? ",
        "선생님",
    ],
    ["세계에서 가장 빠른 차는? ", "첫차"],
    ["산토끼의 반대말은? ", "죽은토끼"],
    ["물고기의 반대말은? ", "불고기"],
    ["사람들이 가장 싫어하는 거리는? ", "걱정거리"],
]

qst_num = []
ran_num = random.randint(0, len(bank) - 1)

for i in range(2):
    while ran_num in qst_num:
        ran_num = random.randint(0, len(bank) - 1)
    qst_num.append(ran_num)

    q = bank[ran_num]
    qst = q[0]
    correct = q[1]

    answer = input(qst)
    check(correct, answer)

print("당신의 점수는 %d점입니다." % score)
