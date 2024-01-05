from rules_engine import Variable


def test_equals():
    rule = Variable('foo') == Variable('bar')
    bar = 50
    assert not rule(dict(foo=51, bar=bar))
    assert rule(dict(foo=50, bar=bar))
    assert not rule(dict(foo=49, bar=bar))


def test_not_equals():
    rule = Variable('foo') != Variable('bar')
    bar = 50
    assert rule(dict(foo=51, bar=bar))
    assert not rule(dict(foo=50, bar=bar))
    assert rule(dict(foo=49, bar=bar))


def test_greater_than():
    rule = Variable('foo') > Variable('bar')
    bar = 50
    assert rule(dict(foo=51, bar=bar))
    assert not rule(dict(foo=50, bar=bar))
    assert not rule(dict(foo=49, bar=bar))


def test_greater_than_or_equal_to():
    rule = Variable('foo') >= Variable('bar')
    bar = 50
    assert rule(dict(foo=51, bar=bar))
    assert rule(dict(foo=50, bar=bar))
    assert not rule(dict(foo=49, bar=bar))


def test_less_than():
    rule = Variable('foo') < Variable('bar')
    bar = 50
    assert not rule(dict(foo=51, bar=bar))
    assert not rule(dict(foo=50, bar=bar))
    assert rule(dict(foo=49, bar=bar))


def test_less_than_or_equal_to():
    rule = Variable('foo') <= Variable('bar')
    bar = 50
    assert not rule(dict(foo=51, bar=bar))
    assert rule(dict(foo=50, bar=bar))
    assert rule(dict(foo=49, bar=bar))
