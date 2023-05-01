from renderer.render import render


def test_render_list_result():
    assert render(["admin", "config", "local"]) == "admin\nconfig\nlocal"


def test_render_string():
    expected_output = "some string!"
    assert render(expected_output) == expected_output
