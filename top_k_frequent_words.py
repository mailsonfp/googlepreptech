def top_k_frequent_words(words, k):
    frequencies = [[] for _ in range(len(words) + 1)]
    count_dictionary = dict()

    for i in range(len(words)):
        count_dictionary[words[i]] = 1 + count_dictionary.get(words[i], 0)

    for key, val in count_dictionary.items():
        frequencies[val].append(key)

    array_return = []
    for i in range(len(frequencies)-1, 0, -1):
        frequencies[i].sort()
        for word in frequencies[i]:
            array_return.append(word)
            if len(array_return) == k:
                return array_return

    return array_return


if __name__ == '__main__':
    words_to_analyse = ["i", "love", "leetcode", "i", "love", "coding"]
    k_param = 2
    print(f"K frequent words: {top_k_frequent_words(words_to_analyse, k_param)}")

    words_to_analyse = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k_param = 4
    print(f"K frequent words: {top_k_frequent_words(words_to_analyse, k_param)}")

    words_to_analyse = ["i", "love", "leetcode", "i", "love", "coding"]
    k_param = 3
    print(f"K frequent words: {top_k_frequent_words(words_to_analyse, k_param)}")

