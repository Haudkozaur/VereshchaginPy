from vereshchagin_figures import Rectangle, TriangleLeft, TriangleRight, Parabola, ParabolicTrapezoid, Trapezoid

# rectangle = Rectangle(1, 5)
# triangle_1 = TriangleLeft(1, 2)
# triangle_2 = TriangleLeft(1, 3)
# parabola = Parabola(1, 1)
#
# result = (rectangle + triangle_1) + (rectangle + triangle_2) + (rectangle + parabola)
# print(result)
#
# trapezoidparabola = ParabolicTrapezoidUp(1, 2, 3, 1)
#
# result_2 = trapezoidparabola + rectangle
# print(result_2)
#
# rectangle = Rectangle(1, 5)
# triangle_1 = TriangleLeft(1, 2)
# triangle_2 = TriangleLeft(1, 3)
# parabola = Parabola(1, -1)
#
# result = (rectangle + triangle_1) + (rectangle + triangle_2) + (rectangle + parabola)
# print(result)
# rectangle = Rectangle(1, 5)
# trapezoid = Trapezoid(1, -2, 3)
#
# result_2 = trapezoid + rectangle
# print(result_2)
#
# triangle_1 = TriangleLeft(1, -2)
# triangle_2 = TriangleLeft(1, 3)
#
# result_2 = (triangle_1+rectangle)+(triangle_2+rectangle)
# print(result_2)


from vereshchagin_visualise import VereshchaginVisualiser

from vereshchagin_visualise import VereshchaginVisualiser



rect1 = Rectangle(x=5, height=3)
rect2 = Rectangle(x=5, height=-2)
triangle_left = TriangleLeft(x=5, height=-2)
triangle_left_2 = TriangleLeft(x=5, height=-3)
triangle_right = TriangleRight(x=5, height=2)
trapezoid = Trapezoid(x=5, height_left=4, height_right=-2)
parabola = Parabola(x=5, line_load=1)
par_trap = ParabolicTrapezoid(x=5, height_left=2, height_right=3, line_load=-1)
viz = VereshchaginVisualiser()
# viz.draw_situation(rect1, rect2)
# viz.draw_situation(rect1,triangle_left)
# viz.draw_situation(triangle_right, triangle_left)
# viz.draw_situation(triangle_left, triangle_left_2)
# viz.draw_situation(trapezoid, rect2)
# viz.draw_situation(rect1, parabola)
# viz.draw_situation(parabola, trapezoid)
# viz.draw_situation(parabola, triangle_left)
# viz.draw_situation(rect2, parabola)
viz.draw_situation(rect1, par_trap)
viz.draw_situation(par_trap, rect2)
viz.draw_situation(par_trap, triangle_left)
viz.draw_situation(par_trap, triangle_right)
viz.draw_situation(par_trap, trapezoid)
viz.draw_situation(parabola, par_trap)