from triangle import classify_triangle
import math

def test_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(0, 2, 3) == "Invalid"
    assert classify_triangle(-1, 2, 3) == "Invalid"

def test_equilateral_triangle():
    assert classify_triangle(3, 3, 3) == "Equalateral"
    assert classify_triangle(5, 5, 5) == "Equalateral"
    assert classify_triangle(10.123, 10.123, 10.123) == "Equalateral"

def test_isosceles_triangle():
    assert classify_triangle(3, 3, 4) == "Isocelese"
    assert classify_triangle(10.123, 10.123, 15.456) == "Isocelese"
    assert classify_triangle(1, 1, math.sqrt(2)) == "RightIsocelese"

def test_scalene_triangle():
    assert classify_triangle(3, 4, 5) == "RightScaline"
    assert classify_triangle(5, 6, 7) == "Scaline"
    assert classify_triangle(10.123, 15.456, 20.789) == "Scaline"

def test_satisfies_pythagorean_theorem():
    assert classify_triangle(3, 4, 5) == "RightScaline" or classify_triangle(3, 4, 5) == "RightIsocelese"