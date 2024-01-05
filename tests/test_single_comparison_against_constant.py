from rules_engine import Variable


def test_equals():
    rule = Variable('foo') == 50
    assert not rule(dict(foo=51))
    assert rule(dict(foo=50))
    assert not rule(dict(foo=49))


def test_not_equals():
    rule = Variable('foo') != 50
    assert rule(dict(foo=51))
    assert not rule(dict(foo=50))
    assert rule(dict(foo=49))


def test_greater_than():
    rule = Variable('foo') > 50
    assert rule(dict(foo=51))
    assert not rule(dict(foo=50))
    assert not rule(dict(foo=49))


def test_greater_than_or_equal_to():
    rule = Variable('foo') >= 50
    assert rule(dict(foo=51))
    assert rule(dict(foo=50))
    assert not rule(dict(foo=49))


def test_less_than():
    rule = Variable('foo') < 50
    assert not rule(dict(foo=51))
    assert not rule(dict(foo=50))
    assert rule(dict(foo=49))


def test_less_than_or_equal_to():
    rule = Variable('foo') <= 50
    assert not rule(dict(foo=51))
    assert rule(dict(foo=50))
    assert rule(dict(foo=49))
