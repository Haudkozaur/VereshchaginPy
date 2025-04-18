from vereshchagin_figures import Rectangle, TriangleLeft, Parabola, ParabolicTrapezoid, Trapezoid

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
rectangle = Rectangle(1, 5)
trapezoid = Trapezoid(1, -2, 3)

result_2 = trapezoid + rectangle
print(result_2)

triangle_1 = TriangleLeft(1, -2)
triangle_2 = TriangleLeft(1, 3)

result_2 = (triangle_1+rectangle)+(triangle_2+rectangle)
print(result_2)