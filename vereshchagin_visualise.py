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
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.RECTANGLE_TRIANGLE_LEFT:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.RECTANGLE_TRIANGLE_RIGHT:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.TRIANGLE_LEFT_TRIANGLE_LEFT:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.TRIANGLE_LEFT_TRIANGLE_RIGHT:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.TRIANGLE_RIGHT_TRIANGLE_RIGHT:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.RECTANGLE_TRAPEZOID:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.RECTANGLE_PARABOLA:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.TRIANGLE_LEFT_TRAPEZOID:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.TRIANGLE_LEFT_PARABOLA:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.TRIANGLE_RIGHT_PARABOLA:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.TRIANGLE_RIGHT_TRAPEZOID:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.TRAPEZOID_TRAPEZOID:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.TRAPEZOID_PARABOLA:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.PARABOLA_PARABOLA:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)

            case FigureType.PARABOLIC_TRAPEZOID_RECTANGLE:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)
            case FigureType.PARABOLIC_TRAPEZOID_TRIANGLE_LEFT:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)
            case FigureType.PARABOLIC_TRAPEZOID_TRIANGLE_RIGHT:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)
            case FigureType.PARABOLIC_TRAPEZOID_TRAPEZOID:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)
            case FigureType.PARABOLIC_TRAPEZOID_PARABOLA:
                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0.5)
            case FigureType.PARABOLIC_TRAPEZOID_PARABOLIC_TRAPEZOID:

                self.draw_single(ax, figure_1, 'blue', 0.4, label_offset=0.5)
                self.draw_single(ax, figure_2, 'red', 0.4, label_offset=0)

            case _:
                raise TypeError(
                    f"Unsupported figure combination: {type(figure_1).__name__} + {type(figure_2).__name__}"
                )
        heights = []
        for fig in [figure_1, figure_2]:
            if hasattr(fig, "height"):
                heights.append(fig.height)
            elif hasattr(fig, "height_left") and hasattr(fig, "height_right"):
                heights.extend([fig.height_left, fig.height_right])
            else:
                heights.append(0)

        min_y = min(0, *heights)
        max_y = max(0, *heights)
        padding = (max_y - min_y) * 0.2 or 1  # zawsze jakiś margines
        ax.set_ylim(min_y - padding, max_y + padding)

        ax.axhline(0, color='black', linewidth=1)
        ax.set_xlim(0, figure_1.x)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel("")
        ax.set_ylabel("")
        ax.grid(False)
        for spine in ax.spines.values():
            spine.set_visible(False)

        plt.title(f'Situation: {type(figure_1).__name__} + {type(figure_2).__name__}')
        plt.show()

    def draw_single(self, ax, fig, color, alpha, label_offset=0.0):
        x0 = 0

        match fig:
            case vf.Rectangle(x=x, height=h):
                y0 = min(0, h)
                ax.add_patch(
                    patches.Rectangle((x0, y0), x, abs(h), color=color, alpha=alpha)
                )
                y_label = h + 0.2 + label_offset if h >= 0 else h - 0.2 - label_offset
                ax.text(x0 + x / 2, y_label, f"rectangle height = {h}",
                        ha='center', va='bottom' if h >= 0 else 'top')
                ax.text(x0 + x / 2, -0.3, f"x = {x}", ha='center', va='top')

            case vf.TriangleLeft(x=x, height=h):
                ax.add_patch(
                    patches.Polygon([(x0, 0), (x0, h), (x0 + x, 0)], closed=True, color=color, alpha=alpha)
                )
                direction = 1 if h >= 0 else -1
                x_label = x0 - 0.3 - label_offset * direction
                ax.text(x_label, h / 2, f"triangle height = {h}",
                        ha='right', va='center', rotation=90)
                ax.text(x0 + x / 2, -0.3, f"x = {x}", ha='center', va='top')

            case vf.TriangleRight(x=x, height=h):
                ax.add_patch(
                    patches.Polygon([(x0, 0), (x0 + x, h), (x0 + x, 0)], closed=True, color=color, alpha=alpha)
                )
                direction = 1 if h >= 0 else -1
                x_label = x0 + x + 0.3 + label_offset * direction
                ax.text(x_label, h / 2, f"triangle height = {h}",
                        ha='left', va='center', rotation=90)
                ax.text(x0 + x / 2, -0.3, f"x = {x}", ha='center', va='top')

            case vf.Trapezoid(x=x, height_left=h_left, height_right=h_right):
                ax.add_patch(
                    patches.Polygon(
                        [(x0, 0), (x0, h_left), (x0 + x, h_right), (x0 + x, 0)],
                        closed=True, color=color, alpha=alpha
                    )
                )

                direction_left = 1 if h_left >= 0 else -1
                direction_right = 1 if h_right >= 0 else -1

                ax.text(x0 - 0.3 - label_offset * direction_left, h_left / 2,
                        f"hL = {h_left}", ha='right', va='center', rotation=90)

                ax.text(x0 + x + 0.3 + label_offset * direction_right, h_right / 2,
                        f"hR = {h_right}", ha='left', va='center', rotation=90)

                ax.text(x0 + x / 2, -0.3, f"x = {x}", ha='center', va='top')

            case vf.Parabola(x=x, line_load=load):
                f = (load * x ** 2) / 8
                self.draw_parabola_through_points(
                    ax,
                    x1=0,
                    x2=x,
                    ymax=f,
                    color=color,
                    alpha=alpha,
                    label=f"parabola f = {round(f, 2)}"
                )
                ax.text(x / 2, -0.3, f"x = {x}", ha='center', va='top')
            case vf.ParabolicTrapezoid(x=x, height_left=h_left, height_right=h_right, line_load=line_load):
                f = (line_load * x ** 2) / 8

                x_vals = np.linspace(x0, x0 + x, 200)
                base_line = np.linspace(h_left, h_right, 200)
                bump = np.sin(np.linspace(0, np.pi, 200))
                curvature = f * 0.2
                y_vals = base_line + bump * curvature

                cross_axis = (h_left >= 0 and h_right <= 0) or (h_left <= 0 and h_right >= 0)

                if cross_axis:
                    ax.fill_between(x_vals, 0, y_vals, color=color, alpha=alpha)
                    ax.plot(x_vals, y_vals, color=color, linewidth=2, alpha=alpha)
                    peak_x = x0 + x / 2
                    peak_y = max(y_vals) if f >= 0 else min(y_vals)
                    ax.text(peak_x, peak_y + 0.2 if f >= 0 else peak_y - 0.2,
                            f"f = {round(f, 2)}", ha='center', va='bottom' if f >= 0 else 'top')

                else:
                    if f >= 0 and not (h_left < 0 and h_right < 0):
                        points = (
                                [(x0, 0)] +
                                list(zip(x_vals, y_vals)) +
                                [(x0 + x, 0)]
                        )
                        ax.add_patch(
                            patches.Polygon(points, closed=True, color=color, alpha=alpha)
                        )
                    else:
                        points = (
                                [(x0, 0)] +
                                list(zip(x_vals, y_vals)) +
                                [(x0 + x, 0)]
                        )
                        ax.add_patch(
                            patches.Polygon(points, closed=True, color=color, alpha=alpha)
                        )

                    ax.plot(x_vals, y_vals, color=color, linewidth=2, alpha=alpha)
                    peak_x = x0 + x / 2
                    peak_y = (h_left + h_right) / 2 + curvature
                    ax.text(peak_x, peak_y + 0.2 if f >= 0 else peak_y - 0.2,
                            f"f = {round(f, 2)}", ha='center', va='bottom' if f >= 0 else 'top')

                ax.text(x0 - 0.3, h_left / 2, f"hL = {h_left}", ha='right', va='center', rotation=90)
                ax.text(x0 + x + 0.3, h_right / 2, f"hR = {h_right}", ha='left', va='center', rotation=90)
                ax.text(x0 + x / 2, -0.3, f"x = {x}", ha='center', va='top')

            case _:
                raise TypeError(f"Unsupported figure type in overlay: {type(fig).__name__}")

    def draw_parabola_through_points(self, ax, x1, x2, ymax, color, alpha, label):
        xv = (x1 + x2) / 2
        A = np.array([
            [x1 ** 2, x1, 1],
            [x2 ** 2, x2, 1],
            [xv ** 2, xv, 1]
        ])
        b = np.array([0, 0, ymax])
        a, b, c = np.linalg.solve(A, b)

        x_vals = np.linspace(x1, x2, 200)
        y_vals = a * x_vals ** 2 + b * x_vals + c

        ax.plot(x_vals, y_vals, color=color, linewidth=2)
        ax.fill_between(x_vals, 0, y_vals, color=color, alpha=alpha)

        ax.text(xv, ymax + 0.2 if ymax >= 0 else ymax - 0.2, label,
                ha='center', va='bottom' if ymax >= 0 else 'top')
