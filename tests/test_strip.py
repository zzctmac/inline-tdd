from inline_tdd.strip import strip_source


def test_strip_comments_import_and_call_without_removing_lines():
    source = (
        "from inline_tdd import itestdd\n"
        "\n"
        "def add(a, b):\n"
        "    return a + b\n"
        "\n"
        "itestdd().given(1, 2).check_eq(add, 3)\n"
        "\n"
        "x = 10\n"
    )

    result = strip_source(source)

    assert "# from inline_tdd import itestdd\n" in result
    assert "# itestdd().given(1, 2).check_eq(add, 3)\n" in result
    assert "\n\n\n" not in result


def test_strip_keeps_blank_lines_blank_for_multiline_call():
    source = (
        "from inline_tdd import itestdd\n"
        "\n"
        "itestdd(\n"
        ").given(1, 2).check_eq(\n"
        "\n"
        "    lambda a, b: a + b,\n"
        "    3,\n"
        ")\n"
        "\n"
        "x = 10\n"
    )

    result = strip_source(source)
    lines = result.splitlines()

    # The internal blank line in the multiline call should stay blank, not become '# '.
    assert lines[4] == ""
    assert "\n# \n" not in result


def test_strip_is_idempotent_on_already_commented_lines():
    source = (
        "# from inline_tdd import itestdd\n"
        "\n"
        "# itestdd().given(1, 2).check_eq(lambda a, b: a + b, 3)\n"
        "\n"
        "x = 10\n"
    )

    result = strip_source(source)

    assert result == source


def test_strip_comments_import_and_call_without_removing_lines_1():
    source = (
        "from inline_tdd import itestdd\n"
        "\n"
        "def add(a, b):\n"
        "    itestdd().given(1, 2).check_eq(add, 3)\n"
        "    result = a + b\n"
        "    return result"
    )

    result = strip_source(source)
    print(result)

    assert result[-1] != "\n"