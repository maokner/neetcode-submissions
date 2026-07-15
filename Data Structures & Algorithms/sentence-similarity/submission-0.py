class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        for idx in range(len(sentence1)):
            w1 = sentence1[idx]
            w2 = sentence2[idx]
            if w1 != w2:
                if [w1, w2] not in similarPairs and [w2, w1] not in similarPairs:
                    return False
        
        return True
        