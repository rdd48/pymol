from pymol import cmd

def print_sele(dist=6, dist2=7, chain_sel='F', sele='sele'):
    cmd.do('select c1, chain {chain_sel} and sc. within {dist} of {sele}'.format(chain_sel=chain_sel, dist=dist, sele=sele))
    cmd.do('select c2, chain {chain_sel} and name C+CA+N+O within {dist2} of {sele}'.format(chain_sel=chain_sel, dist2=dist2, sele=sele))
    cmd.do('stored.print_resis = set()')
    cmd.do('iterate c1, stored.print_resis.add(int(resi))')
    cmd.do('iterate c2, stored.print_resis.add(int(resi))')
    cmd.do('print(" ".join([str(i) for i in sorted(list(stored.print_resis))]))')
    cmd.do('delete c1')
    cmd.do('delete c2')



cmd.extend( "print_sele", print_sele )