# This is code for area under the curve

#plt.plot(xpoints, ypoints)


final_x = 10
x_in = 0
x_fin = 0

y_in = 0
y_fin = 0
area = 0

while x_fin<10:
    y_in = x_in**2
    y_fin = x_fin**2

    # SPlliting Area in 2 parts
    area_rect = (x_fin - x_in) * y_in
    area_tri = 1/2 * (x_fin - x_in) * (y_fin - y_in)
    
    # Calculating
    area  = area + (area_rect + area_tri)
    x_in = x_fin
    x_fin = x_fin  + 0.00001

print("Hello area under the G is : ",area)