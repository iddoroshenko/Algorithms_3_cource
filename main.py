import search_string.native as native
import search_string.rabin_karp as rabin_karp

if __name__ == '__main__':
    print('Hi Anya and Sasha')
    print(native.search("qwerty", "ert"))
    print(rabin_karp.search("qwerty", "ert"))
