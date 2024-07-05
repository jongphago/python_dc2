# [미션] STEP 3 점수 계산하기
def check(corret, answer):
    # 전역 변수 score를 사용합니다.
    pass
    if answer == corret:
        print("맞았습니다.")
        # 점수를 1점 올립니다.
        pass
    else:
        print("틀렸습니다.")
    print("\n")


score = 0

answer = input("똑똑한 사람을 가장 많이 만날 수 있는 곳은? ")
check("화장실", answer)

answer = input(
    "공부시간에 교실에서 모두 공부하는데 유일하게 공부를 하지 않아도 혼나지 않는 사람은? "
)
check("선생님", answer)

answer = input("세계에서 가장 빠른 차는? ")
check("첫차", answer)

print("당신의 점수는 %d점입니다." % score)
