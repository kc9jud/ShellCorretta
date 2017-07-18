nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/usda.int       usda.int     
         
nudel o_180020.trl
nudel o_180020.lnz
nudel o_180020.tmp
nudel o_180020.lev
nudel o_180220.trl
nudel o_180220.lnz
nudel o_180220.tmp
nudel o_180220.lev
nudel o_180420.trl
nudel o_180420.lnz
nudel o_180420.tmp
nudel o_180420.lev
         
nuaddint o_180ba.addint o_180.int o_180.ant
nucp  o_180.ppar p.par
nucp  o_180.npar n.par
nudel o_180sl.inf
NuShellX < o_180.modelx > o_180mod.out
NuShellX < o_180.levelx > o_180lev.out
nucp nul > opd.dat
source shellx.bat > o_180.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  ba0200.lph o_180020.eng o_180.modelx o_180.levelx ba0200.lpe > nucp.txt
nuren o_180020.lp ba0200.lp
nuren o_180020.ls ba0200.ls
nuren o_180020.nhw ba0200.nhw
nucp  ba0204.lph o_180220.eng o_180.modelx o_180.levelx ba0204.lpe > nucp.txt
nuren o_180220.lp ba0204.lp
nuren o_180220.ls ba0204.ls
nuren o_180220.nhw ba0204.nhw
nucp  ba0208.lph o_180420.eng o_180.modelx o_180.levelx ba0208.lpe > nucp.txt
nuren o_180420.lp ba0208.lp
nuren o_180420.ls ba0208.ls
nuren o_180420.nhw ba0208.nhw
nulev o_18a     
levp o_18a     
