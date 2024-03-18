import datetime
from MathTools.log_files import check_log_folder
import matplotlib.pyplot as plt
from MathTools.Functions.line_2d import line_2d_example


def plot_sets_of_functions_2d(W: dict, key_save: bool, key_show: bool, path: str, height_of_picture: float):
    """
    The plot_sets_of_functions_2d function plots one or more sets of 2D functions on separate figures.
    Each set can contain multiple functions, and each function can be represented as a line, dots, or a dashed line.
    The function does not have a direct return value. Instead, it either displays the plot(s) on the screen
    (if key_show is True) or saves the plot(s) as image file(s) (if key_save is True). The image file(s) are saved
    in the specified directory (path) or in the Data/Chapter YYYY.MM.DD/ directory if path is set to 'Default'.

    :param W: A dictionary containing the sets of functions to be plotted. The structure of W is as follows:

        W = {'W1': {'S': S1, 'ttl': ttl1, 'axisX': axisX1, 'axisY': axisY1}, 'W2': { ... }, ... } - dict of sets

        Si = {'F1': {'F': F1, 'X': X1, 'T': T1, 'Label': Label1, 'Color': Color1, 'Line width': LW1},
        'F2': { ... }, ... } - dict of functions for set i

        Fi = [Fi1, Fi2, ..., FiJi] and Xi = [Xi1, Xi2, ..., XiJi] are lists representing the y-coordinates and
        x-coordinates of the function, respectively.

        Ti = 'Line' OR 'Dots' OR 'Dash' - specifies the line style for each function

        ttli = '...' - title for set i

        axisXi = '...', axisYi = '...' - are the labels for the x-axis and y-axis, respectively

        Labeli = '...' -  is the label for the function

        Colori - is the color of the line or dots (matplotlib color notation system)

        LWi - line width (number)

        Layout (general layouts for input dictionaries)
            S = {'F0': {'F': F0, 'X': X0, 'T': 'Dots', 'Label': 'Label1', 'Color': 'k', 'Line width': LW1},
            'F1': {'F': F, 'X': X, 'T': 'Line', 'Label': 'Label2', 'Color': 'k', 'Line width': LW2}}
            W = {'W1': {'S': S, 'ttl': 'LOL', 'axisX': 'axisX1', 'axisY': 'axisY1'}}

    :param key_save: A flag indicating whether to save the plot(s) as image file(s) or not.
    :param key_show: A flag indicating whether to display the plot(s) on the screen or not.
    :param path: The path to the directory where the image file(s) will be saved. If path is set to 'Default',
        the image file(s) will be saved in the Data/Chapter YYYY.MM.DD/ directory.
        "C:\\...\\FolderName" or 'Default'. If path = 'Default' then folder will be "Data/Chapter CurrentDate"
    :param height_of_picture: The height of the figure(s) in inches.
    :return:
    """

    if key_save & key_show:
        print("plot_sets_of_functions_2d. Cannot show and save at the same time")
    if key_save:
        now = datetime.datetime.now()
        now = datetime.date(now.year, now.month, now.day)
        if path == 'Default':
            N, P = check_log_folder()

    # Height_of_picture = 13 will be as your screen
    kW = list(dict.keys(W))
    for i in range(0, len(kW)):
        plt.figure(i, figsize=(height_of_picture, 768 * height_of_picture / 1366))  # for 1366 x 768 screen
        plt.title(W[kW[i]]['ttl'])
        plt.grid(which='major', fillstyle='left')
        kS = list(dict.keys(W[kW[i]]['S']))
        for j in range(0, len(kS)):
            T = W[kW[i]]['S'][kS[j]]['T']
            X = W[kW[i]]['S'][kS[j]]['X']
            F = W[kW[i]]['S'][kS[j]]['F']
            Label = W[kW[i]]['S'][kS[j]]['Label']
            Color = W[kW[i]]['S'][kS[j]]['Color']
            LW = W[kW[i]]['S'][kS[j]]['Line width']
            if isinstance(X[0], datetime.date):
                plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
                plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=15))
            if T == 'Line':
                plt.plot(X, F, color=Color, linewidth=LW, label=Label)  # plot(X, F) for lines
            if T == 'Dots':
                plt.plot(X, F, 'ko', label=Label)  # plot(X, F) for dots
            if T == 'Dash':
                plt.plot(X, F, '--', color=Color, linewidth=LW, label=Label)  # plot(X, F) for dash line
            if isinstance(X[0], datetime.date):
                plt.gcf().autofmt_xdate()
        plt.legend()
        if key_show:
            plt.show()
        if key_save:
            if path == 'Default':
                plt.savefig('Data/Chapter ' + str(now.year) + '.' + str(now.month) + '.' + str(now.day) + '/' + str(N)
                            + '.' + str(P + 1 + i) + '.png')
            else:
                plt.savefig(path + str('\\') + 'Figure ' + str(now.year) + '.' + str(now.month)
                            + '.' + str(now.day) + '.png')

    return


def plot_sets_of_functions_2d_example():
    line_2d_example()
    return
