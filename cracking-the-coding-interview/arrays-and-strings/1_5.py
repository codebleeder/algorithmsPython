__author__ = 'cloudera'


def compress_bad(input_str):
    my_str = []
    input_str_list = list(input_str)
    last = 0
    count = 1
    for i in range(1, len(input_str_list)):
        if input_str_list[i] == input_str_list[last]:
            count += 1
        else:
            my_str.append(input_str_list[last]+str(count))
            count = 1
            last = i
    my_str.append(input_str_list[last]+str(count))
    my_str = ''.join(my_str)
    if len(input_str) <= len(my_str):
        return input_str
    else:
        return ''.join(my_str)


def get_size_compressed(input_str_list):
    last = ''
    count = 1
    size = 0
    for i in input_str_list:
        if i == last:
            count += 1
        else:
            size += 1 + len(str(count))
            count = 1
            last = i
    return size


def compress_good(input_str):
    input_str_list = list(input_str)
    size_compressed = get_size_compressed(input_str_list)
    if size_compressed < len(input_str):
        compressed = []
        last = ''
        count = 1
        for i in input_str_list:
            if i == last:
                count += 1
            else:
                last = i
                compressed.append(last+str(count))
                count = 1
        compressed.append(last+str(count))
        return ''.join(compressed)
    else:
        return input_str

test_input = ['sharad', 'shaarad', 'aaabbbccc']
for i in test_input:
    print compress_good(i)
