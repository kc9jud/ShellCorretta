nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/usdb.int       usdb.int     
         
nudel o_210050.trl
nudel o_210050.lnz
nudel o_210050.tmp
nudel o_210050.lev
nudel o_210150.trl
nudel o_210150.lnz
nudel o_210150.tmp
nudel o_210150.lev
nudel o_210250.trl
nudel o_210250.lnz
nudel o_210250.tmp
nudel o_210250.lev
nudel o_210350.trl
nudel o_210350.lnz
nudel o_210350.tmp
nudel o_210350.lev
nudel o_210450.trl
nudel o_210450.lnz
nudel o_210450.tmp
nudel o_210450.lev
nudel o_210550.trl
nudel o_210550.lnz
nudel o_210550.tmp
nudel o_210550.lev
nudel o_210650.trl
nudel o_210650.lnz
nudel o_210650.tmp
nudel o_210650.lev
         
nuaddint o_210bb.addint o_210.int o_210.ant
nucp  o_210.ppar p.par
nucp  o_210.npar n.par
nudel o_210sl.inf
NuShellX < o_210.modelx > o_210mod.out
NuShellX < o_210.levelx > o_210lev.out
nucp nul > opd.dat
source shellx.bat > o_210.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  bb0501.lph o_210050.eng o_210.modelx o_210.levelx bb0501.lpe > nucp.txt
nuren o_210050.lp bb0501.lp
nuren o_210050.ls bb0501.ls
nuren o_210050.nhw bb0501.nhw
nucp  bb0503.lph o_210150.eng o_210.modelx o_210.levelx bb0503.lpe > nucp.txt
nuren o_210150.lp bb0503.lp
nuren o_210150.ls bb0503.ls
nuren o_210150.nhw bb0503.nhw
nucp  bb0505.lph o_210250.eng o_210.modelx o_210.levelx bb0505.lpe > nucp.txt
nuren o_210250.lp bb0505.lp
nuren o_210250.ls bb0505.ls
nuren o_210250.nhw bb0505.nhw
nucp  bb0507.lph o_210350.eng o_210.modelx o_210.levelx bb0507.lpe > nucp.txt
nuren o_210350.lp bb0507.lp
nuren o_210350.ls bb0507.ls
nuren o_210350.nhw bb0507.nhw
nucp  bb0509.lph o_210450.eng o_210.modelx o_210.levelx bb0509.lpe > nucp.txt
nuren o_210450.lp bb0509.lp
nuren o_210450.ls bb0509.ls
nuren o_210450.nhw bb0509.nhw
nucp  bb050b.lph o_210550.eng o_210.modelx o_210.levelx bb050b.lpe > nucp.txt
nuren o_210550.lp bb050b.lp
nuren o_210550.ls bb050b.ls
nuren o_210550.nhw bb050b.nhw
nucp  bb050d.lph o_210650.eng o_210.modelx o_210.levelx bb050d.lpe > nucp.txt
nuren o_210650.lp bb050d.lp
nuren o_210650.ls bb050d.ls
nuren o_210650.nhw bb050d.nhw
nulev o_21b     
levp o_21b     
