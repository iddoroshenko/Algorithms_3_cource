def search(text, pattern):
    cmp_count = 0
    text_size = len(text)
    pattern_size = len(pattern)
    if pattern_size == 0:
        return (0, cmp_count)
    if text_size == 0 or pattern_size > text_size:
        return (-1, cmp_count)
    for i in range(text_size - pattern_size + 1):
        isEqual = True
        for j in range(pattern_size):
            cmp_count += 1
            if text[i+j] != pattern[j]:
                isEqual = False
                break
        if isEqual:
            return i, cmp_count
    return -1, cmp_count
