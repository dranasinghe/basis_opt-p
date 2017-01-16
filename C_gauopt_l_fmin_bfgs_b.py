import numpy as np
import scipy  
from scipy import optimize
#import subprocess
import os


initial_values=np.array([8.3735,-1.997,0.1879,-0.0123,2.2452,-1.754,0.2414,-0.0386])
#params=initial_values
def func(params, *args):
    # # numSJ numberof S function to be optimized
   numSJ =9
   SJ = np.arange(0,numSJ,1)
   print SJ
   
   SB0=params[0]
   SB1=params[1]
   SB2=params[2]
   SB3=params[3]
   
    # # numPJ numberof P function to be optimized
   numPJ =4
   PJ = np.arange(0,numPJ,1)
   print SJ
   
   PB0=params[4]
   PB1=params[5]
   PB2=params[6]
   PB3=params[7]
   
   print params
   f1=open('./C_0_3_temp', 'r')
   
   OUT =open('./C_0_3.psi', 'w+')
   for line in f1:   
      print >>OUT,  line.rstrip()
   
   print >>OUT,  "****"
   print >>OUT,  "C    0"
   
# S functions are printed to inputfile   
   for k in SJ:
       lnalphaSJ=SB0+SB1*SJ[k]+SB2*np.power(SJ[k], 2)+SB3*np.power(SJ[k], 3)
       alphaSJ= np.exp(lnalphaSJ)
       print >>OUT, "S  1  1.00"
       print >>OUT, "%20.9e       1.0000000" %alphaSJ
   
# S functions are printed to inputfile   
   for l in PJ:
       lnalphaPJ=PB0+PB1*PJ[l]+PB2*np.power(PJ[l], 2)+PB3*np.power(PJ[l], 3)
       alphaPJ= np.exp(lnalphaPJ)
       print >>OUT, "P  1  1.00"
       print >>OUT, "%20.9e       1.0000000" %alphaPJ
   
   print >>OUT, "****"
   print >>OUT, "}"
   print >>OUT, "set reference uhf"
   print >>OUT, "scf_energy, scf_wfn = energy('scf', return_wfn=True)"
   print >>OUT, "Temp =open('./tempC.out', 'w+')"
   print >>OUT, "print >>Temp,(scf_energy)"
   #print >>OUT, "print (scf_energy)"
   
   OUT.close()
   f1.close()
   
   os.system("psi4 C_0_3.psi")
   
   f2=open('./tempC.out', 'r')
   for word in f2:
      H_energy = word.rstrip()
   Energy=float(H_energy) 
   print Energy
   return Energy

scipy.optimize.minimize(func, x0=initial_values,method='L-BFGS-B',options={'disp':True, 'maxls': 20, 'gtol': 1e-05, 'eps': 1e-06, 'maxiter': 150, 'ftol':1e-010, 'maxcor': 10, 'maxfun':500})

