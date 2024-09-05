from poorlib.utils.list_utils import split_list

# Test when the input list is empty
def test_empty_list():
    items = []
    result = list(split_list(items, batch=5))
    assert result == [[]]

# Test when the input list size is exactly divisible by the batch size
def test_exact_batch_size():
    items = [1, 2, 3, 4, 5, 6]
    result = list(split_list(items, batch=2))
    assert result == [[1, 2], [3, 4], [5, 6]]

# Test when the input list size is smaller than the batch size
def test_smaller_than_batch():
    items = [1, 2, 3]
    result = list(split_list(items, batch=5))
    assert result == [[1, 2, 3]]

# Test when the input list size is not exactly divisible by the batch size
def test_non_exact_batch_size():
    items = [1, 2, 3, 4, 5]
    result = list(split_list(items, batch=3))
    assert result == [[1, 2, 3], [4, 5]]

# Test when the input batch size is larger than the list
def test_large_batch_size():
    items = [1, 2, 3]
    result = list(split_list(items, batch=10))
    assert result == [[1, 2, 3]]