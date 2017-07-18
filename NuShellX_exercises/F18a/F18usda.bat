nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/usda.int       usda.int     
         
nudel f_180011.trl
nudel f_180011.lnz
nudel f_180011.tmp
nudel f_180011.lev
nudel f_180111.trl
nudel f_180111.lnz
nudel f_180111.tmp
nudel f_180111.lev
nudel f_180211.trl
nudel f_180211.lnz
nudel f_180211.tmp
nudel f_180211.lev
nudel f_180311.trl
nudel f_180311.lnz
nudel f_180311.tmp
nudel f_180311.lev
nudel f_180411.trl
nudel f_180411.lnz
nudel f_180411.tmp
nudel f_180411.lev
nudel f_180511.trl
nudel f_180511.lnz
nudel f_180511.tmp
nudel f_180511.lev
         
nuaddint f_180ba.addint f_180.int f_180.ant
nucp  f_180.ppar p.par
nucp  f_180.npar n.par

nudel f_180sl.inf
NuShellX < f_180.modelx > f_180mod.out
NuShellX < f_180.levelx > f_180lev.out
source shellx.bat > f_180.cpu
nuren shellx.bat shellx1.bat
nucp  ba1200.lph f_180011.eng f_180.modelx f_180.levelx ba1200.lpe > nucp.txt
nuren f_180011.lp ba1200.lp
nuren f_180011.ls ba1200.ls
nuren f_180011.nhw ba1200.nhw
nucp  ba1202.lph f_180111.eng f_180.modelx f_180.levelx ba1202.lpe > nucp.txt
nuren f_180111.lp ba1202.lp
nuren f_180111.ls ba1202.ls
nuren f_180111.nhw ba1202.nhw
nucp  ba1204.lph f_180211.eng f_180.modelx f_180.levelx ba1204.lpe > nucp.txt
nuren f_180211.lp ba1204.lp
nuren f_180211.ls ba1204.ls
nuren f_180211.nhw ba1204.nhw
nucp  ba1206.lph f_180311.eng f_180.modelx f_180.levelx ba1206.lpe > nucp.txt
nuren f_180311.lp ba1206.lp
nuren f_180311.ls ba1206.ls
nuren f_180311.nhw ba1206.nhw
nucp  ba1208.lph f_180411.eng f_180.modelx f_180.levelx ba1208.lpe > nucp.txt
nuren f_180411.lp ba1208.lp
nuren f_180411.ls ba1208.ls
nuren f_180411.nhw ba1208.nhw
nucp  ba120a.lph f_180511.eng f_180.modelx f_180.levelx ba120a.lpe > nucp.txt
nuren f_180511.lp ba120a.lp
nuren f_180511.ls ba120a.ls
nuren f_180511.nhw ba120a.nhw
nulev f_18a     
levp f_18a     
