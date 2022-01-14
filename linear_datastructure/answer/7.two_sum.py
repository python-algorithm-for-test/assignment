#두 수의 합
#덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하시오
from typing import List

def twoSum(l:List[int], target:int) -> List[int]:
    num_map = {}
    for idx, val in enumerate(l):
        if target - val in num_map: #if exists in key list?
            return [num_map[target - val], idx]
        num_map[val] = idx


if __name__ == '__main__':
    l = [2,7,11,15]
    target = 9
    print(twoSum(l, target)) #return :[0,1]