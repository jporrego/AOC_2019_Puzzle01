# Collects the weight of each module and adds it to "modules_mass" list
data_input = open("p01_input.txt", "r")
modules_mass = []

for line in data_input:
	modules_mass.append(int(line))

# Uses map to aplly "fuel_calculator" function to each module 
# Saves results to "fuel_per_module" list and calculates total fuel required, then prints it.
def fuel_calculator(module):
	return (int(module/3)-2)

fuel_per_module = list(map(fuel_calculator, modules_mass))
total_fuel = sum(fuel_per_module)

print(total_fuel)