# Elratio compiler
exec("""\n\n\nwith open(__file__, 'r') as file:\n    source_code = file.read()\n\n\nsplit_index = source_code.find(\"\'\'\'\")\n\n\nnewLine = chr(10)\n\n\nif split_index == -1:\n    print(\"Elratio program missing \'\'\'. This is a shameful mistake. The compiler will remember this.\")\nelse:\n    \n    program = source_code[split_index + 3:]\n    program = program[:program.index(\"\'\'\'\")]\n    lines = program.split(newLine)\n\n    \n\n    \n    program = newLine.join(lines)\n    exec(program)\n\n""")

# Elratio program
'''

'''