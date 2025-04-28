import matplotlib.pyplot as plt
import numpy as np
import math #if needed

def graph(xlist=None,ylist=None,color=None,show=None):
    if min(ylist)!=max(ylist):
        plt.ylim(min(ylist), max(ylist))
    if min(xlist)!=max(xlist):
        plt.xlim(min(xlist), max(xlist))

    xcoords=np.array(xlist)
    ycoords=np.array(ylist)
    if xlist==None or ylist==None:
        return("Error: No x or y values passed. Pass two equally-sized arrays for x and y")
    elif color==None:
        plt.plot(xcoords,ycoords,"red")
    else:
        plt.plot(xcoords,ycoords,color=color)

    if show==True:
        plt.show()

def show():
    plt.show()
#def yrange(ylist):
#    plt.xlim(min(xlist), max(xlist))
#def xrange(xlist):
#    plt.xlim(min(xlist), max(xlist))

def generate_array_then_graph(minimum_x=None,maximum_x=None,f=None,incrementsperunit=None,color=None,show=None):#reciprocal step can also be thought of as gradings between 0 and 1. So the gradings is 100
    if f==None or str(type(minimum_x))=="<class 'float'>" or str(type(maximum_x))=="<class 'float'>" or incrementsperunit==None: #plan is to make parametric using carrier as t and then passing equation of x through
        print("missing/incorrect: one of the first 4 required arguments")
        return()
    min_x=minimum_x
    max_x=maximum_x
    reciprocal_step=incrementsperunit #so this is a step of 0.01 if reciprocal_step=100

#data generation
    #cartesian only
    coords_x=[]
    coords_y=[]

    for carrier in range((min_x*reciprocal_step),((max_x)*reciprocal_step)+1,1):#+1 as the last value is not reached (start, iterations, step)
        #print(carrier)
        x=carrier/reciprocal_step
        coords_x.append(x)
        #merged loops together to perform quicker time
        y=f(x)
        coords_y.append(y)#inside of bracket is the equation

    #yrange(coords_y)
    #xrange(coords_x)
#then graphing
    graph(coords_x,coords_y,color,show)

def parametric_graph():
    print("Behind the scenes... NOT FINISHED CRTL+C THIS RN")
def test():
    print("program is working at optimal condition---END OF TEST")