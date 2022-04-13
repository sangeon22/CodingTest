word = input().upper()
set_word = list(set(word))
count = []

for i in set_word:
    count.append(word.count(i))
if count.count(max(count)) > 1:
   print("?")
else:
    index = count.index(max(count))
    print(set_word[index])