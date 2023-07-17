# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:13:01 2021

@author: Cathal McAleer
Description:
    This programme allows the user to import a .csv file from the \
    EM simulation software Sonnet, extracts and prints;\
    Parameter titles, Resonant Frequency and Quality Factor from the file.
"""

#............................................................................#
#Importing libraries
import csv
from scipy.interpolate import splev, splrep, sproot
import numpy as np
import matplotlib.pyplot as plt


#...........................................................................#
#Lists to append to
S11_Mag_loop=[] #All S11 Magnitudes in .csv file
S11_Phase_loop=[] #All S11 Phases in .csv file

S21_Mag_loop = [] #All S21 Magnitudes in .csv file 
S21_Phase_loop=[] #All S21 Phases in .csv file

all_Freq=[] #All frequencies in .csv file
Param=[] #List for reading all dimension parameters 

ac_res_freq = [] #Actual resonant frequencies list of each sweep
title=[] #Actual Parameter titles for each sweep
forloop=[0] #number of frequencies being scanned
Qual_Fac=[] #list to append Quality Factor values to for each parameter
#............................................................................#
#Only input into code
print("\nThis programme allows the user to import a .csv file from Sonnet\
 and exports the parameters swept, resonant frequencies and corresponding\
 quality factor from the file.")

#...........................................................................#

#File directory where file is imported
with open("C:\\Users\\scath\\Desktop\\VariationCapacitor.csv",\
          "r") as csvfile:
    
    csvReader=csv.reader(csvfile)
          
    for row in csvReader:
        
        try:
            Param.append(row[0]) #Read entire first row
            all_Freq.append(float(row[0])) #Read in first row of values
            
            S11_Mag_loop.append(float(row[1]))
            S11_Phase_loop.append(float(row[2]))
            
            S21_Mag_loop.append(float(row[5])) 
            S21_Phase_loop.append(float(row[6]))
            
            
        except ValueError: #for Freq and mag. If row isn't a float, continue
            continue
        
End_Freq = max(all_Freq)
#looping through each value of frequencies

for i in range(len(all_Freq)):
    
    a=all_Freq[i] 
    
    
    if a==End_Freq: #if a = end of frequency sweep. 
    #Get's # of frequencies swept by Sonnet
        
        forloop.append(i) #append to forloop list
        
    else:
        continue

#number of sweeps performed = elemenets in forloop list - 1 
num_of_sweeps=len(forloop)-1

#Main prog

for n in range(0,num_of_sweeps-1):
    
    
    b=all_Freq[forloop[n]+1:forloop[n+1]+1]
    
    S11_Mag = S11_Mag_loop[forloop[n]+1:forloop[n+1]+1]
    S11_Phase = S11_Phase_loop[forloop[n]+1:forloop[n+1]+1]
    
    S21_Mag = S21_Mag_loop[forloop[n]+1:forloop[n+1]+1]    
    S21_Phase = S21_Phase_loop[forloop[n]+1:forloop[n+1]+1]
    
    
   
    c=forloop[n]+9*n+8 #Skipping Comments in .csv file
    

    
    #plt.plot(S21_Mag,S21_Phase, label=label1)

    


    
    if c==8:
        start=Param[8]
        title.append(start)
        
    else:
        
        start=Param[forloop[n]+9*n+9]
        title.append(start)
    
    
            
    minimum_db = min(S21_Mag) #minimum S21 corresponding to res. frequency
    HM=(S21_Mag[0]+minimum_db)/2 #Half-width of dip   
    
    #Spline interpolate data to obtain roots at 
    tck=splrep(b, S21_Mag) # spline coeff returned as a tuple
    y_output = splev(b, tck)
    
    #Move data from y=HM to y=0 and solve roots for x
    tck2=splrep(b, y_output-HM)
    
    x=sproot(tck2)#Roots (I.e points at Half-Max)
    
    FWHM=x[1]-x[0] #Full width-Half-Maximum
    

    #Finding corresponding res. frequency in list
    for t in range(len(S21_Mag)):
        if S21_Mag[t]==minimum_db:
            #Append all resonant frequencies to empty list
            ac_res_freq.append(b[t]*1e3)
            
            #Append quality factor (res.freq/Fullwidth-halfmax)
            Qual_Fac.append(b[t]/FWHM)

        else:  #else, continue code
            continue

#.........................Printing Table of Results.........................#

#Print titles 
print("\n{:<8}{:>25}{:>20}".format("Parameter(\u03BCm)", "Res.Freq(GHz)"\
                                   ,"Quality Factor"))
for i in range(len(ac_res_freq)):
    
    print("\n{:<8}{:>20.4f}{:>20.2f}".format(title[i], ac_res_freq[i]\
                                       ,Qual_Fac[i]))
        



#...........................................................................#
