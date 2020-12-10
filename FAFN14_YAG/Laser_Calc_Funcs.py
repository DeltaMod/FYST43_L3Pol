# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:15:14 2020
@authors: Vidar and Isa
"""
import numpy as np

C = 30*10**-6 #F  
V_pump = [5,23,4,23,25,26] #kV
rate = 10        #Hz
lasing_treshold = None #kv #J

def Func_E_Cap(C,V):
    E_cap  = C*np.power(V,2)/2
    return(E_cap)

E_Cap = Func_E_Cap(C,V_pump)

dur = {'IR_nQ':np.array([1]),
       'IR_Q':np.array([1]),
       '532_Q':np.array([1])} 

pow_av = {'IR_nQ':np.array([1]),
          'IR_Q':np.array([1]),
          '532_Q':np.array([1])} 

E_pulse  = {'IR_nQ':np.array([1]),
            'IR_Q':np.array([1]),
            '532_Q':np.array([1])} 

eff = {'IR_nQ':np.array([1]),
       'IR_Q':np.array([1]),
       '532_Q':np.array([1])} 

pow_peak = {'IR_nQ':np.array([1]),
            'IR_Q':np.array([1]),
            '532_Q':np.array([1])} 

t_FWHM = {'IR_nQ':np.array([1]),
            'IR_Q':np.array([1]),
            '532_Q':np.array([1])} 

LT = ['IR_nQ','IR_Q','532_Q'] 

f_prof = 0.94

def Func_PeakPow(t_FWHM, f_prof, E_p):
    
    P_p = f_prof*E_p/t_FWHM
    
    return(P_p)


for cond in LT:
    pow_peak[cond] = Func_PeakPow(t_FWHM[cond], f_prof, [0])

    
