nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/usdb.int       usdb.int     
         
nudel o_190030.trl
nudel o_190030.lnz
nudel o_190030.tmp
nudel o_190030.lev
nudel o_190130.trl
nudel o_190130.lnz
nudel o_190130.tmp
nudel o_190130.lev
nudel o_190230.trl
nudel o_190230.lnz
nudel o_190230.tmp
nudel o_190230.lev
nudel o_190330.trl
nudel o_190330.lnz
nudel o_190330.tmp
nudel o_190330.lev
nudel o_190430.trl
nudel o_190430.lnz
nudel o_190430.tmp
nudel o_190430.lev
nudel o_190530.trl
nudel o_190530.lnz
nudel o_190530.tmp
nudel o_190530.lev
         
nuaddint o_190bb.addint o_190.int o_190.ant
nucp  o_190.ppar p.par
nucp  o_190.npar n.par
nudel o_190sl.inf
NuShellX < o_190.modelx > o_190mod.out
NuShellX < o_190.levelx > o_190lev.out
nucp nul > opd.dat
source shellx.bat > o_190.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  bb0301.lph o_190030.eng o_190.modelx o_190.levelx bb0301.lpe > nucp.txt
nuren o_190030.lp bb0301.lp
nuren o_190030.ls bb0301.ls
nuren o_190030.nhw bb0301.nhw
nucp  bb0303.lph o_190130.eng o_190.modelx o_190.levelx bb0303.lpe > nucp.txt
nuren o_190130.lp bb0303.lp
nuren o_190130.ls bb0303.ls
nuren o_190130.nhw bb0303.nhw
nucp  bb0305.lph o_190230.eng o_190.modelx o_190.levelx bb0305.lpe > nucp.txt
nuren o_190230.lp bb0305.lp
nuren o_190230.ls bb0305.ls
nuren o_190230.nhw bb0305.nhw
nucp  bb0307.lph o_190330.eng o_190.modelx o_190.levelx bb0307.lpe > nucp.txt
nuren o_190330.lp bb0307.lp
nuren o_190330.ls bb0307.ls
nuren o_190330.nhw bb0307.nhw
nucp  bb0309.lph o_190430.eng o_190.modelx o_190.levelx bb0309.lpe > nucp.txt
nuren o_190430.lp bb0309.lp
nuren o_190430.ls bb0309.ls
nuren o_190430.nhw bb0309.nhw
nucp  bb030b.lph o_190530.eng o_190.modelx o_190.levelx bb030b.lpe > nucp.txt
nuren o_190530.lp bb030b.lp
nuren o_190530.ls bb030b.ls
nuren o_190530.nhw bb030b.nhw
nulev o_19b     
levp o_19b     
