import csv
file = open("WIG20.csv", "r")
X_AXIS_COLUMN_NUMBER = 0
Y_AXIS_COLUMN_NUMBER = 1
x_axis = []
y_axis = []

data = csv.reader(file)
for d in data:
    x_axis.append(d[X_AXIS_COLUMN_NUMBER])
    y_axis.append(float(d[Y_AXIS_COLUMN_NUMBER].replace('.', '').replace(',', '.')))

print(x_axis)
print(y_axis)