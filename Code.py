class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        f = 1
        for x in words:
            for y in set(x):
                if y not in allowed:
                    c += 1
            if f == 1:
                c += 1
            else:
                f = 1
        return c
            
