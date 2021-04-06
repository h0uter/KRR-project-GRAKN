from PDDL_GRAKN_interface import *
from PDDL_generation import generate_pddl


if __name__ == "__main__":
    # list all products in the KB
    print("All the products currently in the knowledgebase are:")
    read_all_products_in_KB()

    # ask user input
    new_product_yes_no = input("Do you want to add a new product? (y/n): ")

    if new_product_yes_no == "y":
        new_product_name = input("What is the name of the new product?: ")
        new_product_type = input(
            "What is the product group of the new product? (regular_product/freezer_product/fresh_product): ")

        write_to_KB(new_product_name, new_product_type)
        print("All the products currently in the knowledgebase are:")
        read_all_products_in_KB()

    iterations = input("how many items are in the simulation? (int) :")

    product_names = []
    simulation_names = []
    storage_locations = []
    packaging_bools = []
    for i in range(int(iterations)):
        print("for product", (i + 1),":")

        product_name = input("What is the name of product " + str(i+1) + "?: ")

        storage_type, needs_packaging = read_from_KB(product_name)
        storage_locations.append(storage_type)
        packaging_bools.append(needs_packaging)
    	        
        cube_number = input("Which cube number do you want to assign to the product? (111, 222, 333, 444, 582):")
        simulation_name = "aruco_cube_" + cube_number 

        product_names.append(product_name)
        simulation_names.append(simulation_name)

    generate_pddl(product_names, simulation_names, storage_locations, packaging_bools)
