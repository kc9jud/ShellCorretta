nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/usdb.int       usdb.int     
         
nudel o_2800c0.trl
nudel o_2800c0.lnz
nudel o_2800c0.tmp
nudel o_2800c0.lev
         
nuaddint o_280bb.addint o_280.int o_280.ant
nucp  o_280.ppar p.par
nucp  o_280.npar n.par
nudel o_280sl.inf
NuShellX < o_280.modelx > o_280mod.out
NuShellX < o_280.levelx > o_280lev.out
nucp nul > opd.dat
source shellx.bat > o_280.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  bb0c00.lph o_2800c0.eng o_280.modelx o_280.levelx bb0c00.lpe > nucp.txt
nuren o_2800c0.lp bb0c00.lp
nuren o_2800c0.ls bb0c00.ls
nuren o_2800c0.nhw bb0c00.nhw
nulev o_28b     
levp o_28b     
