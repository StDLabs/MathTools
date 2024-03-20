

def numerical_integration(F: list, Fm: list, X: list, a: float, b: float, rule: str, step: str) -> float:
    """
    Performs numerical integration using various rules, such as the rectangular, trapezoidal, and Simpson's rules.
    Supports both constant and variable step sizes

        rule = 'left rectangular' - Left rectangle rule of numerical integration

        rule = 'right rectangular' - Right rectangle rule of numerical integration

        rule = 'middle rectangular' - Middle rectangle rule of numerical integration

        rule = 'trapezoidal' - Trapezoidal rule of numerical integration

        rule = 'simpson' - Simpson's rule of numerical integration

    :param F: F = [F0, F1, ...]
    :param Fm: Fm = [Fm01, Fm12, Fm23, ...] - mid points between Fi and Fi+1 for Middle rectangular rule
    :param X: X = [X0, X1, ...] (for variable step)
    :param a: left boundary (for constant step)
    :param b: right boundary (for constant step)

    :param rule: The name of the integration rule to be used, such as 'left rectangular', 'right rectangular',
        'middle rectangular', 'trapezoidal', or 'simpson'.

        rule = 'left rectangular' - Left rectangle rule of numerical integration
        rule = 'right rectangular' - Right rectangle rule of numerical integration
        rule = 'middle rectangular' - Middle rectangle rule of numerical integration
        rule = 'trapezoidal' - Trapezoidal rule of numerical integration
        rule = 'simpson' - Simpson's rule of numerical integration

    :param step: step = 'constant' or 'variable'. Specifies whether the integration should use a
        'constant' or 'variable' step size.

    :return: approximate value of the integral
    """

    n = len(F)  # number of points
    value = 0
    if step == 'constant':
        h = (b - a) / (n - 1)
        if rule == 'left rectangular':
            for i in range(0, n - 1):
                value += F[i] * h
        if rule == 'right rectangular':
            for i in range(0, n - 1):
                value += F[i + 1] * h
        if rule == 'middle rectangular':
            for i in range(0, int((n - 1) / 2)):
                value += Fm[i] * 2 * h
        if rule == 'trapezoidal':
            for i in range(0, n - 1):
                value += (F[i] + F[i + 1]) * (h / 2)
        if rule == 'simpson':
            if (n - 1) % 2 != 0:
                print('numerical_integration.simpson: N must be an odd number')
            for i in range(0, int((n - 1) / 2)):
                value += (F[2 * i] + 4 * F[2 * i + 1] + F[2 * i + 2]) * h / 3
    if step == 'variable':
        if rule == 'left rectangular':
            for i in range(0, n - 1):
                value += F[i] * (X[i + 1] - X[i])
        if rule == 'right rectangular':
            for i in range(0, n - 1):
                value += F[i + 1] * (X[i + 1] - X[i])
        if rule == 'middle rectangular':
            for i in range(0, int((n - 1) / 2)):
                value += Fm[i] * (X[2 * i + 2] - X[2 * i])
        if rule == 'trapezoidal':
            for i in range(0, n - 1):
                value += (F[i] + F[i + 1]) * ((X[i + 1] - X[i]) / 2)
        if rule == 'simpson':
            print("Numerical_Integration. There is no code for Simpson rule and variable step")

    return value
