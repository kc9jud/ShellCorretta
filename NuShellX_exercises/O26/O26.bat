nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/usdb.int       usdb.int     
         
nudel o_2600_0.trl
nudel o_2600_0.lnz
nudel o_2600_0.tmp
nudel o_2600_0.lev
nudel o_2601_0.trl
nudel o_2601_0.lnz
nudel o_2601_0.tmp
nudel o_2601_0.lev
nudel o_2602_0.trl
nudel o_2602_0.lnz
nudel o_2602_0.tmp
nudel o_2602_0.lev
nudel o_2603_0.trl
nudel o_2603_0.lnz
nudel o_2603_0.tmp
nudel o_2603_0.lev
nudel o_2604_0.trl
nudel o_2604_0.lnz
nudel o_2604_0.tmp
nudel o_2604_0.lev
         
nuaddint o_260bb.addint o_260.int o_260.ant
nucp  o_260.ppar p.par
nucp  o_260.npar n.par
nudel o_260sl.inf
NuShellX < o_260.modelx > o_260mod.out
NuShellX < o_260.levelx > o_260lev.out
nucp nul > opd.dat
source shellx.bat > o_260.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  bb0a00.lph o_2600_0.eng o_260.modelx o_260.levelx bb0a00.lpe > nucp.txt
nuren o_2600_0.lp bb0a00.lp
nuren o_2600_0.ls bb0a00.ls
nuren o_2600_0.nhw bb0a00.nhw
nucp  bb0a02.lph o_2601_0.eng o_260.modelx o_260.levelx bb0a02.lpe > nucp.txt
nuren o_2601_0.lp bb0a02.lp
nuren o_2601_0.ls bb0a02.ls
nuren o_2601_0.nhw bb0a02.nhw
nucp  bb0a04.lph o_2602_0.eng o_260.modelx o_260.levelx bb0a04.lpe > nucp.txt
nuren o_2602_0.lp bb0a04.lp
nuren o_2602_0.ls bb0a04.ls
nuren o_2602_0.nhw bb0a04.nhw
nucp  bb0a06.lph o_2603_0.eng o_260.modelx o_260.levelx bb0a06.lpe > nucp.txt
nuren o_2603_0.lp bb0a06.lp
nuren o_2603_0.ls bb0a06.ls
nuren o_2603_0.nhw bb0a06.nhw
nucp  bb0a08.lph o_2604_0.eng o_260.modelx o_260.levelx bb0a08.lpe > nucp.txt
nuren o_2604_0.lp bb0a08.lp
nuren o_2604_0.ls bb0a08.ls
nuren o_2604_0.nhw bb0a08.nhw
nulev o_26b     
levp o_26b     
