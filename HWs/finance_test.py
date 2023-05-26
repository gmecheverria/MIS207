#
# test the finance.py module
#

# allows the use of finance module
import finance

print(finance.num_of_terms(1000, 12000, 0.05))  # approx. 50.93048347119194

print(finance.rate_of_return(1500, 25000, 12))  # approx. 0.264214389215486

print(finance.future_value(700, 0.04, 10))  # approx. 1036.170999442841

print(finance.present_value(12500, 0.05, 12))  # approx. 6960.46772721949



