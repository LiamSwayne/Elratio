# Read the source code of this program
with open(__file__, 'r') as file:
    source_code = file.read()

# Find the index of the first occurrence of three quotes
split_index = source_code.find('\'\'\'')

# Split the source code at the first occurrence of three quotes
if split_index == -1:
    print("Elratio porgram missing \'\'\'. This is a shameful mistake. The compiler will remember this.")
else:
    # Slice to Elratio program
    program = source_code[split_index + 3:]
    program = program[:program.index('\'\'\'')]

    # Execute Elratio program
    exec(program)

# Elratio only executes code inside the quotes
'''
print("a"*20)
if True:
    print(1000)
'''
