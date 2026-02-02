def test_layout(dash_duo):
    from app import app
    dash_duo.start_server(app)
    
    # Header
    header = dash_duo.wait_for_element("#header")
    assert "Pink Morsel sales - January 2021" in header.text
    
    # Radio
    radio = dash_duo.wait_for_element("#region-radio")
    assert radio is not None
    
    # Graph
    graph = dash_duo.wait_for_element("#visual_graph")
    assert graph is not None
