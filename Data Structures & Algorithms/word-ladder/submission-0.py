class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        q = deque([beginWord])
        visit = set([beginWord])
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return step
                for i in range(len(word)):
                    for c in range(ord('a'), ord('z') + 1):
                        newWord = word[:i] + chr(c) + word[i + 1:]

                        if newWord not in visit and newWord in wordList:
                            visit.add(newWord)
                            q.append(newWord)
        return 0