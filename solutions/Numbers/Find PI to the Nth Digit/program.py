print("Welcome to Find PI to the Nth Digit")
number = int(input("Input number to be "))


# Formulas on https://iq.opengenus.org/different-ways-to-calculate-pi/

##### Leibniz’s Formula

# # My First solution
# def formula(increment):
#     formula_result = 0
#     numerator = 4.0
#     denominator = 3.0
#     counter = 1
#     for i in range(increment):
#         increment_result = numerator / denominator
#         print("Increment_result = ", end=""), print(increment_result)
#         denominator += 2.0
#         print("Current_Counter = ", end=""), print(counter)
#         if (counter % 2) == 0:
#             print("Before leaving1 = ", end=""), print(formula_result)
#             formula_result += increment_result
#             print("Before leaving2 = ", end=""), print(formula_result)
#         elif (counter % 2) == 1:
#             print("Before leaving3 = ", end=""), print(formula_result)
#             formula_result -= increment_result
#             print("Before leaving4 = ", end=""), print(formula_result)
#         counter += 1
#         print("Current_result = ", end=""), print(formula_result, end="\n\n")
#     return formula_result+4
#
# result = formula(number)
# print("Operation final result = ", end=""), print(result)

# Cleaner and seeing a possible solution
# For accurate result, input number 1000000
def formula(increment):
    formula_result = 0
    denominator = 1
    counter = 0
    for i in range(increment):
        increment_result = 4 / denominator
        if (counter % 2) == 0:
            formula_result += increment_result
        elif (counter % 2) == 1:
            formula_result -= increment_result
        denominator += 2.0
        counter += 1
    return formula_result

result = formula(number)
print("Operation final result = ", end=""), print(result)


