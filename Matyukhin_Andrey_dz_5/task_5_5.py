src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
rep = set()
no_rep = set()
for el in src:
    if el in no_rep:
        rep.add(el)
        no_rep.remove(el)
    else:
        no_rep.add(el)
result = [num for num in src if num in no_rep]
print(result)
