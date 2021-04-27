def search(text, pattern):
    cmp_count = 0
    text_size = len(text)
    pattern_size = len(pattern)
    if pattern_size == 0:
        return (0, cmp_count)
    if text_size == 0 or pattern_size > text_size:
        return (-1, cmp_count)

    shift_distance = [pattern_size for x in range(5000)]
    for i in range(pattern_size - 1):
        shift_distance[ord(pattern[i])] = pattern_size - i - 1
    i = 0
    while i < text_size - pattern_size + 1:
        flag = True
        for j in range(pattern_size - 1, -1, -1):
            cmp_count += 1
            if text[i+j] != pattern[j]:
                i += shift_distance[ord(text[i+j])]
                flag = False
                break
        if flag:
            return (i, cmp_count)
    return (-1, cmp_count)
