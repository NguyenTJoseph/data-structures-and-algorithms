from stack_queue_bracket import validate_brackets

def test_validate_brackets1():
    string = "{}"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_validate_brackets2():
    string = "{}(){}"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_validate_brackets3():
    string = "()[[Extra Characters]]"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_validate_brackets4():
    string = "(){}[[]]"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_validate_brackets5():
    string = "{}{Code}[Fellows](())"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_validate_brackets6():
    string = "[({}]"
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

def test_validate_brackets7():
    string = "(]("
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

def test_validate_brackets8():
    string = "{(})"
    actual = validate_brackets(string)
    expected = False
    assert actual == expected
