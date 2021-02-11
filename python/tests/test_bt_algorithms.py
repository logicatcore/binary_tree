import pytest
from lib import heapify

class TestHeapify:
    def test_max_heapify(self):
        assert [3, 2, 1] == heapify.max_heapify([1, 2, 3]), "The max-heap property is not maintained"
        assert [10, 9, 7, 8, 5, 6, 3, 1, 4, 2] == heapify.max_heapify(list(range(1, 11))), "The max-heap property is not maintained"

    def test_min_heapify(self):
        assert [1, 2, 3] == heapify.min_heapify([3, 2, 1]), "The min-heap property is not maintained"
        assert [1, 2, 4, 3, 6, 5, 8, 10, 7, 9] == heapify.min_heapify(list(reversed(range(1, 11)))), "The min-heap property is not maintained"