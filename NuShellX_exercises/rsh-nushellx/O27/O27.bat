nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/usdb.int       usdb.int     
         
nudel o_2700-0.trl
nudel o_2700-0.lnz
nudel o_2700-0.tmp
nudel o_2700-0.lev
nudel o_2701-0.trl
nudel o_2701-0.lnz
nudel o_2701-0.tmp
nudel o_2701-0.lev
nudel o_2702-0.trl
nudel o_2702-0.lnz
nudel o_2702-0.tmp
nudel o_2702-0.lev
         
nuaddint o_270bb.addint o_270.int o_270.ant
nucp  o_270.ppar p.par
nucp  o_270.npar n.par
nudel o_270sl.inf
NuShellX < o_270.modelx > o_270mod.out
NuShellX < o_270.levelx > o_270lev.out
nucp nul > opd.dat
source shellx.bat > o_270.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  bb0b01.lph o_2700-0.eng o_270.modelx o_270.levelx bb0b01.lpe > nucp.txt
nuren o_2700-0.lp bb0b01.lp
nuren o_2700-0.ls bb0b01.ls
nuren o_2700-0.nhw bb0b01.nhw
nucp  bb0b03.lph o_2701-0.eng o_270.modelx o_270.levelx bb0b03.lpe > nucp.txt
nuren o_2701-0.lp bb0b03.lp
nuren o_2701-0.ls bb0b03.ls
nuren o_2701-0.nhw bb0b03.nhw
nucp  bb0b05.lph o_2702-0.eng o_270.modelx o_270.levelx bb0b05.lpe > nucp.txt
nuren o_2702-0.lp bb0b05.lp
nuren o_2702-0.ls bb0b05.ls
nuren o_2702-0.nhw bb0b05.nhw
nulev o_27b     
levp o_27b     
