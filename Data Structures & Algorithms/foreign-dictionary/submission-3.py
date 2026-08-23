class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indegree = defaultdict(int)
        edges = defaultdict(set)
        chars = set(words[0])
        for i in range(1, len(words)):
            prev, word = words[i-1], words[i]
            if prev == word:
                continue
            if prev.startswith(word):
                return ""
            for j in range(min(len(word), len(prev))):
                if word[j] == prev[j]:
                    continue
                if word[j] not in edges[prev[j]]:
                    indegree[word[j]] += 1
                    edges[prev[j]].add(word[j])
                break

            chars.update(word)
        queue = deque([])
        for c in chars:
            if indegree[c] == 0:
                queue.append(c)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for dependent in edges[node]:
                indegree[dependent] -= 1
                if indegree[dependent] <= 0:
                    queue.append(dependent)
        if len(res) != len(chars):
            return ""
        return "".join(res)