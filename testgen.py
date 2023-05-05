import numpy as np
from matplotlib import pyplot as plt

#utility function 
def construct_ys(max_y, num_lines):
    ys = 0
    if num_lines%2 == 0:
        ys = np.arange(-max_y, max_y+0.01, 2*max_y/(num_lines/2-1))
        ys = np.array([*ys, *np.flip(ys)])
    else:
        ys = np.arange(-max_y, max_y-0.01, 2*max_y/((num_lines+1)/2-1))
        ys = np.array([*ys, max_y, *np.flip(ys)])
    return ys


##test image that gives illusion of class 1 objects
class TestClass1:
    def __init__(self, num_lines=35, v_lw=1.5, theta=15, h=0.6, a_lw=1.5, v_alpha=1, a_alpha=0.8):
        '''
        Parameters
        ==========
        num_lines: int, default 35
            The number of vertical lines in the plot
        v_lw: float, default 1.5
            The linewidth of the vertical lines
        theta: float/int, default 15
            The smallest angle between the arrow line and the vertical line
        h: float, default 0.6
            The height of each vertical lines, such that each line has a length of 2h
        a_lw: float, default 1.5
            The linewidth of the arrow lines
        v_alpha: float, default 1
            The alpha value of the vertical lines 
        a_alpha: float, default 0.8
            The alpha value of the arrow lines
        
        '''
        self.num_lines = num_lines
        self.v_lw=v_lw
        self.theta = (theta/180)*np.pi
        self.h = h
        self.a_lw = a_lw
        self.v_alpha = v_alpha
        self.a_alpha = a_alpha

    def plot(self):
        ##x-positions of num_lines vertical lines
        plt.figure(figsize=(347/60, 258/60))
        dis = 13/(self.num_lines-1)
        x_lab = np.arange(-6.5, 6.5+0.01, dis)
        max_angle = np.pi/2 - self.theta
        interval = dis*0.43
        max_y = interval*np.tan(max_angle)
        if self.num_lines%2 == 0:
            ys = np.arange(-max_y, max_y+0.01, 2*max_y/(self.num_lines/2 - 1))
            ys = np.array([*ys, *np.flip(ys)])
        else:
            ys = np.arange(-max_y, max_y-0.001, 2*max_y/((self.num_lines+1)/2 - 1))
            ys = np.array([*ys, max_y, *np.flip(ys)])
        plt.axis('off')
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        plt.axis('equal')
        for i, x in enumerate(x_lab):
            interval = dis*0.43
            plt.plot([x, x], [-self.h, self.h], c='red', alpha=self.v_alpha, lw=self.v_lw, zorder=10)
            upper_y = self.h+ys[i]; lower_y = -self.h-ys[i]
            if upper_y < lower_y:
                ratio = self.h/abs(ys[i])
                interval = interval*ratio
                upper_y = 0.02
                lower_y = -0.02
            plt.plot([x, x+interval], [self.h, upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [self.h, upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x+interval], [-self.h, lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [-self.h, lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)

    def plot_show(self):
        self.plot()
        plt.show()

    def plot_save(self, path, dpi=100):
        self.plot()
        plt.margins(0,0)
        plt.tight_layout()
        plt.savefig(path, dpi=dpi, bbox_inches='tight', pad_inches = 0)
        plt.close()

##test image that gives illusion of class 3 objects
class TestClass3:
    def __init__(self, num_lines=35, v_lw=1.5, theta=15, h=0.6, a_lw=1.5, v_alpha=1, a_alpha=0.8):
        '''
        Parameters
        ==========
        num_lines: int, default 35
            The number of vertical lines in the plot
        v_lw: float, default 1.5
            The linewidth of the vertical lines
        theta: float/int, default 15
            The smallest angle between the arrow line and the vertical line
        h: float, default 0.6
            The height of each vertical lines, such that each line has a length of 2h
        a_lw: float, default 1.5
            The linewidth of the arrow lines
        v_alpha: float, default 1
            The alpha value of the vertical lines 
        a_alpha: float, default 0.8
            The alpha value of the arrow lines
        
        '''
        self.num_lines = num_lines
        self.v_lw=v_lw
        self.theta = (theta/180)*np.pi
        self.h = h
        self.a_lw = a_lw
        self.v_alpha = v_alpha
        self.a_alpha = a_alpha

    def plot(self):
        ##x-positions of num_lines vertical lines
        plt.figure(figsize=(347/60, 258/60))
        dis = 13/(self.num_lines-1)
        x_lab = np.arange(-6.5, 6.5+0.01, dis)
        max_angle = np.pi/2 - self.theta
        interval = dis*0.43
        max_y = interval*np.tan(max_angle)
        if self.num_lines%2 == 0:
            ys = np.arange(-max_y, max_y+0.01, 2*max_y/(self.num_lines/2 - 1))
            ys = np.array([*ys, *np.flip(ys)])
        else:
            ys = np.arange(-max_y, max_y-0.001, 2*max_y/((self.num_lines+1)/2 - 1))
            ys = np.array([*ys, max_y, *np.flip(ys)])
        plt.axis('off')
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        plt.axis('equal')
        for i, x in enumerate(x_lab):
            interval = dis*0.43
            plt.plot([x, x], [-self.h, self.h], c='red', alpha=self.v_alpha, lw=self.v_lw, zorder=10)
            upper_y = self.h-ys[i]; lower_y = -self.h+ys[i]
            if upper_y < lower_y:
                ratio = self.h/abs(ys[i])
                interval = interval*ratio
                upper_y = 0.02
                lower_y = -0.02
            plt.plot([x, x+interval], [self.h, upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [self.h, upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x+interval], [-self.h, lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [-self.h, lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)

    def plot_show(self):
        self.plot()
        plt.show()

    def plot_save(self, path, dpi=100):
        self.plot()
        plt.margins(0,0)
        plt.tight_layout()
        plt.savefig(path, dpi=dpi, bbox_inches='tight', pad_inches = 0)
        plt.close()

##test image that gives illusion of class 2 objects
class TestClass2:
    def __init__(self, num_lines=35, v_lw=1.5, theta=15, h=0.6, a_lw=1.5, v_alpha=1, a_alpha=0.8):
        '''
        Parameters
        ==========
        num_lines: int, default 35
            The number of vertical lines in the plot
        v_lw: float, default 1.5
            The linewidth of the vertical lines
        theta: float/int, default 15
            The smallest angle between the arrow line and the vertical line
        h: float, default 0.6
            The height of each vertical lines, such that each line has a length of 2h
        a_lw: float, default 1.5
            The linewidth of the arrow lines
        v_alpha: float, default 1
            The alpha value of the vertical lines 
        a_alpha: float, default 0.8
            The alpha value of the arrow lines
        
        '''
        self.num_lines = num_lines
        self.v_lw=v_lw
        self.theta = (theta/180)*np.pi
        self.h = h
        self.a_lw = a_lw
        self.v_alpha = v_alpha
        self.a_alpha = a_alpha

    def plot(self):
        ##x-positions of num_lines vertical lines
        plt.figure(figsize=(347/60, 258/60))
        dis = 13/(self.num_lines-1)
        x_lab = np.arange(-6.5, 6.5+0.01, dis)
        max_angle = np.pi/2 - self.theta
        interval = dis*0.43
        max_y = interval*np.tan(max_angle)
        if self.num_lines%2 == 0:
            ys = construct_ys(max_y, self.num_lines/2)
            ys = np.array([*ys, *ys])
        else:
            ys = construct_ys(max_y, (self.num_lines+1)/2)
            ys = np.array([*ys, *ys])[1:]
        plt.axis('off')
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        plt.axis('equal')
        for i, x in enumerate(x_lab):
            interval = dis*0.43
            plt.plot([x, x], [-self.h, self.h], c='red', alpha=self.v_alpha, lw=self.v_lw, zorder=10)
            upper_y = self.h+ys[i]; lower_y = -self.h-ys[i]
            if upper_y < lower_y:
                ratio = self.h/abs(ys[i])
                interval = interval*ratio
                upper_y = 0.02
                lower_y = -0.02
            plt.plot([x, x+interval], [self.h, upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [self.h, upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x+interval], [-self.h, lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [-self.h, lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)

    def plot_show(self):
        self.plot()
        plt.show()

    def plot_save(self, path, dpi=100):
        self.plot()
        plt.margins(0,0)
        plt.tight_layout()
        plt.savefig(path, dpi=dpi, bbox_inches='tight', pad_inches = 0)
        plt.close()
        
class CheckClass1:
    def __init__(self, num_lines=35, v_lw=1.5, theta=15, h=0.6, a_lw=1.5, v_alpha=1, a_alpha=0.8):
        '''
        Parameters
        ==========
        num_lines: int, default 35
            The number of vertical lines in the plot
        v_lw: float, default 1.5
            The linewidth of the vertical lines
        theta: float/int, default 15
            The smallest angle between the arrow line and the vertical line
        h: float, default 0.6
            The height of each vertical lines, such that each line has a length of 2h
        a_lw: float, default 1.5
            The linewidth of the arrow lines
        v_alpha: float, default 1
            The alpha value of the vertical lines 
        a_alpha: float, default 0.8
            The alpha value of the arrow lines
        
        '''
        self.num_lines = num_lines
        self.v_lw=v_lw
        self.theta = (theta/180)*np.pi
        self.h = h
        self.a_lw = a_lw
        self.v_alpha = v_alpha
        self.a_alpha = a_alpha

    def plot(self):
        ##x-positions of num_lines vertical lines
        plt.figure(figsize=(347/60, 258/60))
        dis = 13/(self.num_lines-1)
        x_lab = np.arange(-6.5, 6.5+0.01, dis)
        max_angle = np.pi/2 - self.theta
        interval = dis*0.43
        max_y = interval*np.tan(max_angle)
        if self.num_lines%2 == 0:
            ys = np.arange(-max_y, max_y+0.01, 2*max_y/(self.num_lines/2 - 1))
            ys = np.array([*ys, *np.flip(ys)])
        else:
            ys = np.arange(-max_y, max_y-0.001, 2*max_y/((self.num_lines+1)/2 - 1))
            ys = np.array([*ys, max_y, *np.flip(ys)])
        plt.axis('off')
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        plt.axis('equal')
        for i, x in enumerate(x_lab):
            interval = dis*0.43
            plt.plot([x, x], [-self.h, self.h], c='red', alpha=self.v_alpha, lw=self.v_lw, zorder=10)
            upper_y = self.h+ys[i]; lower_y = -self.h-ys[i]
            if upper_y < lower_y:
                ratio = self.h/abs(ys[i])
                interval = interval*ratio
                upper_y = 0.02
                lower_y = -0.02
            plt.plot([x, x+interval], [2*self.h, self.h + upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [2*self.h, self.h + upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x+interval], [-2*self.h, -self.h + lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [-2*self.h, -self.h + lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)

    def plot_show(self):
        self.plot()
        plt.show()

    def plot_save(self, path, dpi=100):
        self.plot()
        plt.margins(0,0)
        plt.tight_layout()
        plt.savefig(path, dpi=dpi, bbox_inches='tight', pad_inches = 0)
        plt.close()
        
class CheckClass2:
    def __init__(self, num_lines=35, v_lw=1.5, theta=15, h=0.6, a_lw=1.5, v_alpha=1, a_alpha=0.8):
        '''
        Parameters
        ==========
        num_lines: int, default 35
            The number of vertical lines in the plot
        v_lw: float, default 1.5
            The linewidth of the vertical lines
        theta: float/int, default 15
            The smallest angle between the arrow line and the vertical line
        h: float, default 0.6
            The height of each vertical lines, such that each line has a length of 2h
        a_lw: float, default 1.5
            The linewidth of the arrow lines
        v_alpha: float, default 1
            The alpha value of the vertical lines 
        a_alpha: float, default 0.8
            The alpha value of the arrow lines
        
        '''
        self.num_lines = num_lines
        self.v_lw=v_lw
        self.theta = (theta/180)*np.pi
        self.h = h
        self.a_lw = a_lw
        self.v_alpha = v_alpha
        self.a_alpha = a_alpha

    def plot(self):
        ##x-positions of num_lines vertical lines
        plt.figure(figsize=(347/60, 258/60))
        dis = 13/(self.num_lines-1)
        x_lab = np.arange(-6.5, 6.5+0.01, dis)
        max_angle = np.pi/2 - self.theta
        interval = dis*0.43
        max_y = interval*np.tan(max_angle)
        if self.num_lines%2 == 0:
            ys = construct_ys(max_y, self.num_lines/2)
            ys = np.array([*ys, *ys])
        else:
            ys = construct_ys(max_y, (self.num_lines+1)/2)
            ys = np.array([*ys, *ys])[1:]
        plt.axis('off')
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        plt.axis('equal')
        for i, x in enumerate(x_lab):
            interval = dis*0.43
            plt.plot([x, x], [-self.h, self.h], c='red', alpha=self.v_alpha, lw=self.v_lw, zorder=10)
            upper_y = self.h+ys[i]; lower_y = -self.h-ys[i]
            if upper_y < lower_y:
                ratio = self.h/abs(ys[i])
                interval = interval*ratio
                upper_y = 0.02
                lower_y = -0.02
            plt.plot([x, x+interval], [2*self.h, self.h+upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [2*self.h, self.h+upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x+interval], [-2*self.h, -self.h + lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [-2*self.h, -self.h + lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)

    def plot_show(self):
        self.plot()
        plt.show()

    def plot_save(self, path, dpi=100):
        self.plot()
        plt.margins(0,0)
        plt.tight_layout()
        plt.savefig(path, dpi=dpi, bbox_inches='tight', pad_inches = 0)
        plt.close()
        
class CheckClass3:
    def __init__(self, num_lines=35, v_lw=1.5, theta=15, h=0.6, a_lw=1.5, v_alpha=1, a_alpha=0.8):
        '''
        Parameters
        ==========
        num_lines: int, default 35
            The number of vertical lines in the plot
        v_lw: float, default 1.5
            The linewidth of the vertical lines
        theta: float/int, default 15
            The smallest angle between the arrow line and the vertical line
        h: float, default 0.6
            The height of each vertical lines, such that each line has a length of 2h
        a_lw: float, default 1.5
            The linewidth of the arrow lines
        v_alpha: float, default 1
            The alpha value of the vertical lines 
        a_alpha: float, default 0.8
            The alpha value of the arrow lines
        
        '''
        self.num_lines = num_lines
        self.v_lw=v_lw
        self.theta = (theta/180)*np.pi
        self.h = h
        self.a_lw = a_lw
        self.v_alpha = v_alpha
        self.a_alpha = a_alpha

    def plot(self):
        ##x-positions of num_lines vertical lines
        plt.figure(figsize=(347/60, 258/60))
        dis = 13/(self.num_lines-1)
        x_lab = np.arange(-6.5, 6.5+0.01, dis)
        max_angle = np.pi/2 - self.theta
        interval = dis*0.43
        max_y = interval*np.tan(max_angle)
        if self.num_lines%2 == 0:
            ys = np.arange(-max_y, max_y+0.01, 2*max_y/(self.num_lines/2 - 1))
            ys = np.array([*ys, *np.flip(ys)])
        else:
            ys = np.arange(-max_y, max_y-0.001, 2*max_y/((self.num_lines+1)/2 - 1))
            ys = np.array([*ys, max_y, *np.flip(ys)])
        plt.axis('off')
        plt.ylim(-5, 5)
        plt.xlim(-5, 5)
        plt.axis('equal')
        for i, x in enumerate(x_lab):
            interval = dis*0.43
            plt.plot([x, x], [-self.h, self.h], c='red', alpha=self.v_alpha, lw=self.v_lw, zorder=10)
            upper_y = self.h-ys[i]; lower_y = -self.h+ys[i]
            if upper_y < lower_y:
                ratio = self.h/abs(ys[i])
                interval = interval*ratio
                upper_y = 0.02
                lower_y = -0.02
            plt.plot([x, x+interval], [2*self.h, self.h+upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [2*self.h, self.h+upper_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x+interval], [-2*self.h, -self.h+lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)
            plt.plot([x, x-interval], [-2*self.h, -self.h+lower_y], c='black', alpha=self.a_alpha, lw=self.a_lw, zorder=1)

    def plot_show(self):
        self.plot()
        plt.show()

    def plot_save(self, path, dpi=100):
        self.plot()
        plt.margins(0,0)
        plt.tight_layout()
        plt.savefig(path, dpi=dpi, bbox_inches='tight', pad_inches = 0)
        plt.close()



##num_test must be a multiple of 450
def class1_generator(path, num_tests=5*450):
    for nl in range(15, 45):
        for h in np.arange(0.6, 2.1, 0.1):
            for i in range(int(num_tests/450)):
                if nl > 30:
                    v_lw = np.random.uniform(1, 3)
                else:
                    v_lw = np.random.uniform(2, 4)
                a_lw = 0.75*v_lw
                v_alpha = np.random.uniform(0.6, 1)
                a_alpha = np.random.uniform(0.4, 0.7)
                theta = np.random.uniform(12, 25)
                img = TestClass1(num_lines=nl, v_lw=v_lw, theta=theta, h=h, a_lw = a_lw, v_alpha=v_alpha, 
                                 a_alpha=a_alpha)
                path_tosave = path + "/class1_nl{}_vlw{}_theta{}_h{}_alw{}_va{}_aa{}.png".format(nl, round(v_lw,1),
                                        round(theta, 1), round(h, 1), round(a_lw, 1), round(v_alpha, 2), round(a_alpha, 2))
                img.plot_save(path_tosave, dpi=70)

##num_test must be a multiple of 450
def class3_generator(path, num_tests=5*450):
    for nl in range(15, 45):
        for h in np.arange(0.6, 2.1, 0.1):
            for i in range(int(num_tests/450)):
                if nl > 30:
                    v_lw = np.random.uniform(1, 3)
                else:
                    v_lw = np.random.uniform(2, 4)
                a_lw = 0.75*v_lw
                v_alpha = np.random.uniform(0.6, 1)
                a_alpha = np.random.uniform(0.4, 0.7)
                theta = np.random.uniform(12, 25)
                img = TestClass3(num_lines=nl, v_lw=v_lw, theta=theta, h=h, a_lw = a_lw, v_alpha=v_alpha, 
                                 a_alpha=a_alpha)
                path_tosave = path + "/class3_nl{}_vlw{}_theta{}_h{}_alw{}_va{}_aa{}.png".format(nl, round(v_lw,1),
                                        round(theta, 1), round(h, 1), round(a_lw, 1), round(v_alpha, 2), round(a_alpha, 2))
                img.plot_save(path_tosave, dpi=70)

##num_test must be a multiple of 450
def class2_generator(path, num_tests=5*450):
    for nl in range(20, 50):
        for h in np.arange(0.6, 2.1, 0.1):
            for i in range(int(num_tests/450)):
                if nl > 30:
                    v_lw = np.random.uniform(1, 3)
                else:
                    v_lw = np.random.uniform(2, 4)
                a_lw = 0.75*v_lw
                v_alpha = np.random.uniform(0.6, 1)
                a_alpha = np.random.uniform(0.4, 0.7)
                theta = np.random.uniform(12, 25)
                img = TestClass2(num_lines=nl, v_lw=v_lw, theta=theta, h=h, a_lw = a_lw, v_alpha=v_alpha, 
                                 a_alpha=a_alpha)
                path_tosave = path + "/class2_nl{}_vlw{}_theta{}_h{}_alw{}_va{}_aa{}.png".format(nl, round(v_lw,1),
                                        round(theta, 1), round(h, 1), round(a_lw, 1), round(v_alpha, 2), round(a_alpha, 2))
                img.plot_save(path_tosave, dpi=70)
                
                
##num_test must be a multiple of 450
def check1_generator(path, num_tests=5*450):
    for nl in range(15, 45):
        for h in np.arange(0.6, 2.1, 0.1):
            for i in range(int(num_tests/450)):
                if nl > 30:
                    v_lw = np.random.uniform(1, 3)
                else:
                    v_lw = np.random.uniform(2, 4)
                a_lw = 0.75*v_lw
                v_alpha = np.random.uniform(0.6, 1)
                a_alpha = np.random.uniform(0.4, 0.7)
                theta = np.random.uniform(12, 25)
                img = CheckClass1(num_lines=nl, v_lw=v_lw, theta=theta, h=h, a_lw = a_lw, v_alpha=v_alpha, 
                                 a_alpha=a_alpha)
                path_tosave = path + "/check1_nl{}_vlw{}_theta{}_h{}_alw{}_va{}_aa{}.png".format(nl, round(v_lw,1),
                                        round(theta, 1), round(h, 1), round(a_lw, 1), round(v_alpha, 2), round(a_alpha, 2))
                img.plot_save(path_tosave, dpi=70)
             
##num_test must be a multiple of 450
def check3_generator(path, num_tests=5*450):
    for nl in range(15, 45):
        for h in np.arange(0.6, 2.1, 0.1):
            for i in range(int(num_tests/450)):
                if nl > 30:
                    v_lw = np.random.uniform(1, 3)
                else:
                    v_lw = np.random.uniform(2, 4)
                a_lw = 0.75*v_lw
                v_alpha = np.random.uniform(0.6, 1)
                a_alpha = np.random.uniform(0.4, 0.7)
                theta = np.random.uniform(12, 25)
                img = CheckClass3(num_lines=nl, v_lw=v_lw, theta=theta, h=h, a_lw = a_lw, v_alpha=v_alpha, 
                                 a_alpha=a_alpha)
                path_tosave = path + "/check3_nl{}_vlw{}_theta{}_h{}_alw{}_va{}_aa{}.png".format(nl, round(v_lw,1),
                                        round(theta, 1), round(h, 1), round(a_lw, 1), round(v_alpha, 2), round(a_alpha, 2))
                img.plot_save(path_tosave, dpi=70)
                
##num_test must be a multiple of 450
def check2_generator(path, num_tests=5*450):
    for nl in range(20, 50):
        for h in np.arange(0.6, 2.1, 0.1):
            for i in range(int(num_tests/450)):
                if nl > 30:
                    v_lw = np.random.uniform(1, 3)
                else:
                    v_lw = np.random.uniform(2, 4)
                a_lw = 0.75*v_lw
                v_alpha = np.random.uniform(0.6, 1)
                a_alpha = np.random.uniform(0.4, 0.7)
                theta = np.random.uniform(12, 25)
                img = CheckClass2(num_lines=nl, v_lw=v_lw, theta=theta, h=h, a_lw = a_lw, v_alpha=v_alpha, 
                                 a_alpha=a_alpha)
                path_tosave = path + "/check2_nl{}_vlw{}_theta{}_h{}_alw{}_va{}_aa{}.png".format(nl, round(v_lw,1),
                                        round(theta, 1), round(h, 1), round(a_lw, 1), round(v_alpha, 2), round(a_alpha, 2))
                img.plot_save(path_tosave, dpi=70)


if __name__ == '__main__':
#     class1_generator('./test/class1', num_tests=4*450)
#     class3_generator('./test/class3', num_tests=4*450)
#     class2_generator('./test/class2', num_tests=4*450)
    check1_generator('./test/check1', num_tests=4*450)
    check3_generator('./test/check3', num_tests=4*450)
    check2_generator('./test/check2', num_tests=4*450)
    
    
    
    
    
    
    
    