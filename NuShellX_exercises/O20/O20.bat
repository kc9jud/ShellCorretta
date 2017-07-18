         
nudel o_200040.trl
nudel o_200040.lnz
nudel o_200040.tmp
nudel o_200040.lev
nudel o_200140.trl
nudel o_200140.lnz
nudel o_200140.tmp
nudel o_200140.lev
nudel o_200240.trl
nudel o_200240.lnz
nudel o_200240.tmp
nudel o_200240.lev
nudel o_200340.trl
nudel o_200340.lnz
nudel o_200340.tmp
nudel o_200340.lev
nudel o_200440.trl
nudel o_200440.lnz
nudel o_200440.tmp
nudel o_200440.lev
nudel o_200540.trl
nudel o_200540.lnz
nudel o_200540.tmp
nudel o_200540.lev
nudel o_200640.trl
nudel o_200640.lnz
nudel o_200640.tmp
nudel o_200640.lev
         
nuaddint o_200bb.addint o_200.int o_200.ant
nucp  o_200.ppar p.par
nucp  o_200.npar n.par
nudel o_200sl.inf
NuShellX < o_200.modelx > o_200mod.out
NuShellX < o_200.levelx > o_200lev.out
nucp nul > opd.dat
source shellx.bat > o_200.cpu
nuren shellx.bat shellx1.bat
nudel opd.dat
nucp  bb0400.lph o_200040.eng o_200.modelx o_200.levelx bb0400.lpe > nucp.txt
nuren o_200040.lp bb0400.lp
nuren o_200040.ls bb0400.ls
nuren o_200040.nhw bb0400.nhw
nucp  bb0402.lph o_200140.eng o_200.modelx o_200.levelx bb0402.lpe > nucp.txt
nuren o_200140.lp bb0402.lp
nuren o_200140.ls bb0402.ls
nuren o_200140.nhw bb0402.nhw
nucp  bb0404.lph o_200240.eng o_200.modelx o_200.levelx bb0404.lpe > nucp.txt
nuren o_200240.lp bb0404.lp
nuren o_200240.ls bb0404.ls
nuren o_200240.nhw bb0404.nhw
nucp  bb0406.lph o_200340.eng o_200.modelx o_200.levelx bb0406.lpe > nucp.txt
nuren o_200340.lp bb0406.lp
nuren o_200340.ls bb0406.ls
nuren o_200340.nhw bb0406.nhw
nucp  bb0408.lph o_200440.eng o_200.modelx o_200.levelx bb0408.lpe > nucp.txt
nuren o_200440.lp bb0408.lp
nuren o_200440.ls bb0408.ls
nuren o_200440.nhw bb0408.nhw
nucp  bb040a.lph o_200540.eng o_200.modelx o_200.levelx bb040a.lpe > nucp.txt
nuren o_200540.lp bb040a.lp
nuren o_200540.ls bb040a.ls
nuren o_200540.nhw bb040a.nhw
nucp  bb040c.lph o_200640.eng o_200.modelx o_200.levelx bb040c.lpe > nucp.txt
nuren o_200640.lp bb040c.lp
nuren o_200640.ls bb040c.ls
nuren o_200640.nhw bb040c.nhw
nulev o_20b     
levp o_20b     
