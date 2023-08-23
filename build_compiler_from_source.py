def remove_comments(code):
    lines = code.split('\n')
    in_block_comment = False
    result = []

    for line in lines:
        if in_block_comment:
            if line.rstrip().endswith("'''") or line.rstrip().endswith('"""'):
                in_block_comment = False
            continue
        elif line.lstrip().startswith("'''") or line.lstrip().startswith('"""'):
            if line.rstrip().endswith("'''") or line.rstrip().endswith('"""'):
                continue
            else:
                in_block_comment = True
                continue
        
        if '#' in line:
            line = line[:line.index('#')]
        
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
cleaned_code = cleaned_code.replace('\n', '\\n').replace('\"', '\\\"')
wrapped_code = "# Elratio compiler (turn off line-wrapping or you'll see the entire Elratio source code)\nexec(\"\"\"" + cleaned_code + "\"\"\")\n\n# Elratio program\n\'\'\'\n\n\'\'\'"

compiler_file = open('compiler.py', 'w')
compiler_file.write(wrapped_code)
compiler_file.close()
