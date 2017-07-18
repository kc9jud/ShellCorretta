nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/w.int          w.int        
         
nudel ne200022.trl
nudel ne200022.lnz
nudel ne200022.tmp
nudel ne200022.lev
nudel ne200222.trl
nudel ne200222.lnz
nudel ne200222.tmp
nudel ne200222.lev
         
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
nucp  bw2404.lph ne200222.eng ne200.modelx ne200.levelx bw2404.lpe > nucp.txt
nuren ne200222.lp bw2404.lp
nuren ne200222.ls bw2404.ls
nuren ne200222.nhw bw2404.nhw
nulev ne20w     
levp ne20w     

NuShellX < transt.ne2000004 > transtne2000004.tcpu
source shellx.bat > trans.cpu
nucp bw2400_2404.txi ne200x022222.din ne200y022222.din bw2400_2404.trz > nucp1.txt
nulsf  sdpn.sp       bw2400.lpe    bw2404.lpe    bw2400_2404.trz bw2400_2404.obd bw2400_2404.lsa ne200.occ       > nulsf.dao

NuShellX < transt.ne2000044 > transtne2000044.tcpu
source shellx.bat > trans.cpu
nucp bw2404_2404.txi ne200x222222.din ne200y222222.din bw2404_2404.trz > nucp1.txt
nulsf  sdpn.sp       bw2404.lpe    bw2404.lpe    bw2404_2404.trz bw2404_2404.obd bw2404_2404.lsa ne200.occ       > nulsf.dao

dens < ne200w.den   
gamma ne200w
map ne200w.dei
