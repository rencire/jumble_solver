import argparse


def solve(word, file):
    """Generates a set of words that can be created from input word"""
    words = set()
    ref_counts = get_char_counts(word)

    f = open(file, 'r')
    for line in f:
        #remove \n character
        w = line[:-1]
        # assume we ignore case
        w = w.lower()
        char_counts = get_char_counts(w)
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A word jumble solver.  Prints a list of words that can be formed from the input word.')
    parser.add_argument('word', help='Input string for word jumble')
    parser.add_argument('-d', '--dictionary', help='Use a different dictionary file other than the default.  Dictionary file  must contain one word per line or else unexpected results might happen.')
    args = parser.parse_args()
    
    file = './my_2of12_dict.txt'
    if args.dictionary:
        file = args.dictionary

    words = solve(args.word, file)
    for w in words:
        print(w)


