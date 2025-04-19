from vereshchagin_figures import Rectangle, TriangleLeft, TriangleRight, Parabola, ParabolicTrapezoid, Trapezoid
from vereshchagin_visualise import VereshchaginVisualiser

# Example I
# Integrating a rectangle and a left triangle (with height 0 at the right end and 2 at the left), both spanning length 5

# Create a rectangle
rectangle = Rectangle(
    x=5,        # length of the base
    height=3    # constant height across the entire base
)

# Create a left triangle (maximum height on the left, zero at the right)
triangle_left = TriangleLeft(
    x=5,        # length of the base
    height=2    # maximum height on the left edge
)

# Initialize the visualizer
visualiser = VereshchaginVisualiser()

# Display individual figures
visualiser.draw_figure(rectangle)
visualiser.draw_figure(triangle_left)

# Or visualize both figures together in one diagram
visualiser.draw_situation(rectangle, triangle_left)

# Compute the integral of both figures
result = rectangle + triangle_left

# Output the result
print(f"Integration result: {result}")

################################################

# Example II
# Integrating a parabolic trapezoid and a trapezoid — both spanning the same length

# Create a parabolic trapezoid (combination of trapezoid and parabolic curvature)
parab_trap = ParabolicTrapezoid(
    x=4,                 # length
    height_left=3,       # left height of the trapezoid part
    height_right=1.5,    # right height of the trapezoid part
    line_load=-2         # intensity of the parabolic load (negative means curvature faces downward)
)

# Create a simple trapezoid
trapezoid = Trapezoid(
    x=4,
    height_left=2,
    height_right=4
)

# Visualize the individual figures
visualiser.draw_figure(parab_trap)
visualiser.draw_figure(trapezoid)

# Visualize the combined interaction
visualiser.draw_situation(parab_trap, trapezoid)

# Compute the integral
result = parab_trap + trapezoid

# Output the result
print(f"Integration result: {result}")

###################################################
# Example III
# Combining multiple integrals

# To add multiple integration results together, wrap each operation in parentheses.
# This ensures Python performs the intended pairwise integration before summing the values.

# Compute individual integrals and sum them
# Note: parentheses are required to ensure correct evaluation order
sum_result = (rectangle + triangle_left) + (trapezoid + parab_trap)

# Output the final combined result
print(f"Total integration result: {sum_result}")
