import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import vereshchagin_figures as vf
from vereshchagin_pairs import get_figure_pair_type, FigureType

class VereshchaginVisualiser:

    def draw_situation(self, figure_1, figure_2):

        pair_type = get_figure_pair_type(figure_1, figure_2)
        fig, ax = plt.subplots()

        match pair_type:

            case FigureType.RECTANGLE_RECTANGLE:
                self.draw_single(ax, figure_1, 'blue', 0.4)
                self.draw_single(ax, figure_2, 'red', 0.4)

            case FigureType.RECTANGLE_TRIANGLE_LEFT:
                pass

            case FigureType.RECTANGLE_TRIANGLE_RIGHT:
                pass

            case FigureType.RECTANGLE_TRAPEZOID:
                pass

            case FigureType.RECTANGLE_PARABOLA:
                pass

            case FigureType.TRIANGLE_LEFT_TRIANGLE_LEFT:
                pass

            case FigureType.TRIANGLE_LEFT_TRIANGLE_RIGHT:
                pass

            case FigureType.TRIANGLE_LEFT_TRAPEZOID:
                pass

            case FigureType.TRIANGLE_LEFT_PARABOLA:
                pass

            case FigureType.TRIANGLE_RIGHT_TRIANGLE_RIGHT:
                pass

            case FigureType.TRIANGLE_RIGHT_PARABOLA:
                pass

            case FigureType.TRIANGLE_RIGHT_TRAPEZOID:
                pass

            case FigureType.TRAPEZOID_TRAPEZOID:
                pass

            case FigureType.PARABOLA_PARABOLA:
                pass

            case FigureType.TRAPEZOID_PARABOLA:
                pass

            case FigureType.PARABOLIC_TRAPEZOID_RECTANGLE:
                pass

            case FigureType.PARABOLIC_TRAPEZOID_TRIANGLE_LEFT:
                pass

            case FigureType.PARABOLIC_TRAPEZOID_TRIANGLE_RIGHT:
                pass

            case FigureType.PARABOLIC_TRAPEZOID_TRAPEZOID:
                pass

            case FigureType.PARABOLIC_TRAPEZOID_PARABOLA:
                pass

            case FigureType.PARABOLIC_TRAPEZOID_PARABOLIC_TRAPEZOID:
                pass

            case _:
                raise TypeError(
                    f"Unsupported figure combination: {type(figure_1).__name__} + {type(figure_2).__name__}")

        ax.axhline(0, color='black', linewidth=1)
        ax.set_xlim(0, figure_1.x)
        ax.set_ylim(
            -max(figure_1.height, figure_2.height) * 1.2,
             max(figure_1.height, figure_2.height) * 1.2
        )
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.grid(False)
        for spine in ax.spines.values():
            spine.set_visible(False)
        plt.title(f'Situation: {type(figure_1).__name__} + {type(figure_2).__name__}')
        plt.show()

    def draw_single(self, ax, fig, color, alpha):
        x0 = 0
        if isinstance(fig, vf.Rectangle):
            ax.add_patch(
                patches.Rectangle((x0, 0), fig.x, fig.height, color=color, alpha=alpha)
            )
            # podpisy wartości
            ax.text(x0 + fig.x / 2, fig.height + 0.2, f"h={fig.height}", ha='center', va='bottom')
            ax.text(x0 + fig.x / 2, -0.3, f"x={fig.x}", ha='center', va='top')
        else:
            raise TypeError(f"Unsupported figure type in overlay: {type(fig).__name__}")
