#4. 가장 흔한 단어
# 금지된 단어를 제외하고 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분이 없으며 특수문자는 제외한다.
from typing import List

def most_common_word(s : str, banned : List[str]) -> str:
    return None;



if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
    banned = ["hit"]
    print(most_common_word(paragraph, banned))