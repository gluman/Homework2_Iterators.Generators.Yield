import types


def flat_generator(list_of_lists):
    count1 = 0

    item = None
    while count1 < len(list_of_lists):
        if type(list_of_lists[count1]) == list:
            for item in list_of_lists[count1]:
                yield item
            count1 += 1
        else:
            item = list_of_lists[count1]
            count1 += 1
            yield item


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()