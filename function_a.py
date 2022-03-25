def most_common_value(number_list):
    """ returns the most common element of the list
    """
    freq_dict = {}
    for num in number_list:
        if num not in freq_dict.keys():
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1

    highest_count_num = None
    num_count = 0
    for num, count in freq_dict.items():
        if count > num_count:
            highest_count_num = num
            num_count = count

    return highest_count_num


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
