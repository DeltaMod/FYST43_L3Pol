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
    L = 0.52 #m
    Vfsr = 239*10**6 #Hz for no q=switching
    
    
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

data['IR_NQ']['LT'] =  np.array([0.91*10**3])
data['IR_NQ']['V_pump'] = np.array([0.91,0.95,1.0,1.05,1.1,1.15, 1.2, 1.25, 1.3, 1.35, 1.4,1.45, 1.5  ]) *10**3 #V
data['IR_NQ']['pow_avg'] = np.array([8.1,73.4,181.5,340,480,680,885, 1130, 1380, 1630, 1880, 2175,2430 ])*10**-3 #W
data['IR_NQ']['t_FWHM'] = np.array([194.05*10])*10**-9

data['IR_Q']['LT'] =  np.array([0.94*10**3])
data['IR_Q']['V_pump']  = np.array([0.94,0.95,1.0,1.05,1.1,1.15, 1.2, 1.25, 1.3, 1.35, 1.4,1.45,1.5  ])   * 10**3 #V
data['IR_Q']['pow_avg'] = np.array([7.5, 95.6,298,522,728, 965, 1195,1478, 1701,1975,2204,2470, 2700   ]) * 10**-3
data['IR_Q']['t_FWHM'] = np.array([27.9])*10**-9
data['IR_Q']['duration'] = np.array([ ])*10**-9

data['532_Q']['LT'] =  np.array([0.91*10**3])
data['532_Q']['V_pump']  = np.array([1.2,1.5  ])*10**3
data['532_Q']['pow_avg'] = np.array([260 , 680 ])*10**-3
data['532_Q']['t_FWHM'] = np.array([ 17.25  b])*10**-9

#note: we get approx a 25% ratio between this q switching and the original, so the original should be reduced by about 25%
#if we measure the zero rystal, we got 2000 ish, which is aout 0.75% from 2700 MW 

#dye laser: from 1.2 kV, we get 9 mW, calculate efficiency
#The cell is rotated at the rewster angle, and as suvj, it selects only one polarisation to leave the cell.
def Func_PulseEnergy(Pow,Rep):
    E_pulse = Pow/Rep
    return(E_pulse)

def Func_PeakPow(t_FWHM, f_prof, E_pul):
    P_p = f_prof*E_pul/t_FWHM
    
    return(P_p)

def Func_CapEnergy(Cap,Volt):
    E_cap = Cap*np.power(Volt,2)/2
    print(Cap)
    print(Volt)
    return(E_cap)
    
def Func_Efficiency(E_in,E_out):
    Eff = E_out/E_in
    return(Eff)

def Func_EToBurn(H,r_spot,d,rho):
    return(H*np.pi*r_spot**2*d*rho)


    
for key in data.keys():
    data[key]['E_Pulse'] = Func_PulseEnergy(data[key]['pow_avg'],data[key]['rate'])
    #data[key]['P_peak']  = Func_PeakPow(data[key]['t_FWHM'], data[key]['f_prof'], data[key]['E_Pulse'])
    data[key]['E_cap']   = Func_CapEnergy(data[key]['C'],data[key]['V_pump'])
    data[key]['eff']     = Func_Efficiency(data[key]['E_cap'],data[key]['E_Pulse']) #Check later
    


for key in data.keys():
    print(key+'\n==============')
    STRL = len(max(data['IR_NQ'].keys(),key=len))
    for subkey in data[key].keys():
        pad = [' ' for n in range(STRL-len(subkey))]
        
        print(subkey+"".join(pad)+str(data[key][subkey]))

E_burn = Func_EToBurn(M['Steel']['EV'],15.9*10**-6,0.001,M['Steel']['MD'])    

