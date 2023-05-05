import numpy as np
from matplotlib import pyplot as plt

class class0image:
    def __init__(self, h, alpha=1, cross_noise=None, fill='solid', vertical=None, bg_noise=None):
        #cross_noise, if not none, should be a list of 3 elements: [#crosses each side, linewidth, alpha]
        #if fill=='vertical', vertical cannot be None, it will be a list: [#lines, linewidth, alpha]
        #bg_noise, if not None, will be a list: [#scattered noise, alpha, color] color cannot be red
        self.h = h
        self.alpha = alpha
        self.cross_noise = cross_noise
        self.fill = fill
        self.vertical = vertical
        self.bg_noise = bg_noise

    def plot(self):
        plt.axis('off')
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        plt.axis('equal')
        if self.fill=='solid':
            xlab = np.arange(-5, 5, .1)
            ylab = self.h*np.ones(len(xlab))
            plt.fill_between(xlab, ylab, -ylab, color='red', alpha=self.alpha)
        if self.fill == 'vertical':
            x_lab = np.arange(-5, 5, 10/self.vertical[0])
            for x in x_lab:
                #plt.axvline(x=x, ymin=float((5.0-self.h)/10.0), ymax=float((5.0+self.h)/10.0), c='red', alpha=self.vertical[2], lw=self.vertical[1])
                plt.plot([x, x], [-self.h, self.h], c = 'red', alpha=self.vertical[2], lw=self.vertical[1])
        if self.cross_noise:
            cross_x = [np.random.uniform(low=-5, high=5) for i in range(self.cross_noise[0])]
            size = [np.random.uniform(low=25, high=600) for i in range(self.cross_noise[0])]
            plt.scatter(cross_x, self.h*np.ones(len(cross_x)), s=size, 
                        linewidths=self.cross_noise[1], alpha=self.cross_noise[2], marker='x', c='black', zorder=20)
            plt.scatter(cross_x, -self.h*np.ones(len(cross_x)), s=size, 
                        linewidths=self.cross_noise[1], alpha=self.cross_noise[2], marker='x', c='black', zorder=20)
        if self.bg_noise is not None:
            xlab_upper = [np.random.uniform(-4.5, 4.5) for i in range(self.bg_noise[0])]
            ylab_upper = [np.random.uniform(self.h, 5) for i in range(self.bg_noise[0])]
            size_upper = [np.random.uniform(50, 400) for i in range(self.bg_noise[0])]
            xlab_lower = [np.random.uniform(-4.5, 4.5) for i in range(self.bg_noise[0])]
            ylab_lower = [np.random.uniform(-5, -self.h) for i in range(self.bg_noise[0])]
            size_lower = [np.random.uniform(50, 400) for i in range(self.bg_noise[0])]
            plt.scatter(xlab_upper, ylab_upper, s=size_upper, c = self.bg_noise[2], alpha=self.bg_noise[1])
            plt.scatter(xlab_lower, ylab_lower, s=size_lower, c = self.bg_noise[2], alpha=self.bg_noise[1])
        


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

##this function generates artificial images of class 0
##h can be any float from 0.5-2.5
##alpha can be any float from 0.2 - 1
##cross noise can be added [#cross: 5-25, lw: 1-3, alpha: 0.2-1]
##can be solid or vertical strip: [line: 15-80, lw: 1-5, alpha: 0.2-1]
##bg_noise can be added: [#scattered: 5-60, alpha: 0.1-0.7, color: {blue, purple, green, yellow, grey}]
def generator0(total_num, path, dpi=100, cross_ratio=0.5, vertical_ratio=0.5, bg_ratio=0.8):
    color_map = ['blue', 'purple', 'green', 'yellow', 'grey']
    for i in range(total_num):
        h = np.random.uniform(0.5, 2.5)
        alpha = np.random.uniform(0.2, 1)
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
        img = class0image(h, alpha, cross_noise=cn, fill=fill, vertical=vertical, bg_noise=bg_noise)
        img.plot_save(path + "/class0_{}".format(i), dpi=dpi)


if __name__ == "__main__":
    generator0(200, path='./test/class0', dpi=70)