def solve(word):
    # generate english dictionary
    words = set()
    ref_counts = get_char_counts(word)

    f = open('./my_6of12.txt', 'r')
    for line in f:
        #remove \n character
        w = line[:-1]
        # assume we ignore case
        w = w.lower()
        char_counts = get_char_counts(w)
        # print(char_counts)
        w_is_subset = True
        for char, count in char_counts.items():
            if char not in ref_counts or count > ref_counts[char]:
                w_is_subset = False
                break

        if w_is_subset:
            words.add(w)

    f.close() 
    return words

def get_char_counts(string):
    counts = {}
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


