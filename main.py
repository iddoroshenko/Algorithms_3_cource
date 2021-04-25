import search_string.native as native
import search_string.rabin_karp as rabin_karp
import search_string.boyer_moore as boyer_moore
import search_string.knuth_morris_pratt as knuth_morris_pratt
import search_string.aho_corasick as aho_corasick
import time


def test_string_search_algorithm(text, pattern):
    # Native search
    start = time.time()
    res = native.search(text, pattern)
    stop = time.time()
    print("Native\ni:", res[0], "number of comparisons:", res[1])
    print('Time:', stop - start)

    #Rabin_Karp
    start = time.time()
    res = rabin_karp.search(text, pattern)
    stop = time.time()
    print("rabin_karp\ni:", res[0], "number of comparisons:", res[1])
    print('Time:', stop - start)

    # Boyer_Moore
    start = time.time()
    res = boyer_moore.search(text, pattern)
    stop = time.time()
    print("boyer_moore\ni:", res[0], "number of comparisons:", res[1])
    print('Time:', stop - start)

    # Knuth_Morris_Pratt
    start = time.time()
    res = knuth_morris_pratt.search(text, pattern)
    stop = time.time()
    print("knuth_morris_pratt\ni:", res[0], "number of comparisons:", res[1])
    print('Time:', stop - start)

    # Aho_Corasick
    start = time.time()
    res = aho_corasick.search(text, pattern)
    stop = time.time()
    print("aho_corasick\ni:", res[0], "number of comparisons:", res[1])
    print('Time:', stop - start)


if __name__ == '__main__':
    print('UNIT TESTS:\n')
    res = native.search("qwerty", "ert")
    print('Native  i:', res[0], "number of comparisons:", res[1])
    res = rabin_karp.search("qwerty", "ert")
    print('Rabin_Karp  i:', res[0], "number of comparisons:", res[1])
    res = boyer_moore.search("qwerty", "ert")
    print('Boyer_Moore  i:', res[0], "number of comparisons:", res[1])
    res = knuth_morris_pratt.search("qwerty", "ert")
    print('Knuth_Morris_Pratt  i:', res[0], "number of comparisons:", res[1])
    a = aho_corasick.AhoKorasick()
    a.add_pattern(pattern='acc')
    a.add_pattern(pattern='atc')
    a.add_pattern(pattern='cat')
    a.add_pattern(pattern='gcg')
    a.set_links()
    res = a.search('gcatcg')
    print('1. Aho_Korasick  i:', res)

    b = aho_corasick.AhoKorasick()
    b.add_pattern(pattern='a')
    b.add_pattern(pattern='ab')
    b.add_pattern(pattern='bc')
    b.add_pattern(pattern='c')
    b.set_links()
    res = b.search('gcatcg')
    print('2. Aho_Korasick  i:', res)

    print('\nTESTS:')
    print("File: bad_t_1")
    f_text = open("benchmarks/bad_t_1.txt", "r")
    f_pattern = open("benchmarks/bad_w_1.txt", "r")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: bad_t_2")
    f_text = open("benchmarks/bad_t_2.txt", "r")
    f_pattern = open("benchmarks/bad_w_2.txt", "r")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: bad_t_3")
    f_text = open("benchmarks/bad_t_3.txt", "r")
    f_pattern = open("benchmarks/bad_w_3.txt", "r")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: bad_t_4")
    f_text = open("benchmarks/bad_t_4.txt", "r")
    f_pattern = open("benchmarks/bad_w_4.txt", "r")
    test_string_search_algorithm(f_text.read(), f_pattern.read())

    print("\nFile: good_t_1")
    f_text = open("benchmarks/good_t_1.txt", "r", encoding="utf-8")
    f_pattern = open("benchmarks/good_w_1.txt", "r", encoding="utf-8")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: good_t_2")
    f_text = open("benchmarks/good_t_2.txt", "r", encoding="utf-8")
    f_pattern = open("benchmarks/good_w_2.txt", "r", encoding="utf-8")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: good_t_3")
    f_text = open("benchmarks/good_t_3.txt", "r", encoding="utf-8")
    f_pattern = open("benchmarks/good_w_3.txt", "r", encoding="utf-8")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
    print("\nFile: good_t_4")
    f_text = open("benchmarks/good_t_4.txt", "r", encoding="utf-8")
    f_pattern = open("benchmarks/good_w_4.txt", "r", encoding="utf-8")
    test_string_search_algorithm(f_text.read(), f_pattern.read())
