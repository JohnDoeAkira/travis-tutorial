import numpy
import numpy.random

def test_addition():
    assert 1 + 1 == 2
    
def test_True():
    assert 1 == 1
    
def test_division():
    assert 3/2 == 1.5

def test_partition():
    array_test = numpy.random.randint(20, size=10)
    k_ind = 10
    array_part = numpy.partition(array_test, 10)
    
    for v in array_part[:k_ind]:
        assert v < array_test[k_ind]
