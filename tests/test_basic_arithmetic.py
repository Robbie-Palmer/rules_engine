from rules_engine import Variable


def test_add():
    rule = (Variable('foo') + 10) > 60
    assert rule(dict(foo=51))
    assert not rule(dict(foo=50))

    rule = (Variable('foo') + Variable('bar')) > 60
    assert rule(dict(foo=61, bar=0))
    assert not rule(dict(foo=60, bar=0))
    assert rule(dict(foo=60, bar=1))

    rule = (Variable('foo') + 10) > Variable('bar')
    bar = 60
    assert rule(dict(foo=51, bar=bar))
    assert not rule(dict(foo=50, bar=bar))
    assert not rule(dict(foo=49, bar=bar))


def test_subtract():
    rule = (Variable('foo') - 10) > 40
    assert rule(dict(foo=51))
    assert not rule(dict(foo=50))

    rule = (Variable('foo') - Variable('bar')) > 60
    assert rule(dict(foo=61, bar=0))
    assert not rule(dict(foo=61, bar=1))

    rule = (Variable('foo') - 10) > Variable('bar')
    bar = 40
    assert rule(dict(foo=51, bar=bar))
    assert not rule(dict(foo=50, bar=bar))


def test_multiply():
    rule = (Variable('foo') * 10) >= 100
    assert rule(dict(foo=11))
    assert rule(dict(foo=10))
    assert not rule(dict(foo=9))

    rule = (Variable('foo') * Variable('bar')) >= 100
    assert rule(dict(foo=20, bar=5))
    assert not rule(dict(foo=9, bar=10))

    rule = (Variable('foo') * 10) >= Variable('bar')
    bar = 100
    assert rule(dict(foo=10, bar=bar))
    assert not rule(dict(foo=9, bar=bar))


def test_divide():
    rule = (Variable('foo') / 10) >= 10
    assert rule(dict(foo=110))
    assert rule(dict(foo=100))
    assert not rule(dict(foo=99))

    rule = (Variable('foo') / Variable('bar')) >= 10
    assert rule(dict(foo=100, bar=5))
    assert not rule(dict(foo=81, bar=9))

    rule = (Variable('foo') / 10) >= Variable('bar')
    bar = 10
    assert rule(dict(foo=100, bar=bar))
    assert not rule(dict(foo=99, bar=bar))


def test_integer_division():
    rule = (Variable('foo') // 2) == 2
    assert rule(dict(foo=5))
    assert not rule(dict(foo=6))


def test_modulo():
    rule = (Variable('foo') % 3) == 2
    assert rule(dict(foo=8))
    assert not rule(dict(foo=9))


def test_power():
    rule = (Variable('foo') ** 2) == Variable('bar')
    assert rule(dict(foo=2, bar=4))
    assert rule(dict(foo=3, bar=9))
    assert not rule(dict(foo=4, bar=15))
