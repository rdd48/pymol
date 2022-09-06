from pymol import cmd
import glob

def ld(pdb_name=all):
	pdbs = glob.glob(pdb_name)
	print(pdbs)
	for i in pdbs:
		if i[-3:] == 'pdb':
			cmd.do('load {i}'.format(i=i))
		elif i[-3:] == '.gz':
			cmd.do('load {i}'.format(i=i))



cmd.extend( "ld", ld)