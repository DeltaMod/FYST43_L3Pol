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

data = {'IR_NQ':{},'IR_Q':{},'532_Q':{}}

for key in data.keys():
    L = 20
    data[key] = {'V_pump' : np.array([]),
                 'E_cap'  : np.array([]),
                 'pow_avg': np.array([]),
                 'E_Pulse': np.array([]),
                 'eff'    : np.array([]),
                 'P_peak' : np.array([]),
                 
                 't_FWHM' : np.array([]),
                 'C':30*10**-6,
                 'rate':10,
                 'duration': None,
                 'LT':None,
                 'f_prof':0.94}

M = {'Cu':   {'EV':4.73 * 10**6,'MD':8960}, #J/kg, and kg/m^3
     'Al':   {'EV':10.53* 10**6,'MD':2700},
     'Steel':{'EV':6.80 * 10**6,'MD':8050},
     'Fe':   {'EV':6.09 * 10**6,'MD':7874},
     'Brass':{'EV':4.73 * 10**6,'MD':8730}}



def Func_PulseEnergy(Pow,Rep):
    E_pulse = Pow/Rep
    return(E_pulse)

def Func_PeakPow(t_FWHM, f_prof, E_pul):
    P_p = f_prof*E_pul/t_FWHM
    
    return(P_p)

def Func_CapEnergy(Cap,Volt):
    E_cap = Cap*np.power(Volt,2)/2
    return(E_cap)
    
def Func_Efficiency(P_in,P_out):
    Eff = P_out/P_in
    return(Eff)

for key in data.keys():
    data[key]['E_Pulse'] = Func_PulseEnergy(data[key]['pow_avg'],data[key]['rate'])
    data[key]['P_peak']  = Func_PeakPow(data[key]['t_FWHM'], data[key]['f_prof'], data[key]['E_Pulse'])
    data[key]['E_cap']   = Func_CapEnergy(data[key]['C'],data[key]['V_pump'])
    data[key]['eff']     = Func_Efficiency(data[key]['P_peak'],data[key]['pow_avg']) #Check later
    


for key in data.keys():
    print(key+'\n==============')
    STRL = len(max(data['IR_NQ'].keys(),key=len))
    for subkey in data[key].keys():
        pad = [' ' for n in range(STRL-len(subkey))]
        
        print(subkey+"".join(pad)+str(data[key][subkey]))

    
