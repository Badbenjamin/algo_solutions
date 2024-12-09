def canConstruct(ransomNote, magazine):
        rn = list(ransomNote)
        mag = list(magazine)

        result = []
        for char in ransomNote:
            if char in mag:
                result.append(mag.pop(mag.index(char)))
            else:
                return False
        return True
