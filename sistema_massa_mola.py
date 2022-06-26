import numpy as np
import matplotlib.pyplot as plt

#deslocamento da massa 1
q1=[]
q1.append(0.91)

#angulo da massa 2
q2=[]
q2.append(1.01)

#velocidade da massa 1
q3=[]
q3.append(0.89)

#velocidade da massa 2
q4=[]
q4.append(1.04)
ti=0; tf=1.5;h=0.005 
t=np.arange(ti,tf,h)
n=len(t)
m1=1.94; m2=0.10; x11=1.2; x12=-1.3; x21=1.4; x22=1.5
K1=0.50;g=9.81

for j in range(0,n-1):
    # RK Estágio 1
  M1barra = -m2*(x21*np.sin(q2[j])+x22*np.cos(q2[j])) + m2*(x21*np.cos(q2[j])-x22*np.sin(q2[j]))
  M2barra = m2*(-x21*np.cos(q2[j])+x22*np.sin(q2[j])) - m2*(x21*np.sin(q2[j])+x22*np.cos(q2[j]))
  k11 = h*q3[j]
  k12 = h*q4[j]
  k13 = -h*K1/m1*q1[j]
  k14 = h*(-M2barra/M1barra)*q4[j]**2+m2*K1/(m1*M1barra)*q2[j]-2*m2*g/M1barra*np.cos(q2[j])
  # RK Estágio 2
  M1barraaux1 = -m2*(x21*np.sin(q2[j]+0.5*k12)+x22*np.cos((q2[j]+0.5*k12)))+m2*(x21*np.cos(q2[j]+0.5*k12)-x22*np.sin(q2[j]+0.5*k12))
  M2barraaux1 = m2*(-x21*np.cos(q2[j]+0.5*k12)+x22*np.sin(q2[j]+0.5*k12))-m2*(x21*np.sin((q2[j]+0.5*k12))+x22*np.cos((q2[j]+0.5*k12)))
  k21 = h*(q3[j]+0.5*k13)
  k22 = h*(q4[j]+0.5*k14)
  k23 = -h*K1/m1*(q1[j]+0.5*k11)
  k24 = h*(-M2barraaux1/M1barraaux1)*((q4[j]+0.5*k14)**2)+m2*K1/(m1*M1barraaux1)*(q2[j]+0.5*k12)-2*m2*g/M1barraaux1*np.cos(q2[j]+0.5*k12)

  # RK Estágio 3
  M1barraaux2 = -m2*(x21*np.sin(q2[j]+0.5*k22)+x22*np.cos((q2[j]+0.5*k22))) + m2*(x21*np.cos((q2[j]+0.5*k22))-x22*np.sin((q2[j]+0.5*k22)))
  M2barraaux2 = m2*(-x21*np.cos((q2[j]+0.5*k22))+x22*np.sin((q2[j]+0.5*k22))) - m2*(x21*np.sin((q2[j]+0.5*k22))+x22*np.cos((q2[j]+0.5*k22)))
  k31 = h*(q3[j]+0.5*k23)
  k32 = h*(q4[j]+0.5*k24)
  k33 = -h*K1/m1*(q1[j]+0.5*k21)
  k34 = h*(-M2barraaux2/M1barraaux2)*(q4[j]+0.5*k24)**2+m2*K1/(m1 *M1barraaux2)*(q2[j]+0.5*k22)-2*m2*g/M1barraaux2*np.cos(q2[j]+0.5*k22)

  # RK Estágio 4
  M1barraaux3 = -m2*(x21*np.sin((q2[j]+k32)+x22*np.cos((q2[j]+k32)))) + m2*(x21*np.cos((q2[j]+k32))-x22*np.sin((q2[j]+k32)))
  M2barraaux3 = m2*(-x21*np.cos((q2[j]+k32))+x22*np.sin((q2[j]+k32))) - m2*(x21*np.sin((q2[j]+k32))+x22*np.cos((q2[j]+k32)))
  k41 = h*(q3[j]+0.5*k33)
  k42 = h*(q4[j]+0.5*k34)
  k43 = -h*K1/m1*(q1[j]+0.5*k31)
  k44 = h*(-M2barraaux3/M1barraaux3)*(q4[j]+k34)**2+m2*K1 / (m1*M1barraaux3)*(q2[j]+k32)-2*m2*g/M1barraaux3*np.cos(q2[j]+k32)

  # Processo de atualização
  q1.append(q1[j]+1/6*(k11+2*k21+2*k31+k41))
  q2.append(q2[j]+1/6*(k12+2*k22+2*k32+k42))
  q3.append(q3[j]+1/6*(k13+2*k23+2*k33+k43))
  q4.append(q4[j]+1/6*(k14+2*k24+2*k34+k44))


plt.plot(t,q1,label='Posição Massa 1')
plt.plot(t,q2,label='Ângulo Massa 2')
plt.plot(t,q3,label='Velocidade Massa 1')
plt.plot(t,q4,label='Velocidade Massa 2')
plt.legend()
plt.show()