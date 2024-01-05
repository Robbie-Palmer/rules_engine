from rules_engine import Variable


def test_and():
    first_rule = Variable('foo') > 0
    second_rule = Variable('bar') > 0
    rule = first_rule & second_rule

    both_false_data = dict(foo=0, bar=0)
    assert not rule(both_false_data)
    first_true_data = dict(foo=1, bar=0)
    assert not rule(first_true_data)
    second_true_data = dict(foo=0, bar=1)
    assert not rule(second_true_data)
    both_true_data = dict(foo=1, bar=1)
    assert rule(both_true_data)


def test_or():
    first_rule = Variable('foo') > 0
    second_rule = Variable('bar') > 0
    rule = first_rule | second_rule

    both_false_data = dict(foo=0, bar=0)
    assert not rule(both_false_data)
    first_true_data = dict(foo=1, bar=0)
    assert rule(first_true_data)
    second_true_data = dict(foo=0, bar=1)
    assert rule(second_true_data)
    both_true_data = dict(foo=1, bar=1)
    assert rule(both_true_data)


def test_xor():
    first_rule = Variable('foo') > 0
    second_rule = Variable('bar') > 0
    rule = first_rule ^ second_rule

    both_false_data = dict(foo=0, bar=0)
    assert not rule(both_false_data)
    first_true_data = dict(foo=1, bar=0)
    assert rule(first_true_data)
    second_true_data = dict(foo=0, bar=1)
    assert rule(second_true_data)
    both_true_data = dict(foo=1, bar=1)
    assert not rule(both_true_data)
