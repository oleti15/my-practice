def length_of_longest_substring(s: str) -> int:
    char_index = {}
    left = max_length = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length
s="abcabcbb"
print(length_of_longest_substring(s))
