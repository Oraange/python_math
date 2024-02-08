"""
The drunk passenger problem

문제: 
    비행기에 100개의 좌석이 있고 100명의 사람이 비행기에 타려고 한다.
    100개의 좌석에는 각각 1부터 100까지의 숫자가 적혀있고 승객들은 탑승 순서대로
    1번부터 100번까지 착석하면 된다.

    그런데, 첫번째 승객은 만취자여서 자신의 자리를 찾지 못하고 아무 좌석에 앉아버렸다.
    첫번째 승객을 제외한 나머지 승객은 각자 자신의 자리에 맞게 착석을 한다.
    하지만 자신의 자리에 누군가 앉아있을 경우 해당 승객은 남은 좌석 중 랜덤한 자리에 앉는다.

    이렇게 100명 모두 자리에 앉았을 때,
    마지막 100번째 승객이 자신이 원래 앉아야 할 자리(100번 자리)에 앉을 수 있는 확률은 얼마일까?

해결:
    100명의 승객
"""

import collections
from multiprocessing import Pool
from random import choice

def get_drunk_passenger():
    passengers = [False] * 100
    remain_seats = [i for i in range(100)]

    for psngr in range(len(passengers) - 1):
        # 좌석 선택:
        #     0번(첫번째 사람: 취한 사람)이거나 자리에 이미 앉아있는 경우 랜덤 좌석에 착석
        choice_num = choice(remain_seats) if not psngr or passengers[psngr] else psngr
        passengers[choice_num] = True
        remain_seats.remove(choice_num)

    return remain_seats[0] == 99

def main_with_process():
    with Pool(4) as pool:
        result = pool.starmap_async(get_drunk_passenger, [() for _ in range(int(1e6))])
        print(f"결과: {dict(collections.Counter(result.get()))}")

if __name__ == "__main__":
    main_with_process()
