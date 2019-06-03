from nose.tools import assert_almost_equal, assert_raises


def mean(*args):
    if not len(args):
        raise TypeError('At least one argument required')
    return sum(args) / len(args)


def test_mean():
    """Test example mean calculation"""
    assert_almost_equal(
        mean(10, 15, 33, 24, 2),
        16.9,
    )


def test_mean_empty():
    """Test mean behaviour when empty list is given"""
    with assert_raises(TypeError):
        mean()
