from collections import Counter

my_list = [10,10,22,22,10,9,17,9,22,10,8]
counter = Counter(my_list)

print(counter)
print(counter[17])
print(counter[22])

most_common = counter.most_common(1)

print(most_common)
print(most_common[0])
print(most_common[0][0])