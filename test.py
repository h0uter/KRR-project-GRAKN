

f = open("problem2.pddl", "r")

text_to_add = f.read()

f.close()

f = open("problem.pddl", "w")

f.write(text_to_add)

f.close()

f = open("problem.pddl", "a")

line = ["test \n"]
line.append(")) \n")
line.append(") \n")
for i in range(len(line)):
    f.write(line[i])

f.close()
