def convert_c_to_f(temp_in_celsius):
    temp_in_fahrenheit = temp_in_celsius * 1.8 + 32
    return temp_in_fahrenheit

temp_in_c = int(input("Enter a celsius degree: "))


temp_in_f = convert_c_to_f(temp_in_c)

print(temp_in_f)