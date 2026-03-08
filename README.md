# pytest-inline-tdd

A [pytest](http://pytest.org) plugin for **test-driven inline testing** — write tests *before* the code they verify, right inside your production source files.

## Motivation

### The Problem with Traditional Unit Tests

Traditional unit tests live in separate `test_*.py` files, isolated from production code. This creates several issues:

1. **Distance breeds neglect** — Tests and source code reside in different files (or directories), making it easy to forget updating tests after code changes.
2. **Coarse granularity** — Unit tests typically target entire functions or methods, lacking focused verification of individual statements within a function.
3. **Lost context** — Reading test code requires constant switching between test files and source files, making intent harder to follow.

### Original pytest-inline (Inline Testing)

[pytest-inline](https://github.com/EngineeringSoftware/pytest-inline) introduced the concept of **inline testing**: placing tests right next to the source code to directly verify a statement's output.

```python
# Original inline testing: test comes AFTER the statement under test
def example(a):
    b = a + 1
    itest().given(a, 1).check_eq(b, 2)  # Code first, test second
```

This solves the separation problem, but it is still a **code-first, test-later** workflow.

### pytest-inline-tdd: TDD Mode for Inline Testing

**pytest-inline-tdd** brings **Test-Driven Development (TDD)** to inline testing. The core idea:

> **Write the test (expectation) first, then write the implementation. Tests and code are tightly coupled in the same file, the same function.**

```python
# TDD inline testing: test comes BEFORE the statement under test
from inline_tdd import itestdd

def example(a):
    itestdd().given(a, 1).check_eq(b, 2)  # Test first: expect b=2 when a=1
    b = a + 1                              # Then implement
```

### Key Differences from Original pytest-inline

| Feature | pytest-inline | pytest-inline-tdd |
|---------|-------------|-------------------|
| Test position | **After** the statement under test | **Before** the statement under test |
| Workflow | Code first, test later | **Test first, code later (TDD)** |
| Package name | `inline` | `inline_tdd` |
| API name | `itest()` | `itestdd()` |
| Mindset | Verify already-written code | Declare expected behavior, then implement |
| Compatibility | Supports both pre/post modes | Supports both pre (TDD) and post modes |

## Use Cases

### 1. Statement-Level TDD

Write your expectation for a statement first, then implement it — testing and coding happen together:

```python
from inline_tdd import itestdd

def calculate_discount(price, rate):
    itestdd().given(price, 100).given(rate, 0.2).check_eq(discount, 20.0)
    discount = price * rate
    
    itestdd().given(price, 100).given(discount, 20.0).check_eq(final, 80.0)
    final = price - discount
    
    return final
```

### 2. Branch Verification for Complex Control Flow

Independently verify each branch of if/elif/else, for, and while statements:

```python
def classify(a):
    itestdd().given(a, 15).check_eq(b, "large")
    itestdd().given(a, 5).check_eq(b, "medium")
    itestdd().given(a, -1).check_eq(b, "small")
    if a > 10:
        b = "large"
    elif a > 0:
        b = "medium"
    else:
        b = "small"
```

### 3. Step-by-Step Data Pipeline Verification

Test each transformation step in place, ensuring every stage of a pipeline behaves as expected:

```python
import numpy as np
from inline_tdd import itestdd

def normalize(data):
    itestdd().given(data, np.array([2.0, 4.0, 6.0])).check_eq(m, 4.0)
    m = np.mean(data)
    
    itestdd().given(data, np.array([2.0, 4.0, 6.0])).given(m, 4.0).check_eq(
        centered.tolist(), [-2.0, 0.0, 2.0])
    centered = data - m
    
    return centered
```

### 4. Database Operation Verification

Inline tests work well for verifying the results of SQL queries and operations:

```python
import sqlite3
from inline_tdd import itestdd

def count_users(conn):
    itestdd().check_eq(n, 3)
    n = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    return n
```

### 5. Parameterized Tests

Cover multiple input-output pairs in a single statement:

```python
def double(a):
    itestdd(parameterized=True).given(a, [1, 2, 3]).check_eq(b, [2, 4, 6])
    b = a * 2
```

## Install

```bash
pip install pytest-inline-tdd
```

## Use

```bash
# Run all inline tests in the current directory
pytest .

# Run inline tests in a specific file
pytest path/to/file.py

# Run tests with a specific tag
pytest . --inline-group tag_name
```

## API

### Declaring an Inline Test

```python
itestdd(test_name, parameterized, repeated, tag, disabled, timeout)
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `test_name` | str | filename + line number | Name of the test |
| `parameterized` | bool | False | Whether the test is parameterized |
| `repeated` | int | 1 | Number of times to repeat the test |
| `tag` | list | [] | Tags for grouping and filtering |
| `disabled` | bool | False | Whether the test is disabled |
| `timeout` | float | -1.0 | Timeout in seconds (-1 for no limit) |

### Preconditions: assume

```python
itestdd().assume(condition).given(...).check_eq(...)
```

If `condition` is False, the test is skipped. Must appear before any `given()` calls, and only one `assume()` is allowed per test.

### Test Inputs: given

```python
itestdd().given(variable, value)
```

Multiple `given()` calls can be chained. Assigns test input values to variables used in the statement under test.

### Test Assertions: check_*

| Method | Description |
|--------|-------------|
| `check_eq(actual, expected)` | Equal |
| `check_neq(actual, expected)` | Not equal |
| `check_true(expr)` | Expression is true |
| `check_false(expr)` | Expression is false |
| `check_none(var)` | Value is None |
| `check_not_none(var)` | Value is not None |
| `check_same(a, b)` | Same object (`is`) |
| `check_not_same(a, b)` | Different objects |
| `fail()` | Force failure |

Only one check assertion is allowed per inline test.

## Stripping Inline Tests

When deploying to production, you can remove (comment) all `inline_tdd` related code (imports and `itestdd()` calls) from your source files using the built-in `strip-itestdd` command:

```bash
# Print cleaned code to stdout
strip-itestdd path/to/file.py

# Edit the file in-place
strip-itestdd path/to/file.py -i

# Write cleaned output to a new file
strip-itestdd path/to/file.py -o clean_file.py
```

You can also run it as a module:

```bash
python -m inline_tdd.strip path/to/file.py -i
```

**Before:**
```python
from inline_tdd import itestdd

def example(a):
    itestdd().given(a, 1).check_eq(b, 2)
    b = a + 1
    return b
```

**After:**
```python
# from inline_tdd import itestdd

def example(a):
    # itestdd().given(a, 1).check_eq(b, 2)
    b = a + 1
    return b
```

## Performance

Inline tests are fast — each test verifies only a single statement. In non-testing mode (i.e., normal production execution), all `itestdd()` calls behave as no-op function calls with negligible overhead.

## Citation

This project builds on the following research:

Title: [Inline Tests](https://dl.acm.org/doi/abs/10.1145/3551349.3556952)

Authors: [Yu Liu](https://sweetstreet.github.io/), [Pengyu Nie](https://pengyunie.github.io/), [Owolabi Legunsen](https://mir.cs.illinois.edu/legunsen/), [Milos Gligoric](http://users.ece.utexas.edu/~gligoric/)

```bibtex
@inproceedings{LiuASE22InlineTests,
  title =        {Inline Tests},
  author =       {Yu Liu and Pengyu Nie and Owolabi Legunsen and Milos Gligoric},
  pages =        {1--13},
  booktitle =    {International Conference on Automated Software Engineering},
  year =         {2022},
}
```

Title: [pytest-inline](https://pengyunie.github.io/p/LiuETAL23pytest-inline.pdf)

Authors: [Yu Liu](https://sweetstreet.github.io/), [Zachary Thurston](), [Alan Han](), [Pengyu Nie](https://pengyunie.github.io/), [Milos Gligoric](http://users.ece.utexas.edu/~gligoric/), [Owolabi Legunsen](https://mir.cs.illinois.edu/legunsen/)

```bibtex
@inproceedings{LiuICSE23PytestInline,
  title =        {pytest-inline: An Inline Testing Tool for Python},
  author =       {Yu Liu and Zachary Thurston and Alan Han and Pengyu Nie and Milos Gligoric and Owolabi Legunsen},
  pages =        {1--4},
  booktitle =    {International Conference on Software Engineering, DEMO},
  year =         {2023},
}
```
