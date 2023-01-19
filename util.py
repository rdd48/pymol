from pymol import cmd
import glob

def ld(pdb_name='all'):
	for i in glob.glob(pdb_name):
		if i[-3:] in ('pdb', '.gz'):
			cmd.do('load {i}'.format(i=i))

def align_all(obj_to_align='all'):
    all_obj = cmd.get_object_list(obj_to_align)

    if len(all_obj) < 2:
        return 'You must provide at least two objects to align!'
    
    target = all_obj[0]
    for i in all_obj[1:]:
        cmd.do('align {i}, {target}'.format(i=i, target=target))

def save_all(save_path, obj_to_save='all'):
    if save_path[-1] != '/':
        save_path += '/'
    for i in cmd.get_object_list(obj_to_save):
        cmd.do('save {save_path}{i}.pdb, {i}'.format(save_path=save_path, i=i))

cmd.extend('ld', ld)
cmd.extend('align_all', align_all)
cmd.extend('save_all', save_all)
