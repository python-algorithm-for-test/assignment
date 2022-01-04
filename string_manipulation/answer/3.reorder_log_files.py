#* 로그를 다음 기준으로 재정렬 하시오.
#1. 로그의 가장 앞 부분은 식별자다.
#2. 문자로 식별된 로그가 숫자 로그보다 앞에 온다.
#3. 식별자는 순서에 영향을 끼치진 않지만, 문자가 동일할 경우 식별자 순으로 한다.
#4. 숫자 로그는 입력 순서대로 한다.

from typing import List

def reorder_log(logs : List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split(" ")[1].isdigit():
           digits.append(log)
        else:
            letters.append(log)

    letters.sort(key= lambda x : (x.split()[1:], x.split()[0]))
    return letters + digits

if __name__ == '__main__':
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig", "let3 art zero"]
    print(reorder_log(logs)) #["let1 art can",let3 art zero","let2 own kit dig", "dig1 8 1 5 1",, "dig2 3 6"]