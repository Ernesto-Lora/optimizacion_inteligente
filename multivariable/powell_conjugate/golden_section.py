# Golden-section search

def f(x):
    return x**2 +54/x

def x(om, a, b):
    return (b-a)*om +a


def transformed_function(om,a,b,f):
    return f( (b-a)*om +a) 

def custom_print(aw, bw, a,b ,k):
    print(f"Iteration {k}")
    print(f"Interval found (in the (1,0) range): [{aw:.6f}, {bw:.6f}]")
    print(f"Interval length (Lw): {bw - aw:.6f}")
    print(f"Interval found: [{x(aw, a, b):.6f}, {x(bw, a, b):.6f}]")
    print(f"Interval length (L): {(bw - aw)*(b-a):.6f}")
    print("-" * 40)


def golden_section(a,b,epsilon,f):
    if b<a:
        c=a
        a=b
        b =c
    print(f"The initial interval is [{a:.6f}, {b:.6f}]")
    print(f"With a tolerance of {epsilon}")
    aw = 0
    bw = 1
    lw = bw-aw
    k=0
    w1 = aw+0.618*lw
    w2=bw-0.618*lw
    f1 = transformed_function(w1,a,b,f)
    f2 = transformed_function(w2,a,b,f)
    while(lw*(b-a)>=epsilon):
        if (f1 < f2):
            aw = w2
            w2 = w1
            f2 = f1
            lw = bw-aw #new lw
            w1 = aw+0.618*lw
            f1 = transformed_function(w1,a,b,f)
            custom_print(aw,bw,a,b,k)
        else:
            bw = w1
            w1 = w2
            f1 = f2
            lw = bw-aw #new lw
            w2=bw-0.618*lw
            f2 = transformed_function(w2,a,b,f)
            custom_print(aw,bw,a,b,k)
        lw = bw-aw
        k += 1
    #print(f"Returning the values [{x(aw, a, b)}, {x(bw, a, b)}]")
    print(f"Returning the values [{x(aw, a, b):.6f}, {x(bw, a, b):.6f}]")
    return x(aw, a ,b)

if __name__ == "__main__":
    a = float(input('Enter the value of "a" (lower bound): '))
    b = float(input('Enter the value of "b" (upper bound): '))
    epsilon = int(input('Enter the precision "epsilon": '))

    golden_section(a=a, b=b, epsilon=epsilon, f=f)
