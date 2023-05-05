import numpy as np
from matplotlib import pyplot as plt

##decorator function to generate the piecewise polynomial
def piecewise_poly(x, y):
    a1, c, a2 = x
    b1, d, b2 = y
    def A(a, c):
        return np.array([[a**2, a, 1], [c**2, c, 1], [2*c, 1, 0]])
    A1 = A(a1, c)
    A2 = A(a2, c)
    b1 = np.array([b1, d, 0]); b2 = np.array([b2, d, 0])
    m1, n1, k1 = np.linalg.solve(A1, b1)
    m2, n2, k2 = np.linalg.solve(A2, b2)
    def poly(x):
        def elementwise(x):
            if x <= c:
                return m1*x**2 + n1*x + k1
            else:
                return m2*x**2 + n2*x + k2
        if type(x) in [int, float]:
            return elementwise(x)
        elif type(x) == np.ndarray:
            return np.array(list(map(elementwise, x)))
    return poly

##class to model class1 images
class class13image:
    def __init__(self, bump_x, bump_y, h, alpha=1, cross_noise=None, 
                 fill='solid', vertical=None, bg_noise=None):
        #bump_x is the x position of the bump
        #bump_y is the height of the bump
        #h is the initial height
        #alpha: the color density of the interior
        #cross_noise, if not none, should be a list of 3 elements: [#crosses each side, linewidth, alpha]
        #if fill=='vertical', vertical cannot be None, it will be a list: [#lines, linewidth, alpha]
        #bg_noise, if not None, will be a list: [#scattered noise, alpha, color] color cannot be red
        self.h = h
        self.x = [-5, bump_x, 5]
        self.y = [h, bump_y, h]
        self.alpha = alpha
        self.cross_noise = cross_noise
        self.fill = fill
        self.vertical = vertical
        self.bg_noise = bg_noise
        ##construct the polynomial
        self.poly = piecewise_poly(self.x, self.y)

    def plot(self):
        plt.axis('off')
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        plt.axis('equal')
        if self.fill=='solid':
            xlab = np.arange(-5, 5, .1)
            ylab = self.poly(xlab)
            plt.fill_between(xlab, ylab, -ylab, color='red', alpha=self.alpha, zorder=10)
        if self.fill == 'vertical':
            x_lab = np.arange(-5, 5, 10/self.vertical[0])
            for x in x_lab:
                y = self.poly(float(x))
                plt.plot([x, x], [-y, y], c = 'red', alpha=self.vertical[2], lw=self.vertical[1], zorder=10)
        if self.cross_noise:
            cross_x = np.array([np.random.uniform(low=-5, high=5) for i in range(self.cross_noise[0])])
            size = [np.random.uniform(low=25, high=600) for i in range(self.cross_noise[0])]
            cross_y = self.poly(cross_x)
            plt.scatter(cross_x, cross_y, s=size, 
                            linewidths=self.cross_noise[1], alpha=self.cross_noise[2], marker='x', c='black', zorder=20)
            plt.scatter(cross_x, -cross_y, s=size, 
                            linewidths=self.cross_noise[1], alpha=self.cross_noise[2], marker='x', c='black', zorder=20)
        if self.bg_noise is not None:
            xlab_upper = [np.random.uniform(-4.5, 4.5) for i in range(self.bg_noise[0])]
            ylab_upper = [np.random.uniform(self.h, 5) for i in range(self.bg_noise[0])]
            size_upper = [np.random.uniform(50, 400) for i in range(self.bg_noise[0])]
            xlab_lower = [np.random.uniform(-4.5, 4.5) for i in range(self.bg_noise[0])]
            ylab_lower = [np.random.uniform(-5, -self.h) for i in range(self.bg_noise[0])]
            size_lower = [np.random.uniform(50, 400) for i in range(self.bg_noise[0])]
            plt.scatter(xlab_upper, ylab_upper, s=size_upper, c = self.bg_noise[2], alpha=self.bg_noise[1], zorder=1)
            plt.scatter(xlab_lower, ylab_lower, s=size_lower, c = self.bg_noise[2], alpha=self.bg_noise[1], zorder=1)
        plt.axhline(5, alpha=0.001)
        plt.axhline(-5, alpha=0.01)

    ##this method plots and shows the image without saving it
    def plot_show(self):
        self.plot()
        plt.show()

    ##this method plots and saves the image into the designated path
    def plot_save(self, path, dpi=100):
        self.plot()
        plt.margins(0,0) 
        plt.savefig(path, dpi=dpi, bbox_inches='tight', pad_inches = 0)
        plt.close()


##this function generates total_num images of class 1 images
def generator1(total_num, path, dpi=100, cross_ratio=0.5, vertical_ratio=0.5, bg_ratio=0.8):
    color_map = ['blue', 'purple', 'green', 'yellow', 'grey']
    for i in range(total_num):
        h = np.random.uniform(0.5, 2.5)
        alpha = np.random.uniform(0.2, 1)
        ##generate random bump y coordinate
        bump_y = np.random.uniform(h+0.3, min(3.5, 1.7*h)) ##make sure y is at most 1.7*h
        ##generate random bump x coordinate
        bump_x = np.random.uniform(-3.5, 3.5)
        cn = None
        if np.random.uniform() <= cross_ratio: ##add cross noise
            cn = [np.random.randint(2, 26), np.random.uniform(0.6, 4), np.random.uniform(0.2, 1)]
        fill = 'solid'; vertical = None
        if np.random.uniform() <= vertical_ratio: ##use vertical lines
            fill = 'vertical'
            num_lines = np.random.randint(10, 81)
            width = 10/num_lines
            ##make sure there is no overlapping between vertical line strips
            lw = np.random.uniform(1, 10)
            while ((lw/width) >= 32):
                lw = np.random.uniform(1, 5)
            vertical = [num_lines, lw, np.random.uniform(0.2, 1)]
        bg_noise = None
        if np.random.uniform() <= bg_ratio: ##add background noise
            bg_noise = [np.random.randint(5, 61), np.random.uniform(0.1, .7), color_map[np.random.randint(0, 5)]]
        img = class13image(bump_x, bump_y, h, alpha, cross_noise=cn, fill=fill, vertical=vertical, bg_noise=bg_noise)
        img.plot_save(path + "/class1_{}".format(i), dpi=dpi)

##this function generates total_num images of class 3 images
def generator3(total_num, path, dpi=100, cross_ratio=0.5, vertical_ratio=0.5, bg_ratio=0.8):
    color_map = ['blue', 'purple', 'green', 'yellow', 'grey']
    for i in range(total_num):
        h = np.random.uniform(0.5, 3)
        alpha = np.random.uniform(0.2, 1)
        ##generate random bump y coordinate
        bump_y = np.random.uniform(0.5*h, 0.9*h)
        ##generate random bump x coordinate
        bump_x = np.random.uniform(-3.5, 3.5)
        cn = None
        if np.random.uniform() <= cross_ratio: ##add cross noise
            cn = [np.random.randint(2, 26), np.random.uniform(0.6, 4), np.random.uniform(0.2, 1)]
        fill = 'solid'; vertical = None
        if np.random.uniform() <= vertical_ratio: ##use vertical lines
            fill = 'vertical'
            num_lines = np.random.randint(10, 81)
            width = 10/num_lines
            ##make sure there is no overlapping between vertical line strips
            lw = np.random.uniform(1, 10)
            while ((lw/width) >= 32):
                lw = np.random.uniform(1, 5)
            vertical = [num_lines, lw, np.random.uniform(0.2, 1)]
        bg_noise = None
        if np.random.uniform() <= bg_ratio: ##add background noise
            bg_noise = [np.random.randint(5, 61), np.random.uniform(0.1, .7), color_map[np.random.randint(0, 5)]]
        img = class13image(bump_x, bump_y, h, alpha, cross_noise=cn, fill=fill, vertical=vertical, bg_noise=bg_noise)
        img.plot_save(path + "/class1_{}".format(i), dpi=dpi)


if __name__ == '__main__':
    generator1(200, './test/class1', dpi=70)
    generator3(200, './test/class3', dpi=70)

