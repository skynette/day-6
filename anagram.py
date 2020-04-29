def find_anagrams(word, candidates):
    ans = []
    word_length = len(word)
    sorted_word = sorted(word.lower())
    for words in candidates:
        if len(words) == word_length:
            if words.lower() == word.lower():
                continue
            elif sorted(words.lower()) == sorted_word:
                ans.append(words)
    return ans