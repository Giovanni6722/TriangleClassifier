from triangle import classify_triangle
import math

def test_studio_orders_are_classified_correctly():

    #buildable sides should return the correct shape
    assert classify_triangle(5, 5, 5) == "Equilateral"
    assert classify_triangle(5, 5, 8) == "Isosceles"
    assert classify_triangle(5, 6, 7) == "Scalene"

    #bad inputs should return invalid to prevent customers from 
    #building a peice that is impossible
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(0, 2, 3) == "Invalid"

    #pythagorean theorem should prefix resutls
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Isosceles"