print(id)  # <built-in function id>
id = 'global'

# Local - Enclosing - Global - Built-in
def func():
    def enclosing():
        id = 'enclosing'
        print(f"[elcosing] id: {id}")
    enclosing()
    id = 'local'
    #     # id += 1  # UnboundLocalError

    print(f"[func] id: {id}")


print(f"[main] id: {id}")
func()
print(f"[main] id: {id}")
