import vereshchagin_figures as vf
from enum import Enum, auto


def get_figure_pair_type(fig1, fig2):
    type_1 = type(fig1)
    type_2 = type(fig2)
    pair = frozenset([type_1, type_2])

    mapping = {
        frozenset([vf.Rectangle]): FigureType.RECTANGLE_RECTANGLE,
        frozenset([vf.Rectangle, vf.TriangleLeft]): FigureType.RECTANGLE_TRIANGLE_LEFT,
        frozenset([vf.Rectangle, vf.TriangleRight]): FigureType.RECTANGLE_TRIANGLE_RIGHT,
        frozenset([vf.Rectangle, vf.Trapezoid]): FigureType.RECTANGLE_TRAPEZOID,
        frozenset([vf.Rectangle, vf.Parabola]): FigureType.RECTANGLE_PARABOLA,
        frozenset([vf.TriangleLeft]): FigureType.TRIANGLE_LEFT_TRIANGLE_LEFT,
        frozenset([vf.TriangleLeft, vf.TriangleRight]): FigureType.TRIANGLE_LEFT_TRIANGLE_RIGHT,
        frozenset([vf.TriangleLeft, vf.Trapezoid]): FigureType.TRIANGLE_LEFT_TRAPEZOID,
        frozenset([vf.TriangleLeft, vf.Parabola]): FigureType.TRIANGLE_LEFT_PARABOLA,
        frozenset([vf.TriangleRight]): FigureType.TRIANGLE_RIGHT_TRIANGLE_RIGHT,
        frozenset([vf.TriangleRight, vf.Trapezoid]): FigureType.TRIANGLE_RIGHT_TRAPEZOID,
        frozenset([vf.TriangleRight, vf.Parabola]): FigureType.TRIANGLE_RIGHT_PARABOLA,
        frozenset([vf.Trapezoid]): FigureType.TRAPEZOID_TRAPEZOID,
        frozenset([vf.Trapezoid, vf.Parabola]): FigureType.TRAPEZOID_PARABOLA,
        frozenset([vf.Parabola]): FigureType.PARABOLA_PARABOLA,
        frozenset([vf.ParabolicTrapezoid, vf.Rectangle]): FigureType.PARABOLIC_TRAPEZOID_RECTANGLE,
        frozenset([vf.ParabolicTrapezoid, vf.TriangleLeft]): FigureType.PARABOLIC_TRAPEZOID_TRIANGLE_LEFT,
        frozenset([vf.ParabolicTrapezoid, vf.TriangleRight]): FigureType.PARABOLIC_TRAPEZOID_TRIANGLE_RIGHT,
        frozenset([vf.ParabolicTrapezoid, vf.Trapezoid]): FigureType.PARABOLIC_TRAPEZOID_TRAPEZOID,
        frozenset([vf.ParabolicTrapezoid, vf.Parabola]): FigureType.PARABOLIC_TRAPEZOID_PARABOLA,
        frozenset([vf.ParabolicTrapezoid]): FigureType.PARABOLIC_TRAPEZOID_PARABOLIC_TRAPEZOID,
    }
    if pair not in mapping:
        raise ValueError(f"Unsupported figure pair: {pair}")
    return mapping[pair]


class FigureType(Enum):
    RECTANGLE_RECTANGLE = auto()
    RECTANGLE_TRIANGLE_LEFT = auto()
    RECTANGLE_TRIANGLE_RIGHT = auto()
    RECTANGLE_TRAPEZOID = auto()
    RECTANGLE_PARABOLA = auto()
    TRIANGLE_LEFT_TRIANGLE_LEFT = auto()
    TRIANGLE_LEFT_TRIANGLE_RIGHT = auto()
    TRIANGLE_LEFT_TRAPEZOID = auto()
    TRIANGLE_LEFT_PARABOLA = auto()
    TRIANGLE_RIGHT_TRIANGLE_RIGHT = auto()
    TRIANGLE_RIGHT_TRAPEZOID = auto()
    TRIANGLE_RIGHT_PARABOLA = auto()
    TRAPEZOID_TRAPEZOID = auto()
    TRAPEZOID_PARABOLA = auto()
    PARABOLA_PARABOLA = auto()
    PARABOLIC_TRAPEZOID_RECTANGLE = auto()
    PARABOLIC_TRAPEZOID_TRIANGLE_LEFT = auto()
    PARABOLIC_TRAPEZOID_TRIANGLE_RIGHT = auto()
    PARABOLIC_TRAPEZOID_TRAPEZOID = auto()
    PARABOLIC_TRAPEZOID_PARABOLA = auto()
    PARABOLIC_TRAPEZOID_PARABOLIC_TRAPEZOID = auto()

