# input
# product_name = "hagelslag"
# storage_location = "shelf"

# file stuff

def generate_pddl_obj(product_name):
    # FILE HANDLING
    f = open("pddl_generators/problem_template_objects.pddl", "r")

    text_to_add = f.read()

    f.close()

    f = open("problem.pddl", "w")

    f.write(text_to_add)
    line_to_add = []
    for i in range(len(product_name)):
    	line_to_add.append(f"\t\t {product_name[i]} - object \n")
    for i in range(len(line_to_add)):
    	f.write(line_to_add[i])
    f.close()   
    f.close()    

def generate_pddl_init(product_name):
    f = open("pddl_generators/problem_template_init.pddl", "r")

    text_to_add = f.read()

    f.close()

    f = open("problem.pddl", "a")

    f.write(text_to_add)
    line_to_add = []
    for i in range(len(product_name)):
    	line_to_add.append(f"\t\t(object-at {product_name[i]} wp_table_1) \n")
    	line_to_add.append(f"\t\t(active {product_name[i]}) \n")
    for i in range(len(line_to_add)):
         f.write(line_to_add[i])
    f.close()    


def generate_pddl_goal(product_name, storage_location):
    f = open("pddl_generators/problem_template_goal.pddl", "r")

    text_to_add = f.read()

    f.close()

    f = open("problem.pddl", "a")
    f.write(text_to_add)
    line_to_add = []
    for i in range(len(product_name)):
    	line_to_add.append(f"\t\t(object-at {product_name[i]} {storage_location[i]}) \n")
    line_to_add.append(")) \n")
    line_to_add.append(") \n")
    for i in range(len(line_to_add)):
        f.write(line_to_add[i])
    f.close()  

def generate_pddl(product_name, simulation_name, storage_location):
    # CONVERT PRODUCT TO ITEMS IN THE SIMULATION
    storage_location_converter = {
        "freezer": "wp_cabinet_1",
        "shelf": "wp_cabinet_2"
        }
    # freezer -> wp_cabinet_1 | shelf -> wp_cabinet_2
    
    # maybe usefull for later when adding more than one product.
    #product_to_cube_converter = dict()
    # product_to_cube_converter[product_name] = "aruco_cube_444"
    storage_locations = []
    for i in range(len(storage_location)):
    	storage_locations.append(storage_location_converter[storage_location[i]])
    
    generate_pddl_obj(simulation_name)
    generate_pddl_init(simulation_name)
    generate_pddl_goal(simulation_name, storage_locations)
    

    # FILE HANDLING
    #f = open("problem_template.pddl", "r")

    #text_to_add = f.read()

    #f.close()

    #f = open("problem.pddl", "w")

    #f.write(text_to_add)

    #f.close()

    #f = open("problem.pddl", "a")

    # TODO: ook initial conditions schrijven

    #line1 = f"\t\t(object-at {product_to_cube_converter[product_name]} {storage_location_converter[storage_location]}) \n"
    #print(line1)

    # line = ["test \n", ]
    #line = [line1]


    #f.close()
