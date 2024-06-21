global_var = 1
global_list = []


def func():
    local_val = global_var
    # global_var += 1  # UnboundLocalError
    global_list.append(1)
    
    print(f"In func local_val: {local_val}")
    print(f"In func global_var: {global_var}")

# print(f"In main global_list ID: {id(global_list)}")
func()
print(f"In main global_var: {global_var}")
# print(f"In main global_list ID: {id(global_list)}")
print(f"In main global_list: {global_list}")
