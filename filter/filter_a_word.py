
words = ['saya makan', 'pergi ke sana', 'apel']

results = []

for word in words:
    if len(word.split(' ')) > 1:
        results.append(word)

print(results)