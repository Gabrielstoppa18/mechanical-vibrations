from pydoc import visiblename
import sistema_massa_mola as sys
import numpy as np
import math

def objetivo(s):
    g=sys.system(s[0],s[1],s[2])
    return max(g[4])

def S_init():
    m1=1.94; m2=0.10; 
    q=[0.91,1.01,0.89,1.04]

    return q,m1,m2

def SA():
    alpha =0.90
    it = 10
    Tf = 1
    T0 = 10
    s=S_init()
    lbl="Solucao Inicial"
    k=sys.system(s[0],s[1],s[2])
    sys.printer(k[0],k[1],k[2],k[3],k[4],lbl)
    valor=objetivo(s)
    print("Valor inicial:", valor)
    
    Xb = s
    xxb=valor

    T = T0
    while T >= Tf:
        for i in range(it):
            #print('-----------------ITERAÇÃO------------------')
            xx=objetivo(s)
            Y=s
            rd = np.random.randint(0,1)
            if rd == 0:
                N1(Y)
                
            elif rd == 1:
                N_2(Y)
            yy=objetivo(Y)
            delta = yy-xx
            if delta <= 0:
                SOL = Y
                xx = yy
            else:
                rr = (np.random.randint(0,100))/100
                if rr < math.exp(-delta/T):
                    SOL = Y
                    xx = yy
            if xx < xxb:
                Xb = SOL
                xxb = xx
            #print(xxb)
        T=alpha*T
    s=Xb    
    solucao=sys.system(s[0],s[1],s[2])
    print("Valor final: ", max(solucao[4]))
    label="-Solução Final do Problema:"
    sys.printer(solucao[0],solucao[1],solucao[2],solucao[3],solucao[4],label)
    

     
def N1(s):
    i=np.random.randint(0,3)
    k=s[0][i]
    j=random_neighbour(k)
    if j ==0:
        return
    s[0][i]=j 

def N_2(s):
    k=s[4]
    j=random_neighbour(k)
    if j ==0:
        return
    s[4]=j
    i=s[5]
    l=random_neighbour(i)
    if l ==0:
        return
    s[5]=l



def random_neighbour(x, fraction=1):
    """Move a little bit x, from the left or the right."""
    amplitude = fraction / 10
    delta = (-amplitude/2.) + amplitude * np.random.random_sample()
    return x+delta
SA()