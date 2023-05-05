import numpy as np
from matplotlib import pyplot as plt

##decorator function
def piecewise_4th(x, y):
    a1, a2, a3, a4, a5 = x
    b1, b2, b3, b4, b5 = y
    def A(a, c):
        return np.array([[a**2, a, 1], [c**2, c, 1], [2*c, 1, 0]])
    A1 = A(a1, a2); A2 = A(a5, a4)
    m1, n1, k1 = np.linalg.solve(A1, np.array([b1, b2, 0]))
    m2, n2, k2 = np.linalg.solve(A2, np.array([b5, b4, 0]))
    B = np.array([
        [a2**4, a2**3, a2**2, a2, 1], 
        [a3**4, a3**3, a3**2, a3, 1], 
        [a4**4, a4**3, a4**2, a4, 1], 
        [4*a2**3, 3*a2**2, 2*a2, 1, 0], 
        [4*a4**3, 3*a4**2, 2*a4, 1, 0]
    ])
    l, phi, theta, gamma, eta = np.linalg.solve(B, np.array([b2, b3, b4, 0, 0]))
    
    ##define the piecewise polynomial
    def poly(x):
        def elementwise(x):
            if x <= a2:
                return m1*x**2 + n1*x + k1
            elif x >= a4:
                return m2*x**2 + n2*x + k2
            else:
                return l*x**4 + phi*x**3 + theta*x**2 + gamma*x + eta
        if type(x) in [int, float]:
            return elementwise(x)
        else:
            return np.array(list(map(elementwise, x)))
    return poly


##this class models images of class 2 with two bumps
class class2image:
    def __init__(self, p2, p3, p4, h, alpha=1, cross_noise=None, 
                 fill='solid', vertical=None, bg_noise=None):
        #bump_x is the x position of the bump
        #bump_y is the height of the bump
        #h is the initial height
        #alpha: the color density of the interior
        #cross_noise, if not none, should be a list of 3 elements: [#crosses each side, linewidth, alpha]
        #if fill=='vertical', vertical cannot be None, it will be a list: [#lines, linewidth, alpha]
        #bg_noise, if not None, will be a list: [#scattered noise, alpha, color] color cannot be red
        self.h = h
        self.x = [-5, p2[0], p3[0], p4[0], 5]
        self.y = [h, p2[1], p3[1], p4[1], h]
        self.alpha = alpha
        self.cross_noise = cross_noise
        self.fill = fill
        self.vertical = vertical
        self.bg_noise = bg_noise
        ##construct the polynomial
        self.poly = piecewise_4th(self.x, self.y)

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

##this function generates total_num images of class 2 images
def generator2(total_num, path, dpi=100, cross_ratio=0.5, vertical_ratio=0.5, bg_ratio=0.8):
    color_map = ['blue', 'purple', 'green', 'yellow', 'grey']
    for i in range(total_num):
        h = np.random.uniform(0.5, 2.5)
        alpha = np.random.uniform(0.2, 1)
        ##generate random y coordinates
        b2 = np.random.uniform(h+0.3, min(3.5, 1.7*h))
        b4 = np.random.uniform(h+0.3, min(3.5, 1.7*h))
        upb = min(b2, b4); delta = upb - h
        b3 = np.random.uniform(h+0.25*delta, upb-0.25*delta)
        ##generate random x coordinates
        a2 = np.random.uniform(-4, -2)
        a3 = np.random.uniform(-1.5, 1.5)
        a4 = np.random.uniform(2, 4)
        p2 = [a2, b2]; p3 = [a3, b3]; p4 = [a4, b4]
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
        img = class2image(p2, p3, p4, h, alpha, cross_noise=cn, fill=fill, vertical=vertical, bg_noise=bg_noise)
        img.plot_save(path + "/class2_{}".format(i), dpi=dpi)


if __name__ == '__main__':
    generator2(200, './test/class2', dpi=70)