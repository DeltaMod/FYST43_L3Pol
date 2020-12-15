# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 23:12:07 2020
@author: Vidar Flodgren
Github: https://github.com/DeltaMod
"""
import numpy as np
from scipy.constants import c,e,h
import sympy
n = 1
d = 0.4
R_1 = np.inf
R_2 = -1

def z012(d,R_1,R_2):
    if R_1 == R_2:
        z_0 = d/2 * np.sqrt( 2 * abs(R_2)/d - 1)
    elif R_1 != R_2 and R_1 !=np.inf and R_2 !=np.inf:
        z_0 = np.sqrt( (-d*(R_1 + d)*(R_2 + d)*(R_1 +R_2+ d))/((R_2+R_1+2*d)**2) )
    elif R_1 == np.inf or R_2 == np.inf:
        if R_1 ==  np.inf:
            R = R_2

        else:

            R = R_1
        z_0 = np.sqrt(-d*(R+d))
    z_1 = (-d*(R_2+d))/(R_2+R_1 +2*d)
    z_2 = z_1 + d
    return({'z_0':z_0,'z_1':z_1,'z_2':z_2,'R_1':R_1,'R_2':R_2,'d':d})

def dfreq(c,n,d):
    return(c/(2*n*d))

def Dupsilon(z_0,z_1,z_2,Dq,Dlm,ups):
    at_terms = np.arctan(z_2/z_0)-np.arctan(z_1/z_0)
    return(ups*(Dq+(1/np.pi)*(Dlm)*(at_terms)))
           


z =z012(d,R_1,R_2)  

print('\nExercise 4\n ======================')

dvups = dfreq(c,n,d)

Dups  = Dupsilon(z['z_0'],z['z_1'],z['z_2'],0,2,dvups)

print('V_FSR = '+ str(Dups/10**6))


lambd = 633*10**-9
n1 = 1
n2 = 1.5
def ResPow(lambd,n1,n2,d):
    mmax = 2*d/lambd
    
    R1 = (n1-n2)**2/(n1+n2)**2
    R2 = (n2-n1)**2/(n2+n1)**2
    
    r = np.sqrt(R1*R2)
    
    FIN  = np.pi*np.sqrt(abs(r))/(1-abs(r))  
    Rs = np.pi/2 *mmax* np.sqrt(FIN)
    return(Rs)

def ResPow2(lamb,d,**kwargs):
    if 'n1' in kwargs.keys():
        if 'n0' not in kwargs.keys():
            kwargs['n0'] = 1    
        n1 =  kwargs['n1']
        n0 = kwargs['n0']
        R     =  (n0-n1)**2/(n0+n1)**2
        r     =  np.sqrt(R*R)
    if 'r' in kwargs.keys():
        r = kwargs['r']
        n0 = 1
        n1 = 1
        
    F     =  ( np.pi*np.sqrt(abs(r))) / (1- abs(r))
    P_res =  np.pi/2 * 2*d/lamb * np.sqrt(F)
    
    return({'nonF':P_res/F,'r':r,'F':F,'P_res':P_res})

ex5lam = 633e-9 
print('\nExercise 5 \n ======================')
P_res_a = ResPow2(ex5lam,10e-3,n1 = 1.5, n0 = 1)
print(P_res_a)
P_res_b = ResPow2(ex5lam,0.05,r=0.85)
print(P_res_b)
P = ResPow(ex5lam,n1,n2,10**-3)

print(P)

def LasingPow(I,Wp):
    return(I/Wp*10**-3)

def RCalc(d,g_1):
    return(1/(1/d - g_1/d))

def DiodeEff(Pe,Pp,h,c,lambd):
    return((Pe/e)/(Pp*lambd/(h*c)))


Deff = DiodeEff(530e-6,1.325e-3,h,c,632.9e-9)

T1_k  = 0.017
T1_uk = 0.012
T2_p  = 0.012 
L1 = 0.45
L2 = 0.57

def MGain(T1,T2,L):
    tot = 1
    tot = tot*T1
    tot = tot*T2
    loss = tot/(2*L)
    
    return(loss)

MedGain_k = MGain(T1_k,T2_p,L1)

MedGain_uk = MGain(T1_uk,T2_p,L2)
