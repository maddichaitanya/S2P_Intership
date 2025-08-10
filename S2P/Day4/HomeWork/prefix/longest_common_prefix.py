def longest_common_prefix(strs):
    if not strs:  # If list is empty
        return ""
    
    prefix = strs[0]  # Assume first word is the prefix initially
    for word in strs[1:]:  # Compare with each next word
        while not word.startswith(prefix):
            prefix = prefix[:-1]  # Remove last character until it matches
            if not prefix:  # If prefix becomes empty
                return ""
    return prefix
# Example
words = ["flower", "flow", "flight"]
print("Longest Common Prefix:", longest_common_prefix(words))
