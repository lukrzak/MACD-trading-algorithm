import csv
file = open("WIG20.csv", "r")
X_AXIS_COLUMN_NUMBER = 0
Y_AXIS_COLUMN_NUMBER = 1
x_axis = []
y_axis = []
macd_values = []
signal_values = []

values = csv.reader(file)
for i in values:
    x_axis.append(i[X_AXIS_COLUMN_NUMBER])
    y_axis.append(float(i[Y_AXIS_COLUMN_NUMBER].replace('.', '').replace(',', '.')))


def get_ema_value(n, day, data):
    alpha = 2 / (n-1)
    ema_value = 0
    ema_value_denominator = 0
    for i in range(n):
        if day - i < 0:
            break
        ema_value += ((1 - alpha) ** i) * data[day - i]
        ema_value_denominator += ((1 - alpha) ** i)
    return ema_value / ema_value_denominator


def calculate_macd_value():
    for i in range(len(y_axis)):
        ema12 = get_ema_value(12, i, y_axis)
        ema26 = get_ema_value(26, i, y_axis)
        macd = ema12 - ema26
        macd_values.append(macd)
        signal = get_ema_value(9, i, macd_values)
        signal_values.append(signal)


calculate_macd_value()
print(macd_values)
print(signal_values)
