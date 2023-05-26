#
# contains simple interest formulas
#

import math

# Calculate rate of return (r) for an investment (PV) to become a future value (FV)
# when invested for a number of terms (n)


def rate_of_return(pv, fv, n):
    return (fv/pv)**(1/n)-1

# Calculate number of terms (n) required for an investment (PV) to become a future value (FV)
# when invested at an expected rate of return (r)


def num_of_terms(pv, fv, r):
    return math.log(fv/pv)/math.log(1+r)

# Calculate Future Value (FV) of an investment (PV) that is invested as a rate of return (r)
# over a number of terms (n)


def future_value(pv, r, n):
    return pv*(1+r)**n

# Calculate Present Value (PV) required to achieve a future value (FV) invested at a rate of return (r)
# over n number of terms (n)


def present_value(fv, r, n):
    return fv/(1+r)**n


