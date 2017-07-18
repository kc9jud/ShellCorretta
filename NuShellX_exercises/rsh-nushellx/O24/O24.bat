nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/usdb.int       usdb.int     
         
nudel o_240080.trl
nudel o_240080.lnz
nudel o_240080.tmp
nudel o_240080.lev
nudel o_240180.trl
nudel o_240180.lnz
nudel o_240180.tmp
nudel o_240180.lev
nudel o_240280.trl
nudel o_240280.lnz
nudel o_240280.tmp
nudel o_240280.lev
nudel o_240380.trl
nudel o_240380.lnz
nudel o_240380.tmp
nudel o_240380.lev
nudel o_240480.trl
nudel o_240480.lnz
nudel o_240480.tmp
nudel o_240480.lev
nudel o_240580.trl
nudel o_240580.lnz
nudel o_240580.tmp
nudel o_240580.lev
nudel o_240680.trl
nudel o_240680.lnz
nudel o_240680.tmp
nudel o_240680.lev
         
nuaddint o_240bb.addint o_240.int o_240.ant
nucp  o_240.ppar p.par
nucp  o_240.npar n.par
nudel o_240sl.inf
NuShellX < o_240.modelx > o_240mod.out
NuShellX < o_240.levelx > o_240lev.out
nucp nul > opd.dat
source shellx.bat > o_240.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  bb0800.lph o_240080.eng o_240.modelx o_240.levelx bb0800.lpe > nucp.txt
nuren o_240080.lp bb0800.lp
nuren o_240080.ls bb0800.ls
nuren o_240080.nhw bb0800.nhw
nucp  bb0802.lph o_240180.eng o_240.modelx o_240.levelx bb0802.lpe > nucp.txt
nuren o_240180.lp bb0802.lp
nuren o_240180.ls bb0802.ls
nuren o_240180.nhw bb0802.nhw
nucp  bb0804.lph o_240280.eng o_240.modelx o_240.levelx bb0804.lpe > nucp.txt
nuren o_240280.lp bb0804.lp
nuren o_240280.ls bb0804.ls
nuren o_240280.nhw bb0804.nhw
nucp  bb0806.lph o_240380.eng o_240.modelx o_240.levelx bb0806.lpe > nucp.txt
nuren o_240380.lp bb0806.lp
nuren o_240380.ls bb0806.ls
nuren o_240380.nhw bb0806.nhw
nucp  bb0808.lph o_240480.eng o_240.modelx o_240.levelx bb0808.lpe > nucp.txt
nuren o_240480.lp bb0808.lp
nuren o_240480.ls bb0808.ls
nuren o_240480.nhw bb0808.nhw
nucp  bb080a.lph o_240580.eng o_240.modelx o_240.levelx bb080a.lpe > nucp.txt
nuren o_240580.lp bb080a.lp
nuren o_240580.ls bb080a.ls
nuren o_240580.nhw bb080a.nhw
nucp  bb080c.lph o_240680.eng o_240.modelx o_240.levelx bb080c.lpe > nucp.txt
nuren o_240680.lp bb080c.lp
nuren o_240680.ls bb080c.ls
nuren o_240680.nhw bb080c.nhw
nulev o_24b     
levp o_24b     
