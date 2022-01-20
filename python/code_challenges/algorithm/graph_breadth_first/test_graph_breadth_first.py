from graph import Graph


def test_graph_breadth_first1():
    g = Graph()
    a = g.add_node("a")
    b = g.add_node("b")
    g.add_edge(a, b)
    actual = g.breadth_first(a)
    expected = [a, b]
    assert expected == actual

def test_graph_breadth_first2():
    g = Graph()
    a = g.add_node("a")
    b = g.add_node("b")
    c = g.add_node("c")
    d = g.add_node("d")
    g.add_edge(a, b)
    g.add_edge(b, c)
    g.add_edge(b, d)
    actual = g.breadth_first(a)
    expected = [a, b, c, d]
    assert expected == actual

def test_graph_breadth_first3():
    g = Graph()
    a = g.add_node("a")
    b = g.add_node("b")
    c = g.add_node("c")
    d = g.add_node("d")
    e = g.add_node("e")
    f = g.add_node("f")
    g.add_edge(a, b)
    g.add_edge(b, c)
    g.add_edge(b, d)
    g.add_edge(c, e)
    g.add_edge(c, f)
    g.add_edge(d, f)
    actual = g.breadth_first(a)
    expected = [a, b, c, d, e, f]
    assert expected == actual
