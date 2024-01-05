"""
Moscow Institute of Physics and Technology
Course: Computer Science. Algorithms and data structures in Python 3.
Lecturer: Timofey Fedorovich Hiryanov
read on 05.09.2017

Contest
"""


# |||||||||||||||||||||||1st semester, week 3|||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||Contest: 'if, for, while'||||||||||||||||||||||||||||||||||||||
# --------------------------|A|----------------------------------------------------

def input_int():
    n = int(input())
    return n


def find_sum_number(n: int) -> int:
    """
    >>> find_sum_number(179)
    17
    >>> find_sum_number(128)
    11
    >>> find_sum_number(101)
    2
     >>> find_sum_number(101452346237237346327327523573475)
     128
     >>> find_sum_number(0)
     0
     >>> find_sum_number(42)
     6
     >>> find_sum_number(7)
     7
    """
    divider = 10 ** (len(str(n)) - 1)
    sum_num = 0
    while divider:
        sum_num += (n // divider) % 10
        divider //= 10
    return sum_num


# --------------------------|B|----------------------------------------------------

def input_data_list():
    data_list = []
    for _ in range(4):
        data_list.append(int(input()))
    return data_list


def queen_move(data_list: list) -> str:
    """
    >>> print(queen_move([1, 1, 8, 8]))
    YES
    >>> print(queen_move([1, 1, 8, 1]))
    YES
    >>> print(queen_move([5, 5, 7, 4]))
    NO
    >>> print(queen_move([5, 3, 6, 7]))
    NO
    >>> print(queen_move([3, 4, 2, 5]))
    YES
    >>> print(queen_move([3, 8, 8, 5]))
    NO
    """
    if ((data_list[0] - data_list[2]) ** 2) == ((data_list[1] - data_list[3]) ** 2):
        result = 'YES'
    elif (data_list[0] - data_list[2]) == 0 or (data_list[1] - data_list[3]) == 0:
        result = 'YES'
    else:
        result = 'NO'
    return result


# --------------------------|C|----------------------------------------------------

def leap_year(year: int) -> str:
    """
    >>> print(leap_year(1))
    NO
    >>> print(leap_year(2000))
    YES
    >>> print(leap_year(400))
    YES
    >>> print(leap_year(9547))
    NO
    """
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        result = 'YES'
    else:
        result = 'NO'
    return result


# --------------------------|D|----------------------------------------------------


def find_list_squarest(num: int) -> list:
    """
    >>> print(*find_list_squarest(50))
    1 4 9 16 25 36 49
    >>> print(*find_list_squarest(16))
    1 4 9 16
    >>> print(*find_list_squarest(16))
    1 4 9 16
    >>> print(*find_list_squarest(101))
    1 4 9 16 25 36 49 64 81 100

    """
    list_squarest = []
    i = 1
    while i ** 2 <= num:
        list_squarest.append(i ** 2)
        i += 1
    return list_squarest


# --------------------------|E|----------------------------------------------------

def find_binary_logarithm(num: int) -> int:
    """
    >>> find_binary_logarithm(4)
    2
    >>> find_binary_logarithm(10)
    4
    >>> find_binary_logarithm(1627)
    11
    >>> find_binary_logarithm(8772)
    14
    """
    k = 0
    while num > 1:
        k += 1
        num = (num + 1) // 2
    return k


# --------------------------|F|----------------------------------------------------

def list_itemsv2(num_list):
    for num in num_list:
        yield num


def input_numv2(num_list_test: list = None, stopbit=None):  # TODO
    global next_numv2  # !!!!!!!!___critical place in the test___!!!!!!!!
    if stopbit:
        del next_numv2  # delete global value
        return '#'
    if num_list_test:
        if 'next_numv2' not in globals():  # create global value
            next_numv2 = list_itemsv2(num_list_test)
        num = next(next_numv2)
        return num
    else:
        num = input()
        return num


def sequence_length(num: list = None):
    """
    >>> sequence_length([1, 7, 9, 0, 5])
    3
    >>> sequence_length([29, 66, 76, 73, 14, 25, 40, 30, 40, 18, 53, 7, 44, 70, 63, 6, 19, 98, 41, 87, 47, 37, 12, 99, 31, 80, 90, 11, 30, 9, 14, 50, 93, 28, 76, 30, 90, 95, 56, 88, 47, 60, 59, 18, 79, 91, 45, 100, 22, 16, 61, 38, 69, 0, 77])
    53
    """
    k = 0
    while True:
        N = int(input_numv2(num))
        if not N:
            break
        k += 1
    if num:
        input_numv2(stopbit=True)  # Test stop
    return k


# --------------------------|G|----------------------------------------------------

def sum_entered_sequence(num: list = None):
    """
    >>> sum_entered_sequence([5, 3, 10, 0])
    18
    >>> sum_entered_sequence([17, -4, 0])
    13
    """
    k = 0
    while True:
        N = int(input_numv2(num))
        if not N:
            break
        k += N
    if num:
        input_numv2(stopbit=True)  # Test stop
    return k


# --------------------------|H|----------------------------------------------------

def number_even_elements(num: list = None):
    """
    >>> number_even_elements([1, 2, 0])
    1
    >>> number_even_elements([1, -1, 0])
    0
    >>> number_even_elements([35, 37, -39, -10, -48, 2, 33, -31, -43, -3, 9, 2, -18, -8, -2, 17, 13, 24, 33, 32, 47, -10, 43, 21, -29, 0])
    10
    """
    k = 0
    while True:
        N = int(input_numv2(num))
        if not N:
            break
        if N % 2 == 0:
            k += 1
    if num:
        input_numv2(stopbit=True)  # Test stop
    return k


# --------------------------|I|----------------------------------------------------

def maximum_sequence(num: list = None):
    """
    >>> maximum_sequence([1, 7, 9, 0])
    9
    >>> maximum_sequence([5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 5957, 0])
    5957
    >>> maximum_sequence([28, 82, 50, 10, 32, 91, 85, 36, 7, 23, 15, 68, 83, 52, 41, 87, 25, 24, 50, 91, 96, 19, 81, 46, 98, 48, 66, 70, 93, 81, 77, 79, 33, 33, 80, 60, 53, 47, 61, 25, 99, 0])
    99
    """
    max_num = float("-inf")
    while True:
        N = int(input_numv2(num))
        if not N:
            break
        if max_num < N:
            max_num = N
    if num:
        input_numv2(stopbit=True)  # Test stop
    return max_num


# --------------------------|J|----------------------------------------------------

def number_elements_equal_maximum(num: list = None):
    """
    >>> number_elements_equal_maximum([1, 7, 9, 0])
    1
    >>> number_elements_equal_maximum([1, 3, 3, 1, 0])
    2
    >>> number_elements_equal_maximum([87, 79, 56, 99, 19, 63, 71, 13, 45, 29, 135, 103, 82, 140, 48, 100, 38, 92, 96, 131, 140, 65, 66, 119, 105, 140, 0])
    3
    """
    max_num = float("-inf")
    k = 0
    while True:
        N = int(input_numv2(num))
        if not N:
            break
        if max_num < N:
            max_num = N
            k = 1
        elif max_num == N:
            k += 1
    if num:
        input_numv2(stopbit=True)  # Test stop
    return k


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


def input_num(num_list_test: list):  # TODO
    global next_num  # !!!!!!!!___critical place in the test___!!!!!!!!
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

# |||||||||||||||||||||||1st semester|||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# |||||||||||||||||||||||Контест: использование массивов||||||||||||||||||||||||||||||||||||||
# --------------------------|A|----------------------------------------------------

def delivery(data_list: list) -> str:
    """
    >>> print(delivery([1, 1, 5, 10, 5, 10, 11, 11]))
    YES
    >>> print(delivery([1, 1, 5, 10, 5, 10, 5, 11]))
    NO
    >>> print(delivery([1, 1, 5, 10, 5, 10, 10, 11]))
    YES
    >>> print(delivery([1, 1, 11, 10, 5, 7, 11, 11]))
    NO
    """
    truck_weight_without_load = int(data_list[0])
    platform_height = int(data_list[1])
    piano_weight = int(data_list[2])
    piano_height = int(data_list[3])
    refrigerator_weight = int(data_list[4])
    refrigerator_height = int(data_list[5])
    max_permissible_weight_bridge = int(data_list[6])
    max_permissible_height_tunnel = int(data_list[7])
    weight_all = 0
    refrigerator_platform_height = 0
    piano_platform_height = 0
    institute = False
    dormitories = False
    
    weight_all = (truck_weight_without_load +\
                piano_weight +\
                refrigerator_weight)  
    
    refrigerator_platform_height = platform_height + refrigerator_height
    piano_platform_height = platform_height + piano_height
    
    if (refrigerator_platform_height <= max_permissible_height_tunnel and
      piano_platform_height <= max_permissible_height_tunnel):
    institute = True
    
    elif(weight_all <= max_permissible_weight_bridge and
       refrigerator_platform_height <= max_permissible_height_tunnel):
    institute = True
    
    
    if weight_all <= max_permissible_weight_bridge:
    dormitories = True
    
    elif (weight_all - refrigerator_weight <= max_permissible_weight_bridge):
    dormitories = True
    
    if institute and dormitories:
    return print('YES')
    else:
    return print('NO')



if __name__ == "__main__":
    import doctest

    doctest.testmod()
