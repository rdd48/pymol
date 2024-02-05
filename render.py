from pymol import cmd

# 1. set path to pse in line 6
# 2. set file name and path for output png (line 9)
# 3. submit script to scheduler

cmd.do('load /path/to/.pse')
cmd.do('ray')
cmd.do('png /path/to/output.png')