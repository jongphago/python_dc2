def makeURL(*words):
    url = "www."
    for word in words:
        url += word
        url += "_"
    url += ".com"
    return url


# 함수의 기능을 완성하세요.
myURL = makeURL("dlab", "python")  # 호출예시
# myURL = makeURL()    #원하는 매개변수 작성하기
print(myURL)
