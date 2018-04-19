omega = 7.3*10**-5
alfa = float(z1)
v = float(z2)
def tor(x):
	global  omega
	global alfa
	global v
	return 1.0*(x**2)*omega*(math.sin((-2*math.pi/360)*alfa))/v
print tor(100)


print 'NEW PLOT f=', v, 'm=', alfa

# Narysujmy na wykresie, jak przyspieszenie zmienia się w czasie.
x_list = [i for i in range(1,100)]
y_list = [tor (x) for x in x_list]

# Rysujemy wykres
ax2=fig.add_subplot(111)
ax2.xaxis.set_label_coords(0.9,0.1)
ax2.yaxis.set_label_coords(0.,1.02)
plt.xlabel(r"$x\,[m]$", fontsize=12)
plt.ylabel(r"$ y\,[m]$", fontsize=12, rotation=0) 
plt.ylim(-0.04,0.04)

# Umieszczamy dane na wykresie
plt.plot(x_list, y_list, 'r-o', markersize=1.0)
# Plot
plt.savefig('plt.png', dpi=400)


del x_list[-1]
del y_list[-1]