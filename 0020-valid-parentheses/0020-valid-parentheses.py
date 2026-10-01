class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        mapping = {")" : "(", "}": "{", "]": "["}

        for st in s:
            if st in mapping.values():
                stck.append(st)

            if st in mapping.keys():
                if not stck or mapping[st] != stck.pop():
                    return False

        return not stck