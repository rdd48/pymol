from pymol import cmd

def get_all_chi_dihedrals(obj):
    num_resis = len(cmd.get_model(obj).get_residues())

    all_dihedrals = []
    for resi in range(num_resis-1):
        for chain in cmd.get_chains(obj):
            base = f'{obj} and chain {chain} and resi {resi} and name '
            base_next = f'{obj} and chain {chain} and resi {resi+1} and name '
            try:
                all_dihedrals.append(
                    cmd.get_dihedral(base + 'CA',base + 'C',base_next + 'N',base_next + 'CA')
                )
            except:
                continue
    
    print(all_dihedrals)

def get_near_zero_dihedrals(obj):
    num_resis = len(cmd.get_model(obj).get_residues())

    all_dihedrals = []
    for resi in range(num_resis-1):
        for chain in cmd.get_chains(obj):
            base = f'{obj} and chain {chain} and resi {resi} and name '
            base_next = f'{obj} and chain {chain} and resi {resi+1} and name '
            try:
                dihedral = cmd.get_dihedral(base + 'CA',base + 'C',base_next + 'N',base_next + 'CA')
                if abs(dihedral) < 10.0:
                    print(f'resi {resi}, {resi+1}')
            except:
                continue

cmd.extend('get_all_chi_dihedrals', get_all_chi_dihedrals)
cmd.extend('get_near_zero_dihedrals', get_near_zero_dihedrals)