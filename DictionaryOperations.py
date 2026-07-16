def demonstrateDictionary():
    d = {'a': 10, 'b': 20, 'c': 30}
    d['a'] = 15
    print(f"Sum: {sum(d.values())}")
    sorted_by_key = dict(sorted(d.items()))
    text = "hello world hello"
    freq = {word: text.split().count(word) for word in set(text.split())}
    print(f"Key exists: {'a' in d}")
