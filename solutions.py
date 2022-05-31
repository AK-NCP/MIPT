"""
Moscow Institute of Physics and Technology
Course: Computer Science. Algorithms and data structures in Python 3.
Lecturer: Timofey Fedorovich Hiryanov
read on 05.09.2017

Contest
"""


# |||||||||||||||||||||||1st semester, week 6|||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||Contest: Using Arrays||||||||||||||||||||||||||||||||||||||

# --------------------------|A|----------------------------------------------------

def input_string_num() -> str:
    string = input()
    return string


def affiliation_point_circle(string_num: str):
    """
    >>> print(affiliation_point_circle("-1 3 1"))
    NO
    >>> print(affiliation_point_circle("2 -7 8"))
    YES
    >>> print(affiliation_point_circle("2 -7 7"))
    NO
    """
    num_list = [float(num) for num in string_num.split(" ")]
    h = (float(num_list[0]) ** 2 + float(num_list[1]) ** 2) ** 0.5  # Pythagorean theorem
    return "NO" if h > float(num_list[2]) else "YES"


# --------------------------|B|----------------------------------------------------

def input_string_x_p_y() -> str:
    string = input()
    return string


def find_deposit_amount(string_num: str):
    """
    >>> find_deposit_amount("51 32 224")
    6
    >>> find_deposit_amount("100 10 200")
    8
    >>> find_deposit_amount("1 1 2")
    100
    """
    num_list = [float(num) for num in string_num.split(" ")]  # [x, p, y]
    years = 0
    while num_list[0] < num_list[2]:
        num_list[0] += (num_list[0] * (num_list[1] / 100))
        num_list[0] = int(num_list[0] * 100) / 100
        years += 1
    return years


# --------------------------|C|----------------------------------------------------


def input_n_binary_num() -> list:
    binary_num_list = []
    N = int(input())
    while N > 0:
        symbol = int(input())
        binary_num_list.append(symbol)
        N -= 1
    return binary_num_list


def find_maximum_one(binary_list: list):
    """
    >>> find_maximum_one([1, 1, 0, 1])
    2
    >>> find_maximum_one([0, 0, 0 , 0, 0, 0])
    0
    >>> find_maximum_one([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0])
    6
    """
    count = 0
    storage = 0
    for num in binary_list:
        if num == 1:
            count += 1
            if storage < count:
                storage = count
        elif num == 0:

            count = 0
    return storage


# --------------------------|D|----------------------------------------------------


def list_items(num_list):
    for num in num_list:
        yield num


def input_num(num_list_test: list):
    global next_num
    if num_list_test:
        if 'next_num' not in globals():
            next_num = list_items(num_list_test)
        num = next(next_num)
        if num == "#":
            del next_num
        return num

    else:
        num = input()
        return num


def summarize_numbers_array(num_list_test=None):
    """
    >>> print(*summarize_numbers_array([1, 2, 3, 4, 5, 6, "#"]))
    3.5 6 1 3
    >>> print(*summarize_numbers_array([2, 86, 34, 72, 91, 91, 10, 61, 57, 56, 83, 72, 96, 96, 23, 66, 86, 47, 56, 91, 32, 2, 98, 15, 94, 45, 84, 66, 19, 76, "#"]))
    60.233 98 2 285
    """
    result = {
        "average": 0,
        "maximum": float("-inf"),
        "minimum": float("inf"),
        "remainders": 0
    }
    count = 0
    triplet = 0
    while True:
        try:
            num = int(input_num(num_list_test))
            count += 1
            result["average"] += num
            if result["maximum"] < num:
                result["maximum"] = num
            if result["minimum"] > num:
                result["minimum"] = num
            triplet += num
            if count % 3 == 0:
                result["remainders"] += triplet % num
                triplet = 0
        except ValueError:
            result["average"] = round(result["average"] / count, 3)
            return result["average"], result["maximum"], result["minimum"], result["remainders"]


# --------------------------|E|----------------------------------------------------

def input_student_outcomes(num_list_test=None):
    student_outcomes_list = []
    temp_total_score = []
    data = "empty"
    number_of_students = 0
    while data:
        data = input_num(num_list_test)
        if not number_of_students and data != "#":
            number_of_students = int(data)
            temp_total_score = [[score] for score in range(number_of_students)]

        elif data != "#":
            student_outcomes_list.append([int(num) for num in data.split()])
            temp_total_score[student_outcomes_list[-1][0]][0] = 0
            student_outcomes_list[-1].append(temp_total_score[student_outcomes_list[-1][0]])  # editable list object

        else:
            data = False
    return number_of_students, student_outcomes_list


def find_total_score(number_of_students, student_outcomes_list):
    """
    >>> print(*find_total_score(*input_student_outcomes(["3", "0 3", "0 10", "2 3", "2 2", "2 4", "#"])))
    10 3 4 3 2
    >>> print(*find_total_score(*input_student_outcomes(["4", "3 7", "3 5", "3 5", "0 7", "0 8", "3 10", "0 6", "1 1", "2 9", "3 2", "#"])))
    10 7 5 5 2 8 7 6 9 1
    """
    for student, score, total_score in student_outcomes_list:
        total_score[0] += score
    student_outcomes_list.sort(key=lambda x: (-x[2][0], x[0], -x[1]), reverse=False)
    result = []
    for item in student_outcomes_list:
        result.append(item[1])
    return result


# --------------------------|F|----------------------------------------------------

def share_chocolate_bar(n: int) -> int:
    """
    >>> share_chocolate_bar(2)
    3
    >>> share_chocolate_bar(117)
    0
    >>> share_chocolate_bar(10)
    571
    """
    correctional, total, temp = 1, 3, 0
    if n % 2 == 1:
        total = 0
    else:
        for i in range(1, n // 2):
            temp = 4 * total - correctional
            correctional = total
            total = temp
    return total


# --------------------------|G|----------------------------------------------------
def input_str_num():
    list_str_num = []
    for i in range(2):
        if i % 2 == 0:
            list_str_num.append(input())
        else:
            list_str_num.append(int(input()))
    return list_str_num


def string_degree(list_data: list) -> str:
    """
    >>> print(string_degree(["aRrKUUeEDCQLWXlHRxCUqaYhWwQHjMdDOCzoYqiKVNHHYgvidE", -1]))
    aRrKUUeEDCQLWXlHRxCUqaYhWwQHjMdDOCzoYqiKVNHHYgvidE
    >>> print(string_degree(["abcd", -4]))
    NO SOLUTION
    >>> print(string_degree(["DkzvtzTgzqqVGqFhaXPNQVyDuzfFJPwyAlJGUKaOwcOlFnWcfZ", -8]))
    NO SOLUTION
    >>> print(string_degree(["abc", 3]))
    abcabcabc
    """
    flag = True
    if list_data[1] >= 0:
        return list_data[0] * list_data[1]
    elif len(list_data[0]) % list_data[1] != 0:
        return "NO SOLUTION"
    else:
        size = len(list_data[0]) // (-(list_data[1]))
        new_str = list_data[0][:size]
        for i in range(1, (-(list_data[1]))):
            for j in range(size):
                flag = (new_str[j] == list_data[0][j + size * i]) and flag
        return new_str if flag else "NO SOLUTION"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
