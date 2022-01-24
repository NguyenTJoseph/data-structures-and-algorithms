from graphs import Graph

def test_graph_depth1():
    gr = Graph()
    a = gr.add_node("a")
    b = gr.add_node("b")
    gr.add_edge(a, b)
    actual = gr.depth_first(a)
    expected = [a, b]
    assert expected == actual

def test_graph_depth2():
    gr = Graph()
    a = gr.add_node("a")
    b = gr.add_node("b")
    c = gr.add_node("c")
    d = gr.add_node("d")
    gr.add_edge(a, b)
    gr.add_edge(b, c)
    gr.add_edge(b, d)
    actual = gr.depth_first(a)
    expected = [a, b, c, d]
    assert expected == actual

def test_graph_depth3():
    gr = Graph()
    a = gr.add_node("a")
    b = gr.add_node("b")
    c = gr.add_node("c")
    d = gr.add_node("d")
    e = gr.add_node("e")
    f = gr.add_node("f")
    g = gr.add_node("g")
    h = gr.add_node("h")
    gr.add_edge(a, b)
    gr.add_edge(a, d)
    gr.add_edge(b, c)
    gr.add_edge(b, d)
    gr.add_edge(c, g)
    gr.add_edge(d, e)
    gr.add_edge(d, h)
    gr.add_edge(d, f)


    gr.add_edge(f, h)
    actual = gr.depth_first(a)
    expected = [a, b, c, g, d, e, h, f]
    assert expected == actual


