import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.optimize as optimize

def line(r1, r2, v1, v2):

    model = open('model.txt', 'w')
    t = 2002.578
    tf = 2018.310
    dt = 0.001
    n = (tf-t)/dt
    r = [r1, r2]
    v = [v1, v2]
    r_t = [t, r[0], r[1]]
    np.savetxt(model, np.column_stack(r_t))
    for i in range(int(n)+1):
        t += dt
        dr = [dummy*dt for dummy in v]
        r = np.add(r, dr)
        r_t = [t, r[0], r[1]]
        np.savetxt(model, np.column_stack(r_t))
    model.close()
#------------------------------------------------------
def plot(data, model):
    t, x, y, ex, ey = np.loadtxt('s7.txt', unpack = True)
    s7 = np.column_stack((t, x, y, ex, ey))
    
    fig, ax = plt.subplots()

    plt.errorbar(data[:, 1], data[:, 2], xerr = data[:, 3], yerr = data[:, 4],  color = 'blue', fmt = '.', ls = 'none', markersize = 10, mec = 'darkblue', capsize = 1, alpha = 0.5, label = 'data')
    for i, txt in enumerate(t):
        ax.annotate(txt, (x[i],y[i]), fontsize=7)    
    plt.plot(model[:, 1], model[:, 2], color = 'k', label = 'model')
    ax.grid(True)
    plt.axis('equal')
    ax.invert_xaxis()   
    ax.set_xlabel('R.A. (mas)')
    ax.set_ylabel('Dec (mas)')
#    ax.set_xlim(600., -800)
    ax.legend(loc = 'lower left', prop={'size': 8})
#-----------------------------------------------------
def transformation(model, data):

    transformation = open('s7_transformation.txt', 'w')

    for j in range(len(data[:, 0])):
        for i in range(len(model[:, 0])):
            if abs(model[i, 0] - data[j, 0]) < 0.0001:
                dx = model[i, 1] - data[j, 1]
                dy = model[i, 2] - data[j, 2]
                delta = [data[j, 0], dx, dy]
                np.savetxt(transformation, np.column_stack(delta))
                break

    transformation.close()
#------------------------------------------------------
def bootstrap(data, initial_guess, bnds, ndata):

    def deviation(variables, sample_x, sample_y, data):
        """
        This function calculates the cumulative seperation between the data points and model points and returns it
        """
        r1, r2, v1, v2 = variables
        line(r1, r2, v1, v2)
        t, x, y = np.loadtxt('model.txt', unpack=True)
        model = np.column_stack((t, x, y))
        pair_deviations = np.zeros(len(data[:, 0]))
        # Calculate separation between each pair of points
        for j in range(len(data[:, 0])):
            for i in range(len(model[:, 0])):
                if abs(model[i, 0] - data[j, 0]) < 0.0001:
                    pair_deviations[j] = (sample_x[j]-model[i, 1])**2 + (sample_y[j]-model[i, 2])**2
                    break 
        total_deviation = sum(pair_deviations)/(2*len(data[:, 0]) - 4) #normalized chi_squared
      
        return total_deviation

    r1_sample = []
    r2_sample = []
    v1_sample = []
    v2_sample = []
    for i in range(ndata):#bootstrapping
        idx = np.random.randint(0, len(data[:, 0]), size = len(data[:, 0]))
        sample_x = data[:, 1][idx]
        sample_y = data[:, 2][idx]

        result = optimize.minimize(deviation, initial_guess, args=(sample_x, sample_y, data ), method='SLSQP', bounds=bnds, tol=1e-4) 
        r1, r2, v1, v2 = result["x"]

        r1_sample.append(r1)
        r2_sample.append(r2)
        v1_sample.append(v1)
        v2_sample.append(v2)
        print(i)

    r1_sample = np.array(r1_sample)
    r2_sample = np.array(r2_sample)
    v1_sample = np.array(v1_sample)
    v2_sample = np.array(v2_sample)

    nsigma = 1 # 1sigma
    err_r1 = nsigma * np.std(r1_sample)
    err_r2 = nsigma * np.std(r2_sample)
    err_v1 = nsigma * np.std(v1_sample)
    err_v2 = nsigma * np.std(v2_sample)

    return err_r1, err_r2, err_v1, err_v2
#-------------------------------------------------------
def fitting():

    t, x, y, ex, ey = np.loadtxt('s7.txt', unpack = True)
    data = np.column_stack((t, x, y, ex, ey))#in marcsec
    tt = data[:, 0]
    xx = data[:, 1]
    yy = data[:, 2]
    exx= data[:, 3]
    eyy= data[:, 4]

    def deviation(variables, tt, xx, yy, exx, eyy):
        """
        This function calculates the cumulative seperation between the data points and model points and returns it
        """
        r1, r2, v1, v2 = variables
        line(r1, r2, v1, v2)
        t, x, y = np.loadtxt('model.txt', unpack=True)
        model = np.column_stack((t, x, y))

        pair_deviations = np.zeros(len(data[:, 0]))
        # Calculate separation between each pair of points
        for j in range(len(data[:, 0])):
            for i in range(len(model[:, 0])):
                if abs(model[i, 0] - data[j, 0]) < 0.0001:
                    pair_deviations[j] = (data[j, 1]-model[i, 1])**2/data[j, 3]**2 + (data[j, 2]-model[i, 2])**2/data[j, 4]**2
                    break 
        print(len(pair_deviations))
        total_deviation = sum(pair_deviations)/(2*len(data[:, 0]) - 4) #minimized chi_squared
      
        return total_deviation


    initial_guess = [529.35, -42.32, 5, 4]#alpha #position in marcsec & velocities marcsec/year
    bnds = ((400., 700.), (-100., 0.), (-10., 10.), (-10., 10.))#alpha
    result = optimize.minimize(deviation, initial_guess, args=(tt, xx, yy, exx, eyy ), method='SLSQP', bounds=bnds, tol=1e-4) 

    r1, r2, v1, v2 = result["x"]
    
    print('Minimized variables result, r1, v1, r2, v2:', r1, v1, r2, v2, 'in mas')

  #  err_r1, err_r2, err_v1, err_v2 = bootstrap(data, initial_guess, bnds, 50)
 #   print 'error on variables, r1, v1, r2, v2:', err_r1, err_v1, err_r2, err_v2

    line(r1, r2, v1, v2)
    t, x, y = np.loadtxt('model.txt', unpack = True)
    model = np.column_stack((t, x, y))#in marcsec
    plot(data, model)
    transformation(model, data)
#-------------------------------------------------------
fitting()
plt.show()