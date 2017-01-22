def condition_for_compare(word, u1, u2):
    return [u1 != -1,
            u2 != len(word),
            word[u1] == word[u2 % len(word)]]

def compare(word, u1, u2):
    return compare(word, u1 - 1, u2 + 1) if all(condition_for_compare(word, u1, u2)) else word[u1 + 1 : u2]

def find_even_pal(word):
    return map(lambda u:compare(word, u, u + 1), range(len(word) - 1))

def find_odd_pal(word):
    return map(lambda u:compare(word, u - 1, u + 1), range(1, len(word) - 1))

def find_pal(word):
    return list(find_even_pal(word)) + list(find_odd_pal(word))

def main(word):
    return max(find_pal(word), key = lambda x: len(x))

print(main('aa1aaa'))