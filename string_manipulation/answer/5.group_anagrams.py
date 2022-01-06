#문자열을 받아 애너그램 단위로 그룹핑을 하라. ==> 동일한 알파벳을 가진 단어끼리 그룹핑을 하라
import collections
from typing import List

def group_anagrams(l : List[str]) -> List[List[str]]:
    anagram = collections.defaultdict(list)

    for word in l:
        anagram[''.join(sorted(word))].append(word)

    return list(anagram.values())

if __name__ == '__main__':
    l = ["eat","tea","tan","ate","nat","bat"]
    print(group_anagrams(l))