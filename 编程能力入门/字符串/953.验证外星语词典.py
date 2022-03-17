class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # def compare(word1, word2):
        #     char1, char2 = "", ""   # 要比较的两个字符
        #     i, j = 0, 0
        #     while i < len(word1) and j < len(word2):
        #         if word1[i] != word2[j]:
        #             char1, char2 = word1[i], word2[j]
        #             return char1, char2
        #         else:
        #             i += 1
        #             j += 1
        #     if i == len(word1) and j != len(word2): # word1走到了尽头
        #         char2 = word2[j]
        #     if i != len(word1) and j == len(word2):   # word2先走到了尽头
        #         char1 = word1[i]  
        #     return char1, char2
        # if len(words) == 1:
        #     return True
        # dic = {}
        # for i in range(len(order)):
        #     dic[order[i]] = i
        # # ""就对应-1
        # # return compare(words[0], words[1])
        # for i in range(1, len(words)):
        #     char1, char2 = compare(words[0], words[1])  # 要比较的两个字符
        #     if dic.get(char1, -1) > dic.get(char2, -1):
        #         return False
        # return True

        order_index = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1), len(word2))):
                if word1[j] != word2[j]:
                    if order_index[word1[j]] > order_index[word2[j]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True