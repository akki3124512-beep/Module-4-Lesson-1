empty = []
l = ['abc', 'cfc', 'xyz', 'aba', '1221']
for i in l:
    if i == i[::-1]:
        empty.append(i)
print(empty)
print("Here are how many words that can reverse: ", len(empty))