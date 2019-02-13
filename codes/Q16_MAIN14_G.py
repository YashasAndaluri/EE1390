import numpy as np
import matplotlib.pyplot as plt

#Calculating midpoint
def mid_pt(Q,R):
	S=(Q+R)/2
	return S

#Defining points P,Q,R
P=np.array([2,2])
Q=np.array([6,-1])
R=np.array([7,3])
##Find midpoint of Q and R 
S=mid_pt(Q,R)
##Finding direction vector of PS
PS=np.vstack((P,S)).T
dvec=np.array([-1,1])
d=np.matmul(PS,dvec)
##Unit direction vector:
unit_d=d/(np.linalg.norm(d))
##Let A be the point (1,-1)
A=np.array([1,-1])
#Let AB be the line parallel to PS where B is a point on the line
B=A+2*unit_d

##Plotting lines
len=10
lam_1=np.linspace(0,1,len)
x_PQ=np.zeros((2,len))
x_QR=np.zeros((2,len))
x_RP=np.zeros((2,len))
x_PS=np.zeros((2,len))
x_AB=np.zeros((2,len))

for i in range(len):
	temp1=P+lam_1[i]*(Q-P)
	x_PQ[:,i]=temp1.T
	temp2=Q+lam_1[i]*(R-Q)
	x_QR[:,i]=temp2.T
	temp3=R+lam_1[i]*(P-R)
	x_RP[:,i]=temp3.T
	temp4=P+lam_1[i]*(S-P)
	x_PS[:,i]=temp4.T
	temp5=A+5*lam_1[i]*(B-A)	
	x_AB[:,i]=temp5.T


plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$') 
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RP$')
plt.plot(x_PS[0,:],x_PS[1,:],label='$PS$') 
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB= 2x + 9y + 7$') 

##Plotting points 
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1-0.15),P[1]*(1-0.1),'P')
plt.plot(Q[0],Q[1],'o')
plt.text(Q[0]*(1+0.03),Q[1]*(1+0.25),'Q')
plt.plot(R[0],R[1],'o')
plt.text(R[0]*(1+0.03),R[1]*(1-0.1),'R')
plt.plot(S[0],S[1],'o')
plt.text(S[0]*(1+0.03),S[1]*(1-0.1),'S')
plt.plot(A[0],A[1],'o')
plt.text(A[0]*(1+0.03),A[1]*(1-0.1),'A= 2x + 9y + 7')

#Set labels,axes,legend and show plot
plt.xlabel('$x$')
plt.ylabel('$y$')
axes = plt.gca()
axes.set_xlim([1,10])
plt.legend(loc='best')
plt.grid()
plt.show()

