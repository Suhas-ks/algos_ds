def compute_failure(pattern):
    m = len(pattern)
    fail = [0] * m
    k = 0
    for j in range(1, m):
        while k > 0 and pattern[j] != pattern[k]:
            k = fail[k - 1]
        if pattern[j] == pattern[k]:
            k += 1
        fail[j] = k
    return fail


def kmp_match(text, pattern):
    n, m = len(text), len(pattern)
    fail = compute_failure(pattern)
    j = 0
    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = fail[j - 1]
        if pattern[j] == text[i]:
            j += 1
        if j == m:
            return i - j + 1
    return None


pattern = 'cat'
text = 'the quick brown fox jumps over the lazy dog and the dog barks'

ind = kmp_match(text, pattern)
if ind != None:
    print(text[ind: ind + len(pattern)])
else:
    print('match not found :(')
