         
nudel o_230070.trl
nudel o_230070.lnz
nudel o_230070.tmp
nudel o_230070.lev
nudel o_230170.trl
nudel o_230170.lnz
nudel o_230170.tmp
nudel o_230170.lev
nudel o_230270.trl
nudel o_230270.lnz
nudel o_230270.tmp
nudel o_230270.lev
nudel o_230370.trl
nudel o_230370.lnz
nudel o_230370.tmp
nudel o_230370.lev
nudel o_230470.trl
nudel o_230470.lnz
nudel o_230470.tmp
nudel o_230470.lev
nudel o_230570.trl
nudel o_230570.lnz
nudel o_230570.tmp
nudel o_230570.lev
nudel o_230670.trl
nudel o_230670.lnz
nudel o_230670.tmp
nudel o_230670.lev
         
nuaddint o_230bb.addint o_230.int o_230.ant
nucp  o_230.ppar p.par
nucp  o_230.npar n.par
nudel o_230sl.inf
NuShellX < o_230.modelx > o_230mod.out
NuShellX < o_230.levelx > o_230lev.out
nucp nul > opd.dat
source shellx.bat > o_230.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  bb0701.lph o_230070.eng o_230.modelx o_230.levelx bb0701.lpe > nucp.txt
nuren o_230070.lp bb0701.lp
nuren o_230070.ls bb0701.ls
nuren o_230070.nhw bb0701.nhw
nucp  bb0703.lph o_230170.eng o_230.modelx o_230.levelx bb0703.lpe > nucp.txt
nuren o_230170.lp bb0703.lp
nuren o_230170.ls bb0703.ls
nuren o_230170.nhw bb0703.nhw
nucp  bb0705.lph o_230270.eng o_230.modelx o_230.levelx bb0705.lpe > nucp.txt
nuren o_230270.lp bb0705.lp
nuren o_230270.ls bb0705.ls
nuren o_230270.nhw bb0705.nhw
nucp  bb0707.lph o_230370.eng o_230.modelx o_230.levelx bb0707.lpe > nucp.txt
nuren o_230370.lp bb0707.lp
nuren o_230370.ls bb0707.ls
nuren o_230370.nhw bb0707.nhw
nucp  bb0709.lph o_230470.eng o_230.modelx o_230.levelx bb0709.lpe > nucp.txt
nuren o_230470.lp bb0709.lp
nuren o_230470.ls bb0709.ls
nuren o_230470.nhw bb0709.nhw
nucp  bb070b.lph o_230570.eng o_230.modelx o_230.levelx bb070b.lpe > nucp.txt
nuren o_230570.lp bb070b.lp
nuren o_230570.ls bb070b.ls
nuren o_230570.nhw bb070b.nhw
nucp  bb070d.lph o_230670.eng o_230.modelx o_230.levelx bb070d.lpe > nucp.txt
nuren o_230670.lp bb070d.lp
nuren o_230670.ls bb070d.ls
nuren o_230670.nhw bb070d.nhw
nulev o_23b     
levp o_23b     
