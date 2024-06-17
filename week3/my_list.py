class MyList:
    def __init__(self, value=[]):
        print("MyList가 생성되었습니다.")
        self.value = value
        
    def __str__(self) -> str:
        return str(self.value)
    
    def append(self, obj) -> None:
        self.value += [obj]  # in-place
        return None


ml = MyList()
print(ml)
res = ml.append(1)
print(res)
print(ml)