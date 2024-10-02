import pytest
from dataclasses import dataclass
from typing import List
from poorlib.utils.list_utils import ListSplitter  # Replace 'your_module' with the actual module name where ListSplitter is defined.

# Define a sample dataclass for testing
@dataclass
class BatchItem:
    items: List[int]

# Test data
items = list(range(10005))  # A list with 10005 elements

def test_splitter_plain_list():
    """Test that the splitter returns plain lists when as_object=False"""
    splitter = ListSplitter(items, batch=1000, as_object=False)
    result = list(splitter)  # Convert the generator to a list of batches

    assert len(result) == 11  # 10 full batches of 1000, and 1 batch of 5 items
    assert result[0] == list(range(1000))  # First batch
    assert result[-1] == list(range(10000, 10005))  # Last batch

def test_splitter_with_dataclass():
    """Test that the splitter returns dataclass objects when as_object=True"""
    splitter = ListSplitter(items, batch=1000, as_object=True, dataclass_type=BatchItem)
    result = list(splitter)  # Convert the generator to a list of batches

    assert len(result) == 11  # 10 full batches of 1000, and 1 batch of 5 items
    assert isinstance(result[0], BatchItem)  # Ensure it's returning the dataclass
    assert result[0].items == list(range(1000))  # Check the contents of the first batch
    assert result[-1].items == list(range(10000, 10005))  # Check the contents of the last batch

def test_empty_list():
    """Test behavior when an empty list is passed"""
    splitter = ListSplitter([], batch=1000, as_object=False)
    result = list(splitter)

    assert result == []  # Should return an empty list

def test_batch_size_larger_than_list():
    """Test when batch size is larger than the list length"""
    splitter = ListSplitter(items, batch=20000, as_object=False)
    result = list(splitter)

    assert len(result) == 1  # Should be only one batch
    assert result[0] == items  # The single batch should contain all items

def test_invalid_dataclass_type():
    """Test that a ValueError is raised when as_object=True and no dataclass_type is provided"""
    with pytest.raises(ValueError):
        splitter = ListSplitter(items, batch=1000, as_object=True)
        next(iter(splitter))  # Attempt to iterate

def test_batch_items_in_order():
    """Test that batch items are split correctly in order"""
    splitter = ListSplitter(items, batch=500, as_object=False)
    result = list(splitter)

    assert len(result) == 21  # 20 full batches of 500, and 1 batch of 5 items
    for i in range(20):
        assert result[i] == list(range(i * 500, (i + 1) * 500))  # Check each batch
    assert result[-1] == list(range(10000, 10005))  # Check the last batch

# Run this test with pytest
