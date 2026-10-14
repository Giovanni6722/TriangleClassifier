An equalateral triangle can't be a right triangle, because 
an equalateral triangle can only have angles of 60 degrees

Copilot review log:

Test: test_invalid_triangle
Copilot suggested?: Yes
Edited
Copilot kept thinking that I had a triangle class and kept trying to
call triangle as an object. It's not an object. Once I wrote one assertion
it understood the context and gave me two more cases to test with it.

Test: test_equilateral_triangle
Copilot suggested?: Yes
Edited
Most cases were fine but it wasn't testing decimals, so I added that assertion myself

Test: test_isosceles_triangle
Copilot suggested?: Yes
Edited
Again cases were fine and it added it's own floating point test, but I also wanted to test
right triangles too so I added that assertion msyelf

Test: test_scalene_triangle
Copilot suggested?: Yes
Kept
With all the context from past tests it understood what to look for and wrote all 3 cases of
whole number test, floating point test, and right triangle test

Test: test_satisfies_pythagorean_theorem
Copilot suggested?: Yes
Rejected
It kept trying to make this unit test with paramaters? When I wrote the name of the function
it was just freaking out so I wrote it myself.