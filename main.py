import types
import os
import datetime

def logger(old_function):
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)
    def new_function(*args, **kwargs):

        result = old_function(*args, **kwargs)
        log_text =f"name func: {old_function.__name__}; " \
                  f"date: {datetime.date.today()}; " \
                  f"time: {datetime.datetime.now().time().strftime('%H:%M:%S')}; " \
                  f"*args: {args}; " \
                  f"**kwargs: {kwargs}; " \
                  f"result: {result}; " \
                  f"\n"

        with open(path, 'a') as f:
            f.writelines(log_text)

        return result

    return new_function

@logger
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


@logger
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