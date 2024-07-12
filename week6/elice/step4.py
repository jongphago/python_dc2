def check(correct, answer):
    # 전역 변수 score를 사용합니다.
    global score, chance
    if answer == correct:
        print("맞았습니다.")
        score += 1
    else:
        # 틀렸을 때 기회가 남아있으면 기회를 하나 줄이고 다시 답을 입력받습니다.
        if chance > 1:
            # 기회를 하나 줄입니다.
            pass
            print(
                "틀렸습니다. 이번 문제를 맞출 수 있는 기회는 %d번 남았습니다." % chance
            )
            # 다시 답을 입력받습니다.데
            pass
        # 틀렸을 때 기회가 남아있지 않으면 다음 문제로 넘어갑니다.
        else:
            print("틀렸습니다. 다음 문제입니다. \n")
            pass
    print("\n")


score = 0
chance = None

# 변수 qst를 선언합니다.
qst = None
answer = input("똑똑한 사람을 가장 많이 만날 수 있는 곳은? ")
check("화장실", answer)

qst = None
answer = input(
    "공부시간에 교실에서 모두 공부하는데 유일하게 공부를 하지 않아도 혼나지 않는 사람은? "
)
check("선생님", answer)

qst = None
answer = input("세계에서 가장 빠른 차는? ")
check("첫차", answer)

print("당신의 점수는 %d점입니다." % score)
