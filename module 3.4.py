def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.upper() in root_word.upper():
            same_words.append(i)
    return same_words

results1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
results2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(results1)
print(results2)