class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        length = len(sentence)
        sentence += sentence
        for i in range(0, length):
            if sentence[i][-1] != sentence[i+1][0]:
                return False
        return True
print(Solution.isCircularSentence(Solution,sentence = "Leetcode is cool"))