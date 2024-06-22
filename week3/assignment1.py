def calcTime(speed, distance):  # -> h
    time = distance / speed  # 걸리는 시간을 계산하세요.
    return time


speed = 60  # 말의 속도 (km/h)
distance = 295.5  # 서울에서 대구까지의 거리 (km)

hours = calcTime(speed, distance)
print(hours)
