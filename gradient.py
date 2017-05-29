from numpy import *

#defining the error computing function
def compute_error_for_given_point(b,m,points):
    totalError=0
    for i in range(0,len(points)):
        x=points[i,0]
        y=points[i,1]
        totalError += (y-(m*x+b))**2
    return totalError/float(len(points))

#doing the minimization process for the error 
def step_gradient(b_current,m_current,points,learning_rate):
    b_gradient=0
    m_gradient=0
    N=float(len(points))
    for i in range(0,len(points)):
        x=points[i,0]
        y=points[i,1]
        b_gradient += -(2/N)*(y-((m_current*x)+b_current))
        m_gradient += -(2/N)*x*(y-((m_current*x)+b_current))
    new_b=b_current-(learning_rate*b_gradient)
    new_m=m_current-(learning_rate*m_gradient)
    return [new_b, new_m]

#forming an array out of the points fetched from the data.
def gradient_descent_runner(points,starting_b,starting_m,learning_rate,num_of_iterations):
    b=starting_b
    m=starting_m
    for i in range(num_of_iterations):
        b, m = step_gradient(b,m,array(points),learning_rate)
    return [b, m]

#fetching the values from the data set and setting up the learning rate and other parameters for best fit line.
def run():
    points = genfromtxt('data.csv',delimiter=',')
    learning_rate=0.0001
    #y=mx+b(slope formula)
    initial_b=0
    initial_m=0
    num_of_iterations=1000
    [b, m]=gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_of_iterations)
    print 'after {0} iterations b={1},m={2} and the error is {3}'.format(num_of_iterations,b,m,compute_error_for_given_point(b,m,points))

if __name__=='__main__':
        run()
