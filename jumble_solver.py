def solve(word):
    # generate english dictionary
    eng_dict =  set()
    f = open('6of12.txt', 'r')
    for line in f:
        #remove \n character
        w = line[:-1]
        eng_dict.add(w)
    f.close() 

    words = set()
    while word:
        # for each permutation, check if its a word
        print(word)
        perms = permutations(word)
        # print(perms)
        for w in perms:
            if w in eng_dict:
                # print(w)
                words.add(w)   
        word = word[1:]

    return words


def permutations(str):
    if len(str) == 1:
       return set([str])
               
    result = set()
    perms = permutations(str[1:])
    for perm in perms:
        for i in range(len(str)):
            result.add(perm[:i] + str[0] + perm[i:])

    return result
        
        
       


