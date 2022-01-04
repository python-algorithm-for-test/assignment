from typing import List

def reverse_string(s : List[str]) -> List[str]:
    return s[::-1]


if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    print(reverse_string(s))