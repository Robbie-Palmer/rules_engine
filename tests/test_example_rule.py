from pytest_cases import parametrize_with_cases, THIS_MODULE, parametrize

from rules_engine import Variable


@parametrize(low_credit_rating=(50, 0), high_flood_risk=(10, 100))
def case_high_revenue_overrules_credit_rating_and_flood_risk(low_credit_rating, high_flood_risk):
    return dict(credit_rating=low_credit_rating, flood_risk=high_flood_risk, revenue=10_000_000), True


def case_low_revenue_but_high_credit_rating_and_low_flood_risk():
    return dict(credit_rating=100, flood_risk=9, revenue=1000), True


def case_low_revenue_and_high_flood_risk_rules_out():
    return dict(credit_rating=100, flood_risk=10, revenue=1000), False


def case_low_revenue_and_low_credit_rating_rules_out():
    return dict(credit_rating=50, flood_risk=0, revenue=1000), False


@parametrize_with_cases('data,expected', cases=THIS_MODULE)
def test_example_rule(data: dict, expected: bool):
    rule = (Variable('credit_rating') > 50) & (Variable('flood_risk') < 10) | (Variable('revenue') > 1_000_000)
    actual = rule(data)
    assert actual == expected
