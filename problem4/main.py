def find_max_sum_sub_array(k, arr):
    max_sum = 0
    step_sum = 0

    for index in range(len(arr) - k):
        window_len = index + k
        select_elements = arr[index:window_len]

        step_sum = sum(select_elements)
        max_sum = max(step_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2]))  # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5]))  # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1]))  # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1]))  # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1]))  # 8
