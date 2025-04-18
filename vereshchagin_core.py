import vereshchagin_figures as vf

def integrate_pair(figure_1, figure_2):
    type_1 = type(figure_1)
    type_2 = type(figure_2)
    pair = frozenset([type_1, type_2])

    if pair == frozenset([vf.Rectangle]):
        print("Rectangle + Rectangle")
        return figure_1.x * figure_1.height * figure_2.height

    elif pair == frozenset([vf.Rectangle, vf.TriangleLeft]):
        print("Rectangle + TriangleLeft")
        rect, tri = (figure_1, figure_2) if isinstance(figure_1, vf.Rectangle) else (figure_2, figure_1)
        return rect.x * rect.height * (tri.height / 2)

    elif pair == frozenset([vf.Rectangle, vf.TriangleRight]):
        print("Rectangle + TriangleRight")
        rect, tri = (figure_1, figure_2) if isinstance(figure_1, vf.Rectangle) else (figure_2, figure_1)
        return rect.x * rect.height * (tri.height / 2)

    elif pair == frozenset([vf.Rectangle, vf.Trapezoid]):
        print("Rectangle + Trapezoid")
        rect, trap = (figure_1, figure_2) if isinstance(figure_1, vf.Rectangle) else (figure_2, figure_1)
        return (rect.x/6)*(2*rect.height*trap.height_left + 2*rect.height*trap.height_right +
                           rect.height*trap.height_right + rect.height*trap.height_left)

    elif pair == frozenset([vf.Rectangle, vf.Parabola]):
        print("Rectangle + Parabola")
        rect, par = (figure_1, figure_2) if isinstance(figure_1, vf.Rectangle) else (figure_2, figure_1)
        f = par.line_load * (par.x**2) / 8
        return (2/3) * (rect.x * f * rect.height)

    elif pair == frozenset([vf.TriangleLeft]):
        print("TriangleLeft + TriangleLeft")
        return (1/3) * figure_1.x * figure_1.height * figure_2.height

    elif pair == frozenset([vf.TriangleLeft, vf.TriangleRight]):
        print("TriangleLeft + TriangleRight")
        tri_left, tri_right = (figure_1, figure_2) if isinstance(figure_1, vf.TriangleLeft) else (figure_2, figure_1)
        return (1/6) * tri_left.x * tri_left.height * tri_right.height

    elif pair == frozenset([vf.TriangleLeft, vf.Trapezoid]):
        print("TriangleLeft + Trapezoid")
        tri, trap = (figure_1, figure_2) if isinstance(figure_1, vf.TriangleLeft) else (figure_2, figure_1)
        return (tri.x/6) * (2*tri.height * trap.height_left + trap.height_right * tri.height)

    elif pair == frozenset([vf.TriangleLeft, vf.Parabola]):
        print("TriangleLeft + Parabola")
        tri, par = (figure_1, figure_2) if isinstance(figure_1, vf.TriangleLeft) else (figure_2, figure_1)
        f = par.line_load * (par.x**2) / 8
        return (1/3) * (tri.x * f * tri.height)

    elif pair == frozenset([vf.TriangleRight]):
        print("TriangleRight + TriangleRight")
        return (1/3) * figure_1.x * figure_1.height * figure_2.height

    elif pair == frozenset([vf.TriangleRight, vf.Parabola]):
        print("TriangleRight + Parabola")
        tri, par = (figure_1, figure_2) if isinstance(figure_1, vf.TriangleRight) else (figure_2, figure_1)
        f = par.line_load * (par.x**2) / 8
        return (1/3) * (tri.x * f * tri.height)

    elif pair == frozenset([vf.TriangleRight, vf.Trapezoid]):
        print("TriangleRight + Trapezoid")
        tri, trap = (figure_1, figure_2) if isinstance(figure_1, vf.TriangleRight) else (figure_2, figure_1)
        return (tri.x/6) * (2*tri.height * trap.height_right + trap.height_left * tri.height)

    elif pair == frozenset([vf.Trapezoid]):
        print("Trapezoid + Trapezoid")
        return (figure_1.x/6) * (
            2*figure_1.height_left * figure_2.height_left +
            2*figure_1.height_right * figure_2.height_right +
            figure_1.height_left * figure_2.height_right +
            figure_1.height_right * figure_2.height_left
        )

    elif pair == frozenset([vf.Parabola]):
        print("Parabola + Parabola")
        f = figure_1.line_load * (figure_1.x**2) / 8
        g = figure_2.line_load * (figure_2.x**2) / 8
        return (8/15) * (figure_1.x * f * g)

    elif pair == frozenset([vf.Trapezoid, vf.Parabola]):
        print("Trapezoid + Parabola")
        trap, par = (figure_1, figure_2) if isinstance(figure_1, vf.Trapezoid) else (figure_2, figure_1)
        f = par.line_load * (par.x**2) / 8
        triangle_1 = vf.TriangleLeft(trap.x, trap.height_left)
        triangle_2 = vf.TriangleRight(trap.x, trap.height_right)
        return (1/3) * (triangle_1.x * f * triangle_1.height +
                        triangle_2.x * f * triangle_2.height)

    elif pair == frozenset([vf.ParabolicTrapezoid, vf.Rectangle]):
        print("ParabolicTrapezoid + Rectangle")
        parab_trap, rect = (figure_1, figure_2) if isinstance(figure_1, vf.ParabolicTrapezoid) else (figure_2, figure_1)
        parabola = vf.Parabola(parab_trap.x, parab_trap.line_load)
        trapezoid = vf.Trapezoid(parab_trap.x, parab_trap.height_left, parab_trap.height_right)
        return integrate_pair(trapezoid, rect) + integrate_pair(parabola, rect)

    elif pair == frozenset([vf.ParabolicTrapezoid, vf.TriangleLeft]):
        print("ParabolicTrapezoid + TriangleLeft")
        parab_trap, tri = (figure_1, figure_2) if isinstance(figure_1, vf.ParabolicTrapezoid) else (figure_2, figure_1)
        parabola = vf.Parabola(parab_trap.x, parab_trap.line_load)
        trapezoid = vf.Trapezoid(parab_trap.x, parab_trap.height_left, parab_trap.height_right)
        return integrate_pair(trapezoid, tri) + integrate_pair(parabola, tri)

    elif pair == frozenset([vf.ParabolicTrapezoid,vf.TriangleRight]):
        print("ParabolicTrapezoid + TriangleRight")
        parab_trap, tri = (figure_1, figure_2) if isinstance(figure_1, vf.ParabolicTrapezoid) else (figure_2, figure_1)
        parabola = vf.Parabola(parab_trap.x, parab_trap.line_load)
        trapezoid = vf.Trapezoid(parab_trap.x, parab_trap.height_left, parab_trap.height_right)
        return integrate_pair(trapezoid, tri) + integrate_pair(parabola, tri)

    elif pair == frozenset([vf.ParabolicTrapezoid, vf.Trapezoid]):
        print("ParabolicTrapezoid + Trapezoid")
        parab_trap, trap = (figure_1, figure_2) if isinstance(figure_1, vf.ParabolicTrapezoid) else (figure_2, figure_1)
        parabola = vf.Parabola(parab_trap.x, parab_trap.line_load)
        trapezoid = vf.Trapezoid(parab_trap.x, parab_trap.height_left, parab_trap.height_right)
        return integrate_pair(trapezoid, trap) + integrate_pair(parabola, trap)

    elif pair == frozenset([vf.ParabolicTrapezoid,vf.Parabola]):
        print("ParabolicTrapezoid + Parabola")
        parab_trap, par = (figure_1, figure_2) if isinstance(figure_1, vf.ParabolicTrapezoid) else (figure_2, figure_1)
        parabola = vf.Parabola(parab_trap.x, parab_trap.line_load)
        trapezoid = vf.Trapezoid(parab_trap.x, parab_trap.height_left, parab_trap.height_right)
        return integrate_pair(trapezoid, par) + integrate_pair(parabola, par)

    elif pair == frozenset([vf.ParabolicTrapezoid]):
        print("ParabolicTrapezoid + ParabolicTrapezoid")
        parab_trap_1, parab_trap_2 = (figure_1, figure_2)
        parabola_1 = vf.Parabola(parab_trap_1.x, parab_trap_1.line_load)
        parabola_2 = vf.Parabola(parab_trap_2.x, parab_trap_2.line_load)
        trapezoid_1 = vf.Trapezoid(parab_trap_1.x, parab_trap_1.height_left, parab_trap_1.height_right)
        trapezoid_2 = vf.Trapezoid(parab_trap_2.x, parab_trap_2.height_left, parab_trap_2.height_right)
        return integrate_pair(parabola_1, parabola_2) + integrate_pair(trapezoid_1, trapezoid_2) + integrate_pair(parabola_1, trapezoid_2) + integrate_pair(parabola_2, trapezoid_1)

    else:
        raise TypeError(f"Unsupported figure combination: {type_1.__name__} + {type_2.__name__}")
