def remove_comments(code):
    lines = code.split('\n')
    in_block_comment = False
    result = []

    for line in lines:
        line = line.strip()

        if in_block_comment:
            if line.endswith("'''") or line.endswith('"""'):
                in_block_comment = False
            continue
        elif line.startswith("'''") or line.startswith('"""'):
            if line.endswith("'''") or line.endswith('"""'):
                continue
            else:
                in_block_comment = True
                continue
        
        if '#' in line:
            line = line[:line.index('#')]
        
        if line:
            result.append(line)
    
    return '\n'.join(result)

source_file = open('source.py', 'r')
source_code = ""
for line in source_file:
    if "# Elratio program" in line:
        break
    source_code += line
source_file.close()

cleaned_code = remove_comments(source_code)
wrapped_code = "# Elratio compiler\nexec('''" + cleaned_code.replace("\n", " ") + "''')\n\n# Elratio program\n\'\'\'\n\n\'\'\'"

compiler_file = open('compiler.py', 'w')
compiler_file.write(wrapped_code)
compiler_file.close()
