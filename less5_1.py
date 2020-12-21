from typing import List

some_list = [1, 2, 3, [11, 21, 31, [22, 33]], 1, 1, [[[44, 45]]]]


def flat_list(data: List[list]) -> List[int]:
    for itm in data:
        if isinstance(itm, list):
            yield from flat_list(itm)
        else:
            yield itm


some_result = flat_list(some_list)

print(some_result)

# print(list(map(eval,some_result.replace('[', '').replace(']', '').split(','))))
