# DO NOT use triple single quote, triple double quote or the python newline character

# Read the source code of this program
with open(__file__, 'r') as file:
    source_code = file.read()

# Find the index of the first occurrence of three quotes
split_index = source_code.find("\'\'\'")

# Define newline character so it isn't modified during compiler build
newLine = chr(10)

# Split the source code at the first occurrence of three quotes
if split_index == -1:
    print("Elratio program missing \'\'\'. This is a shameful mistake. The compiler will remember this.")
else:
    # Extract Elratio program
    program = source_code[split_index + 3:]
    program = program[:program.index("\'\'\'")]
    lines = program.split(newLine)

    

    # Execute Elratio program
    program = newLine.join(lines)
    exec(program)

# Elratio program (test case)
'''
# test 1
print("a"*20)

# test 2
if True:
    print(1000)

# test 3
import time
print(time.time())
'''
