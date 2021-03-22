class CaloricBalance:
    def __init__(self,g,a,h,w):
        self.g = g
        self.a = float(a)
        self.h = float(h)
        self.w = float(w)
        self.b = -1*self.getBMR(g,a,h,w)
    def getBMR(self,g,a,h,w):
        if g == 'm':
            return 66 + (12.7 * h) + (6.23 * w) - (6.8 * a)
        elif g == 'f':
            return 655 + (4.7 * h) + (4.35 * w) - (4.7 * a)
        else:
            return 0
    def getBalance(self):
        return self.b
    def recordActivity(self,calories_burnt,min):
        self.b -= self.w*calories_burnt*min
    def eatFood(self,food):
        self.b += food
