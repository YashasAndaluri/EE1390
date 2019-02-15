import numpy as np
import matplotlib.pyplot as plt


P=np.array([3,0])
Q=np.array([1,-2])

X=np.array([-5,2])
Y=np.array([2,-5])
Z=np.array([5,-2])
W=np.array([-2,5])

M=np.array([6,0])
N=np.array([-6,0])
U=np.array([0,6])
V=np.array([0,-6])

C=np.array([3,-2])
r=2.0
len=5000
x_PC=np.zeros((2,len))
x_MN=np.zeros((2,len))
x_UV=np.zeros((2,len))
D=np.linspace(0,1,len)
semi_c1=np.zeros((2,len))
semi_c2=np.zeros((2,len))
B=np.linspace(-1,1,len)

for i in range(len):
	line1=P+D[i]*(C-P)
	x_PC[:,i]=line1.T
	line2=M+D[i]*(N-M)
	x_MN[:,i]=line2.T
	line3=U+D[i]*(V-U)
	x_UV[:,i]=line3.T
	
	x=B[i]
	y1=np.sqrt(1-(B[i]*B[i]))
	y2=-y1
	z1=np.array([x,y1])
	z2=np.array([x,y2])
	A1=C+r*z1
	A2=C+r*z2
	semi_c1[:,i]=A1.T
	semi_c2[:,i]=A2.T
		
	
plt.plot(x_PC[0,:],x_PC[1,:],label='Radius')
plt.plot(x_MN[0,:],x_MN[1,:],'g')
plt.plot(x_UV[0,:],x_UV[1,:],'g')
plt.plot(semi_c1[0,:],semi_c1[1,:],'r',label='Circle')
plt.plot(semi_c2[0,:],semi_c2[1,:],'r')

plt.plot(Q[0],Q[1],'yo')
plt.text(Q[0]*(1+0.06),Q[1]*(1+0.06),'Q(1,-2)')
plt.plot(P[0],P[1],'yo')
plt.text(P[0]*(1+0.1),P[1]*(1-0.1),'P (3,0)')
plt.plot(C[0],C[1],'yo')
plt.text(C[0]*(1-0.1),C[1]*(1),'C (3,-2)')

plt.text(-3,-0.5,'X-axis')
plt.text(0.4,5,'Y-axis')

plt.plot(X[0],X[1],'bo')
plt.text(X[0]*(1+0.06),X[1]*(1+0.06),'(-5,2)')
plt.plot(Y[0],Y[1],'bo')
plt.text(Y[0]*(1+0.06),Y[1]*(1+0.06),'(2,-5)')
plt.plot(Z[0],Z[1],'bo')
plt.text(Z[0]*(1+0.06),Z[1]*(1+0.06),'(5,-2)')
plt.plot(W[0],W[1],'bo')
plt.text(W[0]*(1+0.06),W[1]*(1+0.06),'(-2,5)')
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(loc='best')
plt.grid()
plt.show()

