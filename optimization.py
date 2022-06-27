from pydoc import visiblename
import sistema_massa_mola as sys
import numpy as np
import math

def objetivo(s):
    return max(s[4])

def S_init():
    ti=0; tf=2;h=0.005 
    m1=1.94; m2=0.10; x11=1.2; x12=-1.3; x21=1.4; x22=1.5
    K1=10
    q=[0.91,1.01,0.89,1.04]

    

    return q,ti,tf,h,m1,m2,x11,x12,x21,x22,K1

def SA():
    alpha =0.90
    it = 10
    Tf = 1
    T0 = 10
    s=S_init()
    sol_ini=sys.system(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10])
    lbl="Solucao Inicial"
    sys.printer(sol_ini[0],sol_ini[1],sol_ini[2],sol_ini[3],sol_ini[4],lbl)
    valor=objetivo(sol_ini)
    print("Valor inicial:", valor)
    
    Xb = s
    xxb=valor

    T = T0
    while T >= Tf:
        for i in range(it):
            #print('-----------------ITERAÇÃO------------------')
            xx=objetivo(sol_ini)
            Y=s
            rd = np.random.randint(0,1)
            if rd == 0:
                N1(Y)
                
            elif rd == 1:
                N_2(Y)


            s_aux=sys.system(Y[0],Y[1],Y[2],Y[3],Y[4],Y[5],Y[6],Y[7],Y[8],Y[9],Y[10])
            yy=objetivo(s_aux)
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
    s=SOL    
    solucao=sys.system(s[0],s[1],s[2],s[3],s[4],s[5],s[6],s[7],s[8],s[9],s[10])
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