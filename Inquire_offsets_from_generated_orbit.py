from __future__ import print_function, division
import numpy as np
from numpy import linalg as la
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import scipy.optimize as optimize
from PyAstronomy import pyasl

def generate_ellipse(num_pts, semi_major, eccentricity, inclination, periapsis, longitude, t_closest):
    m = 4.3 #*10**6 solar mass
    n = np.sqrt(m*4.300952282/3.08567758**2/semi_major**3)*3.155692661 # mean motion: M=nt=sqrt(G(M+m)/a**3)t
    mu = m*4.300952282#mpc*(km/s)**2
    t = t_start - t_closest
    error = 10**(-5)
    flat_ellipse = np.zeros((num_pts, 4))
    flat_velocity = np.zeros((num_pts, 4))
#------------------------------
    def eccentric_anomaly(eccentricity, m_anomaly, error):
        ks = pyasl.MarkleyKESolver()
        E = ks.getE(m_anomaly, eccentricity)
        return E
#------------------------------
    def position(semi_major, eccentricity, e_anomaly, t):
        z = 0.
        nu = 2*np.arctan2(np.sqrt(1+eccentricity)*np.sin(e_anomaly/2), np.sqrt(1-eccentricity)*np.cos(e_anomaly/2))
        y = semi_major*(1-eccentricity*np.cos(e_anomaly))*np.cos(nu)
        x = semi_major*(1-eccentricity*np.cos(e_anomaly))*np.sin(nu)
        r = np.column_stack((x, y, z, t))#mas
        return r
#----------------------------------
    def velocity(mu, e_anomaly, semi_major, eccentricity, t):#(m/s)
        vy = -np.sin(e_anomaly)*np.sqrt(mu*semi_major)/semi_major/(1-eccentricity*np.cos(e_anomaly))
        vx = np.sqrt((1 - eccentricity**2)*mu*semi_major)*np.cos(e_anomaly)/semi_major/(1-eccentricity*np.cos(e_anomaly))
        vz = 0.
        v = np.column_stack((vx, vy, vz, t))
        return v
#-----------------------------
    # Create an ellipse in the xy plane
    for i in range(num_pts):
        m_anomaly = n*t
        e_anomaly = eccentric_anomaly(eccentricity, m_anomaly, error)
        flat_ellipse[i] = position(semi_major, eccentricity, e_anomaly, t+t_closest)
        flat_velocity[i] = velocity(mu, e_anomaly, semi_major, eccentricity, t+t_closest)
        t += dt
#----------------------------
    # Create a rotation matrix using Eulers angles
    rotation_matrix = np.array([[np.cos(-longitude)*np.cos(-inclination)*np.cos(-periapsis) - np.sin(-longitude)*np.sin(-periapsis), -np.cos(-periapsis)*np.sin(-longitude) - np.cos(-longitude)*np.cos(-inclination)*np.sin(-periapsis), np.cos(-longitude)*np.sin(-inclination)], [np.cos(-longitude)*np.sin(-periapsis) + np.cos(-inclination)*np.cos(-periapsis)*np.sin(-longitude), np.cos(-longitude)*np.cos(-periapsis) - np.cos(-inclination)*np.sin(-longitude)*np.sin(-periapsis), np.sin(-longitude)*np.sin(-inclination)], [-np.cos(-periapsis)*np.sin(-inclination), np.sin(-inclination)*np.sin(-periapsis), np.cos(-inclination)]])#ZYZ
#-----------------------------
    # Rotate the ellipse
    rotated_ellipse = np.zeros((num_pts, 7))
    for i in range(num_pts):
        rotated_r = np.dot(rotation_matrix, flat_ellipse[i, 0:3])
        rotated_v = np.dot(rotation_matrix, flat_velocity[i, 0:3])
        rotated_ellipse[i] = np.column_stack((rotated_r[0], rotated_r[1], rotated_r[2], rotated_v[0], rotated_v[1], rotated_v[2], flat_ellipse[i, 3]))
    return rotated_ellipse
#------------------------------------------------------------------------------------------------------

dec_dates = []
row_str = []

def inquiry_positions():

    num_pts = int((t_end-t_start)/dt)
    
#ellipse and orbit is generated and stored in an array, the 7th column stores each timestep
    dummy_ellipse = generate_ellipse(num_pts, semi_major, eccentricity, inclination, periapsis, longitude, t_closest)

# print (type(dummy_ellipse)) = <class 'numpy.ndarray'>

#=============================================================
#now the code to search investigated dates and print respective offsets

#import a text file containing all the dates needed
    dates_file = open("Converted_dates.txt", 'r')

    for each_line in dates_file.readlines():
        
    #rounding the decimal dates to 3 decimal places just in case it wasn't already
        dates_rounded = round(float(each_line), 3)
        dec_dates.append(dates_rounded)
    
    print("Imported dates: ")
    print(dec_dates)
    
    #=============================================================
    
#Preparing an output file

    output_file = open("inquired offsets.txt", 'w+')
    
    #Printing useful information as headers
    orbit_parameter = semi_major, eccentricity, inclination, periapsis, longitude, t_closest
    generated_length = t_start, t_end , dt
    
    #orbit_parameter & generated_length are "tuples", convert to string for ".write" function
    orbit_parameter_str = str(orbit_parameter).replace("(","").replace(")","")
    generated_length_str = str(generated_length).replace("(","").replace(")","")
    
    print ("Orbital parameter given: " + orbit_parameter_str)
    print ("Starting, Ending Year & Timestep: " + generated_length_str)
        
    output_header = "Orbital Parameters Given:\n" + "semi_major, eccentricity, inclination, periapsis, longitude, t_closest:\n" + orbit_parameter_str + "\n\nstarting year, ending year, timestep:\n" + generated_length_str + "\n\n"
    output_file.write(output_header)
    
    #using string formatting to print the parameters in another format
    #orbit_parameter_alt = ("semi major axis: %10.5f, eccentricity: %10.5f, inclination: %10.5f, periapsis: %10.5f, longitude: %10.5f, time of closest approach: %10.5f"%(semi_major, eccentricity, inclination, periapsis, longitude, t_closest))
    #output_file.write(orbit_parameter_alt)
    
    output_body = "Here are the Dates & offsets from Sag A* inquried for this orbit:\nDates\tRA (marcsec)\tDEC (marcsec)\n"
    output_file.write(output_body)
    
    #=============================================================
    
#for each specified dates at 7th column, print the entire row for positions 
#array indice - array[row, column]; and the first one is [0]

    for each_date in dec_dates:
        if t_start <= each_date <= t_end:
            row_index = (each_date-t_start)/dt
            
            # floating number operation is fucked up, row_index ends up with decimals even when it should be an integer
            # rounding is required, otherwise int() simply rounds down everything.
            row_index = int(round(row_index,0))
            
    #originally written to print the entire row:
            #row = dummy_ellipse[row_index,:]    #"row" type: numpy.ndarray
           
    #we found that dummy_ellipse[0][1] are RA, DEC in marcsec respectively, after divided by a factor of 40
    #we only need dummy_ellipse[0][1][6] column: RA, Dec offsets, Time
    
            date_out = round(dummy_ellipse[row_index,6],5)
            RA = float(dummy_ellipse[row_index,0])/40*1000 #marcsec
            Dec = float(dummy_ellipse[row_index,1])/40*1000 #marcsec
            
            #row_str.append(str(row_index))
            row_str.append(str(date_out))
            row_str.append(str(RA))
            row_str.append(str(Dec))         
                        
    #need to change back to strings for .write
            #for value in row:
            #    row_str.append(str(value))
                
            print(row_str)
            
            output_file.write('\t'.join(row_str))
            output_file.write("\n")
            row_str.clear()            
            
        else:
            print("Out of bounds!")
            output_file.write("Out of bounds!")
            output_file.write("\n")
        
    
    #print(np.where(a==2000.001)[0][0])
    #print(type(np.where(a==2000)))
    #b = (np.where(a==2000.001)[0][0])
    #print(dummy_ellipse[b,:])      
              
    
      #=============================================================   
        
    #output_file.write('\n'.join(list3))
    
    dates_file.close()   
    output_file.close()


#=============================================================   

#give the orbital parameters & time settings
t_start = 2000.
t_end = 2020.
dt = 0.001
semi_major, eccentricity, inclination, periapsis, longitude, t_closest = 5.033736 , 0.888946 , 2.400681 , 1.286074 , 4.15521 , 2002.310491


inquiry_positions()
