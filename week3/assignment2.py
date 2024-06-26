def calcTime(city):  # -> (h)
    global speed, cityList
    distance = cityList[city]
    time = distance / speed  # 매개변수 'city'에 따라 걸리는 시간을 계산하세요.
    return time


speed = 60  # (km/h)
cityList = {"대구": 295.5, "대전": 167.9, "여수": 348.9}  # (km)

city = "대구"
time = calcTime(city)
print(f"{city} takes {time} hours.")
