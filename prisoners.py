import random
import matplotlib.pyplot as plt

def is_success(prisoner_num):
    box = random.sample(range(prisoner_num), prisoner_num)
    visited = set()

    """
    1. 상자 안에 적힌 번호의 상자로 이동한다(첫 선택은 자신의 번호)
    2. 해당 상자를 연다.
    3. 상자 안의 번호를 본다.
        3-1. 상자 안의 번호가 자신의 번호와 일치하면 종료.
        3-2. 상자 안의 번호가 자신의 번호와 일치하지 않으면 1번으로 이동.
    """
    for prisoner in range(prisoner_num):
        is_find = False
        if prisoner in visited:
            continue
        choice_num = prisoner
        for _ in range(prisoner_num // 2):
            visited.add(choice_num)
            choice_num = box[choice_num]
            if choice_num == prisoner:
                is_find = True
                break
        if not is_find:
            return 0
    return 1

def get_probability(try_num: int, num: int):
    success = 0
    y_range = [((success:=success+is_success(num))/(i+1))*100 for i in range(try_num)]

    print("\n==========결과==========")
    print(f"성공 횟수: {success}")
    print(f"확률: {(success / try_num) * 100}%")

    plt.plot(range(try_num), y_range)
    plt.show()

if __name__ == "__main__":
    a = ""
    while True:
        try:
            try_num = int(input(f"시행할 횟수를 입력하세요{a}: "))
            if try_num <= 0:
                raise ValueError
            a = ""
            break
        except ValueError:
            a = "(양의 숫자만 입력해 주세요!)"

    while True:
        try:
            prisoner_num = int(input(f"죄수 인원을 입력하세요{a}: "))
            if prisoner_num <= 0:
                raise ValueError
            break
        except ValueError:
            a = "(양의 숫자만 입력해 주세요!)"
    get_probability(try_num, prisoner_num)
