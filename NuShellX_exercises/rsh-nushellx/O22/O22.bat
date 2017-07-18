nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/usdb.int       usdb.int     
         
nudel o_220060.trl
nudel o_220060.lnz
nudel o_220060.tmp
nudel o_220060.lev
nudel o_220160.trl
nudel o_220160.lnz
nudel o_220160.tmp
nudel o_220160.lev
nudel o_220260.trl
nudel o_220260.lnz
nudel o_220260.tmp
nudel o_220260.lev
nudel o_220360.trl
nudel o_220360.lnz
nudel o_220360.tmp
nudel o_220360.lev
nudel o_220460.trl
nudel o_220460.lnz
nudel o_220460.tmp
nudel o_220460.lev
nudel o_220560.trl
nudel o_220560.lnz
nudel o_220560.tmp
nudel o_220560.lev
nudel o_220660.trl
nudel o_220660.lnz
nudel o_220660.tmp
nudel o_220660.lev
nudel o_220760.trl
nudel o_220760.lnz
nudel o_220760.tmp
nudel o_220760.lev
         
nuaddint o_220bb.addint o_220.int o_220.ant
nucp  o_220.ppar p.par
nucp  o_220.npar n.par
nudel o_220sl.inf
NuShellX < o_220.modelx > o_220mod.out
NuShellX < o_220.levelx > o_220lev.out
nucp nul > opd.dat
source shellx.bat > o_220.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  bb0600.lph o_220060.eng o_220.modelx o_220.levelx bb0600.lpe > nucp.txt
nuren o_220060.lp bb0600.lp
nuren o_220060.ls bb0600.ls
nuren o_220060.nhw bb0600.nhw
nucp  bb0602.lph o_220160.eng o_220.modelx o_220.levelx bb0602.lpe > nucp.txt
nuren o_220160.lp bb0602.lp
nuren o_220160.ls bb0602.ls
nuren o_220160.nhw bb0602.nhw
nucp  bb0604.lph o_220260.eng o_220.modelx o_220.levelx bb0604.lpe > nucp.txt
nuren o_220260.lp bb0604.lp
nuren o_220260.ls bb0604.ls
nuren o_220260.nhw bb0604.nhw
nucp  bb0606.lph o_220360.eng o_220.modelx o_220.levelx bb0606.lpe > nucp.txt
nuren o_220360.lp bb0606.lp
nuren o_220360.ls bb0606.ls
nuren o_220360.nhw bb0606.nhw
nucp  bb0608.lph o_220460.eng o_220.modelx o_220.levelx bb0608.lpe > nucp.txt
nuren o_220460.lp bb0608.lp
nuren o_220460.ls bb0608.ls
nuren o_220460.nhw bb0608.nhw
nucp  bb060a.lph o_220560.eng o_220.modelx o_220.levelx bb060a.lpe > nucp.txt
nuren o_220560.lp bb060a.lp
nuren o_220560.ls bb060a.ls
nuren o_220560.nhw bb060a.nhw
nucp  bb060c.lph o_220660.eng o_220.modelx o_220.levelx bb060c.lpe > nucp.txt
nuren o_220660.lp bb060c.lp
nuren o_220660.ls bb060c.ls
nuren o_220660.nhw bb060c.nhw
nucp  bb060e.lph o_220760.eng o_220.modelx o_220.levelx bb060e.lpe > nucp.txt
nuren o_220760.lp bb060e.lp
nuren o_220760.ls bb060e.ls
nuren o_220760.nhw bb060e.nhw
nulev o_22b     
levp o_22b     
