from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets
def func(x):
    return x**2

print(interact(func,x=10))

@interact(x=True,y=0.1)
def g(x,y):
    return (x,y)

fwfwf= g
print(fwfwf)

w = widgets.IntSlider()
from IPython.display import display
display(w)

