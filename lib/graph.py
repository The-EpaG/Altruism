import matplotlib.pyplot as plt


class Graph:
    def plot_y(self, y_points, show=True, label=None):
        plt.plot(y_points, label=label)
        if show:
            if label:
                plt.legend()
            plt.grid()
            plt.show()

    def plot(self, x_points, y_points, show=True, label=None):
        plt.plot(x_points, y_points, label=label)
        if show:
            if label:
                plt.legend()
            plt.grid()
            plt.show()
