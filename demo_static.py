from PDDL_GRAKN_interface import *
from PDDL_generation import generate_pddl

if __name__ == "__main__":
    # list all products in the KB
    print("All the products currently in the knowledgebase are:")
    read_all_products_in_KB()

    # ask user input
    # new_product_yes_no = input("Do you want to add a new product? (y/n): ")
    new_product_yes_no = "y"

    if new_product_yes_no == "y":
        # new_product_name = input("What is the name of the new product: ")
        new_product_name = "kip1"

        # new_product_type = input(
        #     "What is the product group of the new product? (regular_product/freezer_product/fresh_product): ")
        group_of_new_product = "freezer_product"

        write_to_KB(new_product_name, group_of_new_product)
        # write_to_KB(new_product_name, new_product_type)
        print("All the products currently in the knowledgebase are:")
        read_all_products_in_KB()

    # iterations = input("how many items are in the simulation? (int) :")
    iterations = 3

    product_names = []
    simulation_names = []
    storage_locations = []
    packaging_bools = []
    for i in range(int(iterations)):
        print("for product", (i + 1),":")
    generate_pddl(product_names, simulation_names, storage_locations, packaging_bools)
    product_names.append(product_name)
    simulation_names.append(simulation_name)

    generate_pddl(product_names, simulation_names, storage_locations, packaging_bools)
