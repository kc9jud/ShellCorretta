nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/w.int          w.int        
         
nudel ne200022.trl
nudel ne200022.lnz
nudel ne200022.tmp
nudel ne200022.lev
         
nuaddint ne200bw.addint ne200.int ne200.ant
nucp  ne200.ppar p.par
nucp  ne200.npar n.par

nudel ne200sl.inf
NuShellX < ne200.modelx > ne200mod.out
NuShellX < ne200.levelx > ne200lev.out
source shellx.bat > ne200.cpu
nuren shellx.bat shellx1.bat
nucp  bw2400.lph ne200022.eng ne200.modelx ne200.levelx bw2400.lpe > nucp.txt
nuren ne200022.lp bw2400.lp
nuren ne200022.ls bw2400.ls
nuren ne200022.nhw bw2400.nhw
nulev ne20w     
levp ne20w     
         
nudel f_190021.trl
nudel f_190021.lnz
nudel f_190021.tmp
nudel f_190021.lev
         
nuaddint f_190bw.addint f_190.int f_190.ant
nucp  f_190.ppar p.par
nucp  f_190.npar n.par

nudel f_190sl.inf
NuShellX < f_190.modelx > f_190mod.out
NuShellX < f_190.levelx > f_190lev.out
source shellx.bat > f_190.cpu
nuren shellx.bat shellx1.bat
nucp  bw1301.lph f_190021.eng f_190.modelx f_190.levelx bw1301.lpe > nucp.txt
nuren f_190021.lp bw1301.lp
nuren f_190021.ls bw1301.ls
nuren f_190021.nhw bw1301.nhw
nulev f_19w     
levp f_19w     

NuShellX < trans1.f_1900010 > trans1f_1900010.tcpu
source shellx.bat > trans.cpu
nucp bw1301_2400.txi f_190021022.din bw1301_2400.trz > nucp.txt
nulsf  sdpn.sp       bw1301.lpe    bw2400.lpe    bw1301_2400.trz bw1301_2400.lsf bw1301_2400.lsa f_190.occ       > nulsf.dao
nuaddlsf  ne20sw   
