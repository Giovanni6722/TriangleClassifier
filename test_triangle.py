from triangle import classify_triangle

def test_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"