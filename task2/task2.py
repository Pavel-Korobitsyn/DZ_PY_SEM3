def mult_lst(lst):
    l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    return new_lst

lst = [2, 3, 4, 5, 6]
#mult_lst(lst)
print(f"{lst} => {mult_lst(lst)}")