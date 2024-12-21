import numpy as np

# objects found to be calibrated
# xxx_new.txt is the result after transformation

# copy paste the new objects again

t, x, y, ex, ey = np.loadtxt('sgra.txt', unpack = True)
sgra = np.column_stack((t, x, y, ex, ey ))#in marcsec
sgra_new = open('sgra_new.txt', 'w')

t, x, y, ex, ey = np.loadtxt('s2.txt', unpack = True)
s2 = np.column_stack((t, x, y, ex, ey ))#in marcsec
s2_new = open('s2_new.txt', 'w')

t, x, y, ex, ey = np.loadtxt('s102(copy)_new15.txt', unpack = True)
s102 = np.column_stack((t, x, y, ex, ey ))#in marcsec
s102_new = open('s102_new_new15.txt', 'w')

t, x, y, ex, ey = np.loadtxt('s17.txt', unpack = True)
s17 = np.column_stack((t, x, y, ex, ey ))#in marcsec
s17_new = open('s17_new.txt', 'w')

t, x, y, ex, ey = np.loadtxt('s38.txt', unpack = True)
s38 = np.column_stack((t, x, y, ex, ey ))#in marcsec
s38_new = open('s38_new.txt', 'w')

#=========================================================

# reference linear motion stars

t, x, y, ex, ey = np.loadtxt('s7.txt', unpack = True)
s7 = np.column_stack((t, x, y, ex, ey ))#in marcsec
t, dx, dy = np.loadtxt('s7_transformation.txt', unpack = True)
s7_trans = np.column_stack((t, dx, dy))#in marcsec
s7_new = open('s7_new.txt', 'w')

t, x, y, ex, ey = np.loadtxt('s10.txt', unpack = True)
s10 = np.column_stack((t, x, y, ex, ey))#in marcsec
t, dx, dy = np.loadtxt('s10_transformation.txt', unpack = True)
s10_trans = np.column_stack((t, dx, dy))#in marcsec
s10_new = open('s10_new.txt', 'w')

t, x, y, ex, ey = np.loadtxt('s30.txt', unpack = True)
s30 = np.column_stack((t, x, y, ex, ey))#in marcsec
t, dx, dy = np.loadtxt('s30_transformation.txt', unpack = True)
s30_trans = np.column_stack((t, dx, dy))#in marcsec
s30_new = open('s30_new.txt', 'w')

t, x, y, ex, ey = np.loadtxt('s26.txt', unpack = True)
s26 = np.column_stack((t, x, y, ex, ey ))#in marcsec
t, dx, dy = np.loadtxt('s26_transformation.txt', unpack = True)
s26_trans = np.column_stack((t, dx, dy))#in marcsec
s26_new = open('s26_new.txt', 'w')

t, x, y, ex, ey = np.loadtxt('s65.txt', unpack = True)
s65 = np.column_stack((t, x, y, ex, ey ))#in marcsec
t, dx, dy = np.loadtxt('s65_transformation.txt', unpack = True)
s65_trans = np.column_stack((t, dx, dy))#in marcsec
s65_new = open('s65_new.txt', 'w')

#=========================================================

ave = open('average_transformation.txt', 'w')
ave_trans = np.zeros((len(s7_trans[:, 0]), 5), 'd')
for i in range(len(s7_trans[:, 0])):
    dx = [s7_trans[i, 1] , s10_trans[i, 1] , s26_trans[i, 1] , s30_trans[i, 1] , s65_trans[i, 1]]
    dy = [s7_trans[i, 2] , s10_trans[i, 2] , s26_trans[i, 2] , s30_trans[i, 2] , s65_trans[i, 2]]
    ave_trans[i] = [s7_trans[i, 0], np.mean(dx), np.std(dx)/np.sqrt(5), np.mean(dy), np.std(dy)/np.sqrt(5)]
    np.savetxt(ave, np.column_stack(ave_trans[i]))
print 'average transformation:', ave_trans

#ave_err_r1 = 2.6784
#ave_err_v1 = 0.227
#ave_err_r2 = 2.2614
#ave_err_v2 = 0.3006

#print 'average errors:', ave_err_r1, ave_err_v1, ave_err_r2, ave_err_v2

#=========================================================

# copy paste the new objects again

for i in range(len(sgra[:, 0])):
    sgra_x = sgra[i, 1] + ave_trans[i, 1]
    sgra_y = sgra[i, 2] + ave_trans[i, 3]
    sgra_x_err = np.sqrt(sgra[i, 3]**2 + ave_trans[i, 2]**2)
    sgra_y_err = np.sqrt(sgra[i, 4]**2 + ave_trans[i, 4]**2)
    sgra_xy = [sgra[i, 0], sgra_x, sgra_y, sgra_x_err, sgra_y_err]
    np.savetxt(sgra_new, np.column_stack(sgra_xy))

for i in range(len(s2[:, 0])):
    s2_x = s2[i, 1] + ave_trans[i, 1]
    s2_y = s2[i, 2] + ave_trans[i, 3]
    s2_x_err = np.sqrt(s2[i, 3]**2 + ave_trans[i, 2]**2)
    s2_y_err = np.sqrt(s2[i, 4]**2 + ave_trans[i, 4]**2)
    s2_xy = [s2[i, 0], s2_x, s2_y, s2_x_err, s2_y_err]
    np.savetxt(s2_new, np.column_stack(s2_xy))

for i in range(len(s102[:, 0])):
    s102_x = s102[i, 1] + ave_trans[i, 1]
    s102_y = s102[i, 2] + ave_trans[i, 3]
    s102_x_err = np.sqrt(s102[i, 3]**2 + ave_trans[i, 2]**2)
    s102_y_err = np.sqrt(s102[i, 4]**2 + ave_trans[i, 4]**2)
    s102_xy = [s102[i, 0], s102_x, s102_y, s102_x_err, s102_y_err]
    np.savetxt(s102_new, np.column_stack(s102_xy))

for i in range(len(s7[:, 0])):
    s7_x = s7[i, 1] + ave_trans[i, 1]
    s7_y = s7[i, 2] + ave_trans[i, 3]
    s7_x_err = np.sqrt(s7[i, 3]**2 + ave_trans[i, 2]**2)
    s7_y_err = np.sqrt(s7[i, 4]**2 + ave_trans[i, 4]**2)
    s7_xy = [s7[i, 0], s7_x, s7_y, s7_x_err, s7_y_err]
    np.savetxt(s7_new, np.column_stack(s7_xy))

for i in range(len(s10[:, 0])):
    s10_x = s10[i, 1] + ave_trans[i, 1]
    s10_y = s10[i, 2] + ave_trans[i, 3]
    s10_x_err = np.sqrt(s10[i, 3]**2 + ave_trans[i, 2]**2)
    s10_y_err = np.sqrt(s10[i, 4]**2 + ave_trans[i, 4]**2)
    s10_xy = [s10[i, 0], s10_x, s10_y, s10_x_err, s10_y_err]
    np.savetxt(s10_new, np.column_stack(s10_xy))

for i in range(len(s17[:, 0])):
    s17_x = s17[i, 1] + ave_trans[i, 1]
    s17_y = s17[i, 2] + ave_trans[i, 3]
    s17_x_err = np.sqrt(s17[i, 3]**2 + ave_trans[i, 2]**2)
    s17_y_err = np.sqrt(s17[i, 4]**2 + ave_trans[i, 4]**2)
    s17_xy = [s17[i, 0], s17_x, s17_y, s17_x_err, s17_y_err]
    np.savetxt(s17_new, np.column_stack(s17_xy))

for i in range(len(s30[:, 0])):
    s30_x = s30[i, 1] + ave_trans[i, 1]
    s30_y = s30[i, 2] + ave_trans[i, 3]
    s30_x_err = np.sqrt(s30[i, 3]**2 + ave_trans[i, 2]**2)
    s30_y_err = np.sqrt(s30[i, 4]**2 + ave_trans[i, 4]**2)
    s30_xy = [s30[i, 0], s30_x, s30_y, s30_x_err, s30_y_err]
    np.savetxt(s30_new, np.column_stack(s30_xy))

for i in range(len(s38[:, 0])):
    s38_x = s38[i, 1] + ave_trans[i, 1]
    s38_y = s38[i, 2] + ave_trans[i, 3]
    s38_x_err = np.sqrt(s38[i, 3]**2 + ave_trans[i, 2]**2)
    s38_y_err = np.sqrt(s38[i, 4]**2 + ave_trans[i, 4]**2)
    s38_xy = [s38[i, 0], s38_x, s38_y, s38_x_err, s38_y_err]
    np.savetxt(s38_new, np.column_stack(s38_xy))

for i in range(len(s26[:, 0])):
    s26_x = s26[i, 1] + ave_trans[i, 1]
    s26_y = s26[i, 2] + ave_trans[i, 3]
    s26_x_err = np.sqrt(s26[i, 3]**2 + ave_trans[i, 2]**2)
    s26_y_err = np.sqrt(s26[i, 4]**2 + ave_trans[i, 4]**2)
    s26_xy = [s26[i, 0], s26_x, s26_y, s26_x_err, s26_y_err]
    np.savetxt(s26_new, np.column_stack(s26_xy))

for i in range(len(s65[:, 0])):
    s65_x = s65[i, 1] + ave_trans[i, 1]
    s65_y = s65[i, 2] + ave_trans[i, 3]
    s65_x_err = np.sqrt(s65[i, 3]**2 + ave_trans[i, 2]**2)
    s65_y_err = np.sqrt(s65[i, 4]**2 + ave_trans[i, 4]**2)
    s65_xy = [s65[i, 0], s65_x, s65_y, s65_x_err, s65_y_err]
    np.savetxt(s65_new, np.column_stack(s65_xy))

sgra_new.close()
s2_new.close()
s102_new.close()
s7_new.close()
s10_new.close()
s17_new.close()
s30_new.close()
s38_new.close()
s26_new.close()
s65_new.close()
ave.close()
