def square (x):
    return x**2
def maxer(fumes):
    def fire(y):
        y=fumes(y)
        def haze(z):
            if fumes(z)<y:
                z=y
            print(z)
            return haze
        return haze
    return fire
print(maxer(square)(1)(2)(3)(4))