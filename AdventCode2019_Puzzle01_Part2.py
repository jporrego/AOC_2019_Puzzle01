# Collects the weight of each module and adds it to "modules_mass" list
data_input = open("p01_input.txt", "r")
modules_mass = []

for line in data_input:
	modules_mass.append(int(line))

# Uses map to aplly "fuel_calculator" function to each module. This calcultes fuel requierd for the module and fuel required for the fuel itself. 
# Saves results to "fuel_per_module" list and calculates total fuel required, then prints it.
def fuel_calculator(module):
	module_fuel = int(module/3)-2
	if int(module_fuel/3)-2 > 0:
		fuel_fuel = []
		x = int(module_fuel/3)-2
		while x > 0:
			fuel_fuel.append(x)
			x = int(x/3)-2
		return (module_fuel + sum(fuel_fuel)) 
	else:
		return module_fuel

fuel_per_module = list(map(fuel_calculator, modules_mass))

total_fuel = sum(fuel_per_module)

print(total_fuel)