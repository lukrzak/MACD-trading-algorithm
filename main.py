import csv
file = open("WIG20.csv", "r")
X_AXIS_COLUMN_NUMBER = 0
Y_AXIS_COLUMN_NUMBER = 1
x_axis = []
y_axis = []
macd_values = []

data = csv.reader(file)
for d in data:
    x_axis.append(d[X_AXIS_COLUMN_NUMBER])
    y_axis.append(float(d[Y_AXIS_COLUMN_NUMBER].replace('.', '').replace(',', '.')))


def get_ema_value(n, day):
    alpha = 2 / (n-1)
    ema_value = 0
    ema_value_denom = 0
    for i in range(n):
        if day - i < 0:
            break
        ema_value += ((1 - alpha) ** i) * y_axis[day - i]
        ema_value_denom += ((1 - alpha) ** i)
    return ema_value / ema_value_denom


def calculate_macd_value():
    for i in range(len(y_axis)):
        ema12 = get_ema_value(12, i)
        ema26 = get_ema_value(26, i)
        macd = ema12 - ema26
        macd_values.append(macd)


calculate_macd_value()
print(macd_values)