# input
# product_name = "hagelslag"
# storage_location = "shelf"

# file stuff

def generate_pddl_obj(product_name):
    # FILE HANDLING
    f = open("./pddl_generators/problem_template_objects.pddl", "r")

    text_to_add = f.read()

    f.close()

    f = open("../retail_store_planning/pddl_files/problem_pick_place.pddl", "w")

    f.write(text_to_add)
    line_to_add = []
    for i in range(len(product_name)):
    	line_to_add.append(f"\t\t {product_name[i]} - object \n")
    for i in range(len(line_to_add)):
    	f.write(line_to_add[i])
    f.close()   
    f.close()    

def generate_pddl_init(product_names):
    f = open("./pddl_generators/problem_template_init.pddl", "r")

    text_to_add = f.read()

    f.close()

    f = open("../retail_store_planning/pddl_files/problem_pick_place.pddl", "a")

    product_name_to_table_converter = {
        "aruco_cube_111": "wp_table_2",
        "aruco_cube_222": "wp_table_2",
        "aruco_cube_333": "wp_table_3",
        "aruco_cube_444": "wp_table_3", 
        "aruco_cube_582": "wp_table_1"
    }


    f.write(text_to_add)
    line_to_add = []
    for i in range(len(product_names)):
    	line_to_add.append(f"\t\t(object-at {product_names[i]} {product_name_to_table_converter[product_names[i]]}) \n")
    for i in range(len(line_to_add)):
         f.write(line_to_add[i])
    f.close()    


def generate_pddl_goal(product_name, storage_location, packaging_bools):
    packaging_table_name = "wp_table_2"

    f = open("./pddl_generators/problem_template_goal.pddl", "r")

    text_to_add = f.read()

    f.close()


    f = open("../retail_store_planning/pddl_files/problem_pick_place.pddl", "a")
    f.write(text_to_add)
    line_to_add = []
    for i in range(len(product_name)):
        line_to_add.append(f"\t\t(object-at {product_name[i]} {storage_location[i]}) \n")
        if (packaging_bools[i]== True):
            line_to_add.append(
                f"\t\t(packaged-at {product_name[i]} {packaging_table_name}) \n")
    line_to_add.append(")) \n")
    line_to_add.append(") \n")
    for i in range(len(line_to_add)):
        f.write(line_to_add[i])
    f.close()  

def generate_pddl(product_name, simulation_name, storage_location,packaging_bools):
    # CONVERT PRODUCT TO ITEMS IN THE SIMULATION
    # wp_cabinet2 is de rechter kast
    # wp_cabinet1 is de linker kast
    storage_location_converter = {
        "freezer": "wp_cabinet_1",
        "shelf": "wp_cabinet_2"
        }#problem.pddl
    #product_to_cube_converter = dict()
    # product_to_cube_converter[product_name] = "aruco_cube_444"
    storage_locations = []
    for i in range(len(storage_location)):
    	storage_locations.append(storage_location_converter[storage_location[i]])
    
    generate_pddl_obj(simulation_name)
    generate_pddl_init(simulation_name)
    generate_pddl_goal(simulation_name, storage_locations,packaging_bools)
    
    print("PDDL code succesfully generated, you can now launch the simulation")

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
