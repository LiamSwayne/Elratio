# Elratio compiler
exec('''with open(__file__, 'r') as file: source_code = file.read() split_index = source_code.find('\'\'\'') if split_index == -1: print("Elratio porgram missing \'\'\'. This is a shameful mistake. The compiler will remember this.") else: program = source_code[split_index + 3:] program = program[:program.index('\'\'\'')] exec(program)''')

# Elratio program
'''

'''