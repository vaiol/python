from collections import Counter, defaultdict
from operator import itemgetter
# Counter and defaultdict
# map and lambda
# itemgetter


# 1. lower
# 2. split
# 3. count every occurance
# 4. sort by words
# 5. sort by occurances



def popularity(text: str):
    # 1. lower
    lower_text = text.lower()
    # 2. split
    words_arr = lower_text.split(' ')
    
    # 3. count every occurance
    words_counter = dict()
    for w in words_arr:
        word = w.lower()
        if word in words_counter:
            words_counter[word] += 1
        else:
            words_counter[word] = 1

    def get_second_key(item):
        return item[1]
    
    def get_first_key(item):
        return item[0]

    # 4. sort by words
    sorted_by_word = sorted(words_counter.items(), key=get_first_key)

    # 5. sort by occurances
    sorted_by_popularity = sorted(sorted_by_word, key=get_second_key, reverse=True)
    
    # return
    sorted_words = list(map(get_first_key, sorted_by_popularity))
    return sorted_words



print(popularity('Apple kiwi pIneapple kiWi apple kiwi'))
print(popularity('aPPle pine Apple kiwi Apple kiwi')) # ['apple', 'kiwi', 'pine']
print(popularity('aPPle pine Apple kiwi Apple kiwi')) # ['apple', 'kiwi', 'pine']
print(popularity('aab aaa aac aab aac aaa x')) # ['aaa', 'aab', 'aac', 'x']






def popularity_1(text: str):
    # 1. lower
    lower_text = text.lower()
    # 2. split
    words_arr = lower_text.split(' ')

    # 3. sort by words
    words_arr.sort()
    
    # 4. count every occurance
    words_counter = defaultdict(int)
    for w in words_arr:
        word = w.lower()
        words_counter[word] += 1

    # 5. sort by occurances
    sorted_in_comb = sorted(words_counter.items(), key=itemgetter(1), reverse=True)
    sorted_words = list(map(itemgetter(0), sorted_in_comb))
    return sorted_words





# print(popularity_1('Apple kiwi pIneapple kiWi apple kiwi'))
# print(popularity_1('aPPle pine Apple kiwi Apple kiwi')) # ['apple', 'kiwi', 'pine']
# print(popularity_1('aPPle pine Apple kiwi Apple kiwi')) # ['apple', 'kiwi', 'pine']
# print(popularity_1('aab aaa aac aab aac aaa x')) # ['aaa', 'aab', 'aac', 'x']



def popularity_2(text: str):
    # 1. lower
    lower_text = text.lower()
    # 2. split
    words_arr = lower_text.split(' ')
    
    # 3. count every occurance
    words_counter = Counter(words_arr)

    # 4. sort by words and occurances
    sorted_in_comb = sorted(words_counter.items(), key=lambda item: (-item[1], item[0]))
    
    # convert list of tuple into list
    return list(map(itemgetter(0), sorted_in_comb))

print(popularity_2('Apple kiwi pIneapple kiWi apple kiwi'))
print(popularity_2('aPPle pine Apple kiwi Apple kiwi')) # ['apple', 'kiwi', 'pine']
print(popularity_2('aPPle pine Apple kiwi Apple kiwi')) # ['apple', 'kiwi', 'pine']
print(popularity_2('aab aaa aac aab aac aaa x')) # ['aaa', 'aab', 'aac', 'x']
