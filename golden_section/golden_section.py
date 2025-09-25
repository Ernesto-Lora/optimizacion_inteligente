# Golden-section search

def f(x):
    return x**2 +54/x

def x(om, a, b):
    return (b-a)*om +a


def transformed_function(om,a,b,f):
    return f( (b-a)*om +a) 

def custom_print(aw, bw, k):
    print(f"Iteration {k}")
    print(f"Current interval (in the (0,1) range): [{aw:.6f}, {bw:.6f}]")
    print(f"Interval length (Lw): {bw - aw:.6f}")
    print("-" * 40)


def golden_section(a,b,epsilon,f):
    print(f"The initial interval is [{a:.6f}, {b:.6f}]")
    aw = 0
    bw = 1
    lw = bw-aw
    k=0
    w1 = aw+0.618*lw
    w2=bw-0.618*lw
    f1 = transformed_function(w1,a,b,f)
    f2 = transformed_function(w2,a,b,f)
    while(lw>=epsilon):
        w1 = aw+0.618*lw
        w2=bw-0.618*lw
        print(w1,w2)
        if (transformed_function(w1,a,b,f) < transformed_function(w2,a,b,f)):
            aw = w2
            custom_print(aw,bw,k)
        else:
            bw = w1
            custom_print(aw,bw,k)
        lw = bw-aw
        k += 1
    print(f"Returning the values [{x(aw, a, b):.6f}, {x(bw, a, b):.6f}]")
    return x(aw, a ,b), x(bw, a ,b)

if __name__ == "__main__":
    golden_section(0,5,0.1,f)