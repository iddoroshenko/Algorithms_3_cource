def search(text, pattern):
    text_size = len(text)
    pattern_size = len(pattern)
    if pattern_size == 0:
        return 0
    if text_size == 0 or pattern_size > text_size:
        return -1
    for i in range(text_size - pattern_size + 1):
        # There is more easy way to write this:
        #
        # if text[i:i+pattern_size] == pattern:
        #   return i
        #
        # but looks like get slice operation takes O(pattern_size) time
        # and comparison takes O(pattern_size) time.
        # It could be more expensive than simple loop
        #
        # But if you think that this is nonsense and not an important thing
        # you could delete the code below and insert the simpler method
        isEqual = True
        for j in range(pattern_size):
            if text[i+j] != pattern[j]:
                isEqual = False
                break
        if isEqual:
            return i
    return -1
