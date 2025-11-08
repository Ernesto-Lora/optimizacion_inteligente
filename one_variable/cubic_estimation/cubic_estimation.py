# Cubic estimation
import math
def f(x):
    return (x**2 +54/x)

def get_x_test(x1,x2,mu):
    if (mu == 0):
        return x2
    elif(mu > 1):
        return x1
    else:
        return x2-mu*(x2-x1)

def get_mu(x1,x2,f1,f2,fp_1,fp_2):
    z = 3*(f1-f2)/(x2-x1) +fp_1+fp_2
    omega = ((x2-x1)/abs(x2-x1))*math.sqrt(z**2 - fp_1*fp_2)
    return (fp_2+omega-z)/(fp_2-fp_1+2*omega)

def first_derivative(f1,f2,delta):
    return (f1-f2)/(2*delta)


def cubic_estimation(x1, step_delta, epsilon, delta, f):
    print(f"Initial Point: {x1}")
    print(f"Step delta of: {step_delta}")
    print(f"With both tolerance epsilon: {epsilon}")
    print(f"With Delta for the numeric derivatives: {delta}")
    
    fp_x1 = first_derivative(f1 = f(x1+delta), f2 = f(x1-delta), delta=delta)
    if fp_x1>0:
        step_delta *= -1
    k=0
    while True: #Do-while implementation
        x2 = x1+2**k*step_delta
        fp_x2 = first_derivative(f1 = f(x2+delta), f2 = f(x2-delta), delta=delta)
        if fp_x1*fp_x2 <= 0:
            break
        fp_x1 = fp_x2
        x1 = x2
        k += 1 

    f1  = f(x1)
    f2 = f(x2)
    i = 1
    while True:
        mu = get_mu(x1=x1, x2=x2, f1=f1, f2=f2,fp_1=fp_x1, fp_2=fp_x2)
        x_test = get_x_test(x1=x1, x2=x2, mu=mu)
        f_x_test = f(x_test)

        print(f"Iteration {i}. New optimum candidate: {x_test} ")

        while not(f_x_test<=f1):
            x_test = x_test-0.5*(x_test-x1)
            f_x_test = f(x_test)

        #step 6
        fp_x_test = first_derivative(f1 = f(x_test+delta), f2=f(x_test-delta), delta=delta)
        if abs(fp_x_test) <= epsilon and abs((x_test-x1)/x_test)<=epsilon:
            break
        elif ( fp_x_test*fp_x1<0 ):
            x2 = x_test
            f2 = f_x_test
            fp_x2 = fp_x_test
        else:
            x1 = x_test
            f1 = f_x_test
            fp_x1 = fp_x_test
        i += 1

    
        if i>50:
            break

    print(f"Returning the optimum candidate: {x_test}")

    return x_test

if __name__ == "__main__":
    x1 = float(input('Enter x0: '))
    step_delta = float(input('Enter the Delta step: '))
    epsilon = float(input('Enter tolerance "epsilon": '))
    delta = float(input('Enter delta for numeric derivative : '))
    cubic_estimation(x1=x1,step_delta=step_delta,epsilon=epsilon,delta=delta, f=f)