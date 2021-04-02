# input
product_name = "hagelslag"
storage_location = "freezer"

# file stuff



f = open("problem_template.pddl", "r")

text_to_add = f.read()

f.close()

f = open("problem.pddl", "w")

f.write(text_to_add)

f.close()

f = open("problem.pddl", "a")

storage_location_converter = {
    "freezer":"wp_cabinet_1",
    "shelf": "wp_cabinet_2"
    }


product_to_cube_converter = dict()
product_to_cube_converter[product_name] = "aruco_cube_444"


line1 = f"\t\t(object-at {product_to_cube_converter[product_name]} {storage_location_converter[storage_location]}) \n"
print(line1)

# line = ["test \n", ]
line = [line1]
line.append(")) \n")
line.append(") \n")
for i in range(len(line)):
    f.write(line[i])

f.close()
