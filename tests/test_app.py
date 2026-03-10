import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_header_present():
    layout = app.layout
    header = layout.children[0]
    assert "Soul Foods Pink Morsel Sales Dashboard" in header.children


def test_graph_present():
    layout = app.layout
    graph_container = layout.children[3]
    graph = graph_container.children[0]
    assert graph.id == "sales-chart"


def test_region_picker_present():
    layout = app.layout
    filter_container = layout.children[2]
    radio = filter_container.children[1]
    assert radio.id == "region-filter"