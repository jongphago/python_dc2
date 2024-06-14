def ticket(student, adult):
    pass

total = 0
for i in range(5):
    n1 = int(input("청소년 몇 명?: "))
    n2 = int(input("어른 몇 명?: "))
    money = ticket(n1, n2)
    total += money

    print("총 {}원 입니다.".format(money))
    print("---------------")

print("전체 입장료: %d원" % total)
