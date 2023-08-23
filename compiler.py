# Elratio compiler
exec("""\nwith open(__file__, 'r') as file:\n    source_code = file.read()\n\n\nsplit_index = source_code.find(\"\'\'\'\")\n\n\nif split_index == -1:\n    print(\"Elratio porgram missing \'\'\'. This is a shameful mistake. The compiler will remember this.\")\nelse:\n    \n    program = source_code[split_index + 3:]\n    program = program[:program.index(\"\'\'\'\")]\n\n    \n    exec(program)\n\n""")

# Elratio program
'''

'''