class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # I want to create a dict for [hash_word: List[word]]
        # iterate through the whole list, where for each word we hash it, check if it's in the dictionary, and add it
        # this should be memory and time o(n)
        ans = []
        words_dict = dict()

        for word in strs: 
            hash_word = "".join(sorted(word))

            if hash_word in words_dict:
                words_dict[hash_word].append(word)
            else:
                words_dict[hash_word] = [word]
        
        for k in words_dict.values():
            ans.append(k)

        return ans