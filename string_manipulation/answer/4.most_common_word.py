#4. 가장 흔한 단어
# 금지된 단어를 제외하고 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분이 없으며 특수문자는 제외한다.
import collections
from typing import List
import re

def most_common_word(s : str, banned : List[str]) -> str:
    words = [word for word in re.sub(pattern=r'[^\w]',repl=' ',string=s).lower().split() if word not in banned]
    print(words)

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]




if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
    banned = ["hit"]
    print(most_common_word(paragraph, banned))