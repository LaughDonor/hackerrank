from re import findall

# Set indexing of word
def get_index(word):
    word = list(word)
    return [word.index(x) for x in word]

def remap(plainword, cipherword):
    for p, c in zip(plainword, cipherword):
        if az[c] is None:
            az[c] = p

# Setup list of words
with open('dictionary.lst', 'r') as f:
    words = f.read().lower().split()
cipher = raw_input().split()

# Go for only words shorter than max length
size = len(reduce(lambda x, y: y if len(y) > len(x) else x, cipher))
uniquewords = len(set(cipher))

wordsl = {}
cipherl = {}
for n in range(1, size + 1):
    cipherl[n] = [(x, get_index(x)) for x in cipher if len(x) == n]
    wordsl[n] = [(x, get_index(x)) for x in words if len(x) == n] if len(cipherl[n]) else []

# Setup Alphabet dictionary to map letters to each other
az = dict((x, None) for x in list('abcdefghijklmnopqrstuvwxyz'))

dictionary = {}
# Loop until word bank is filled up
while len(dictionary) < uniquewords:
    left = True
    # Try finding matches with same index pattern
    for n in range(size, 0, -1):
        for i, word in enumerate(cipherl[n]):
            filt = [x for x in wordsl[n] if word[1] == x[1]]
            if len(filt) == 1:
                remap(filt[0][0], word[0])
            if all([az[z] for z in word[0]]):
                dictionary[cipherl[n][i][0]] = ''.join([az[z] for z in word[0]])
                cipherl[n].pop(i)
                left = False
    # If no matches found, try using regex with letters found
    if left:
        for n in range(size, 0, -1):
            for i, word in enumerate(cipherl[n]):
                x = findall(''.join([az[z] or '\w' for z in word[0]]),
                            '-'.join([x[0] for x in wordsl[n] if x[1] == word[1]]))
                if len(x) == 1:
                    remap(x[0], word[0])
                    dictionary[word[0]] = x[0]
                    cipherl[n].pop(i)
print ' '.join([dictionary[x] for x in cipher])
