import csv
import matplotlib.pyplot as plt

file = open("WIG20.csv", "r")
X_AXIS_COLUMN_NUMBER = 0
Y_AXIS_COLUMN_NUMBER = 1
x_axis = []
y_axis = []
macd_values = []
signal_values = []
sell_days_markers = []
sell_markers_values = []
buy_days_markers = []
buy_markers_values = []


def read_csv_file():
    values = csv.reader(file)
    for i in values:
        x_axis.append(i[X_AXIS_COLUMN_NUMBER])
        y_axis.append(float(i[Y_AXIS_COLUMN_NUMBER].replace('.', '').replace(',', '.')))
    # Dates in CSV file are presented in descending order
    x_axis.reverse()
    y_axis.reverse()


def get_ema_value(n, day, data):
    alpha = 2 / (n - 1)
    ema_value = 0
    ema_value_denominator = 0
    for i in range(n):
        if day - i < 0:
            break
        ema_value += ((1 - alpha) ** i) * data[day - i]
        ema_value_denominator += ((1 - alpha) ** i)
    return ema_value / ema_value_denominator


def calculate_macd_value():
    read_csv_file()
    for i in range(len(y_axis)):
        ema12 = get_ema_value(12, i, y_axis)
        ema26 = get_ema_value(26, i, y_axis)
        macd = ema12 - ema26
        macd_values.append(macd)
        signal = get_ema_value(9, i, macd_values)
        signal_values.append(signal)

    for i in range(1, len(macd_values) - 1):
        if macd_values[i - 1] > signal_values[i - 1] and macd_values[i] < signal_values[i]:
            sell_days_markers.append(i)
            sell_markers_values.append(macd_values[i])
        if macd_values[i - 1] < signal_values[i - 1] and macd_values[i] > signal_values[i]:
            buy_days_markers.append(i)
            buy_markers_values.append(macd_values[i])


def plot_macd():
    calculate_macd_value()
    plt.plot(x_axis, macd_values, color='blue', label='MACD')
    plt.plot(x_axis, signal_values, color='red', label='SIGNAL')
    plt.plot(sell_days_markers, sell_markers_values, 'X', label='SELL')
    plt.plot(buy_days_markers, buy_markers_values, 'X', label='BUY')
    plt.xlabel("Date")
    plt.legend(loc='upper left')
    plt.show()

    marker_buy_values = []
    marker_sell_values = []
    for i in range(len(buy_days_markers)):
        marker_buy_values.append(y_axis[buy_days_markers[i]])
        marker_sell_values.append(y_axis[sell_days_markers[i]])

    plt.plot(x_axis, y_axis, color='black')
    plt.plot(buy_days_markers, marker_buy_values, 'X', color='red', label='BUY')
    plt.plot(sell_days_markers, marker_sell_values, 'X', color='blue', label='SELL')
    plt.legend(loc='upper left')
    plt.xlabel("Date")
    plt.show()


def simulate(money):
    funds = money
    buy_days_markers.insert(0, 0)
    sell_days_markers.append(len(x_axis) - 1)
    for i in range(len(buy_days_markers)):
        shares_bought = funds // y_axis[buy_days_markers[i]]
        funds += shares_bought * (y_axis[sell_days_markers[i]] - y_axis[buy_days_markers[i]])
    print(funds)


plot_macd()
simulate(5000)
