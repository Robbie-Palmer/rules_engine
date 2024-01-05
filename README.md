# Rules Engine

A rules engine to process risk submissions to apply segment tags to evaluate insurance opportunities.
Define rules as variables and constants chained by comparisons.

NOTE: The parsing of the Domain Specific Language (DSL) is missing from this implementation.
This project implements only the underlying semantic model and the engine to run submissions through it.

## Usage

- Install the package `pip install .`
- Create a script in which you define and apply your rules, leveraging the imported rules engine
e.g. The pseudocode below is translated to the rule in the python script, and has a risk submission applied:
```
Either:
  credit_rating is above 50
  AND
  flood_risk is below 10
OR
  revenue is above 1000000
```
Can be expressed and evaluated as:
```python
from rules_engine import Variable

EXAMPLE_1 = {
    "credit_rating": 75,
    "flood_risk": 5,
    "revenue": 1000
}
rule = (Variable('credit_rating') > 50) & (Variable('flood_risk') < 10) | (Variable('revenue') > 1_000_000)
rule(EXAMPLE_1)
```

## Assumptions

- All rules must have 1+ variables. It does not make sense to have a rule of only constants which is itself a constant.
- All values are numbers (constants and values of variables).
- All variables map to primitive numbers. There are no complex objects with nested properties.
- A user cannot evaluate the "truthiness" of a variable, they must provide an explicit comparison
  - E.g. They can do: `credit_rating is above 0 AND flood_risk is below 10`
  but they cannot do: `credit_rating AND flood_risk is below 10`
- A user can execute arithmetic against variables e.g. by adding variables together or altering them via constants
  - E.g. `credit_rating PLUS flood_risk is below 15`
  - E.g. `credit_rating PLUS 20 is below flood_risk`
- Missing values are invalid and should throw an error. There are no defaults.
- The rules are self-contained. There is no assignment to new variables which could trigger follow on rules 
via forward chaining.

## Developer Setup

- Create a Python environment. Recommended installation:
    - Install [Miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
    - Create a new python environment `conda create -n rule_engine python=3.10`
    - Active your environment `conda activate rule_engine`
- Install the package in editable mode `pip install -e .`

## Test

- Install the test dependencies `pip install -r ./tests/requirements.txt`
- Run tests `python -m pytest ./tests`
