import datetime
import os


def open_log() -> list:
    """
    File f = "Data/Log.txt". File f contains a row with textual info "D0 D1 D2 N P". D0.D1.D2 - date "YYYY.MM.DD".
    N - current number of the set of pictures. P - current number of the picture from the set.

    :return: k = [D0, D1, D2, N, P]
    """

    f = open('Data/Log', 'r+')
    k = dict(enumerate((list(f))))[0].split()  # creates dict {0:M1, 1:M2, 2:M3, ... (N-1):N}
    k = [int(k[i]) for i in range(0, 5)]
    f.close()

    return k


def check_log_folder() -> [int, int]:
    """
    makes folder "Data/Chapter D0.D1.D2 and gets quantities N, P (see open_log)

    :return: N, P
    """
    now = datetime.datetime.now()
    now = datetime.date(now.year, now.month, now.day)
    k = open_log()

    if (now.day == k[2]) & (now.month == k[1]) & (now.year == k[0]):  # if D0.D1.D2 from file is literally today
        N = k[3] + 1  # continue counting experiments
        P = k[4]
        f = open('Data/Log', 'w+')
        f.write(str(now.year) + ' ' + str(now.month) + ' ' + str(now.day) + ' ' + str(N) + ' ' + str(0))
    else:  # if D0.D1.D2 from file isn't today
        # makes folder "Data/Chapter D0.D1.D2"
        os.makedirs('Data/Chapter ' + str(now.year) + '.' + str(now.month) + '.' + str(now.day))
        # makes folder "Data/Chapter D0.D1.D2"
        N = 1  # start counting sets of experiments from 1-st
        P = 0  # start counting experiments in the set from 1-st
        f = open('Data/Log', 'w+')
        f.write(str(now.year) + ' ' + str(now.month) + ' ' + str(now.day) + ' ' + str(N) + ' ' + str(0))
    f.close()

    return N, P
