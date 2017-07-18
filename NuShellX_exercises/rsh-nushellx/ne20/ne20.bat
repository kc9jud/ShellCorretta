nucpe /Users/tdisbrow2/Documents/nushellx/sps/sd.sp          sd.sp        
nucpe /Users/tdisbrow2/Documents/nushellx/sps/w.int          w.int        
         
nudel ne200022.trl
nudel ne200022.lnz
nudel ne200022.tmp
nudel ne200022.lev
nudel ne200122.trl
nudel ne200122.lnz
nudel ne200122.tmp
nudel ne200122.lev
nudel ne200222.trl
nudel ne200222.lnz
nudel ne200222.tmp
nudel ne200222.lev
nudel ne200322.trl
nudel ne200322.lnz
nudel ne200322.tmp
nudel ne200322.lev
nudel ne200422.trl
nudel ne200422.lnz
nudel ne200422.tmp
nudel ne200422.lev
nudel ne200522.trl
nudel ne200522.lnz
nudel ne200522.tmp
nudel ne200522.lev
nudel ne200622.trl
nudel ne200622.lnz
nudel ne200622.tmp
nudel ne200622.lev
nudel ne200722.trl
nudel ne200722.lnz
nudel ne200722.tmp
nudel ne200722.lev
nudel ne200822.trl
nudel ne200822.lnz
nudel ne200822.tmp
nudel ne200822.lev
         
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
nucp  bw2402.lph ne200122.eng ne200.modelx ne200.levelx bw2402.lpe > nucp.txt
nuren ne200122.lp bw2402.lp
nuren ne200122.ls bw2402.ls
nuren ne200122.nhw bw2402.nhw
nucp  bw2404.lph ne200222.eng ne200.modelx ne200.levelx bw2404.lpe > nucp.txt
nuren ne200222.lp bw2404.lp
nuren ne200222.ls bw2404.ls
nuren ne200222.nhw bw2404.nhw
nucp  bw2406.lph ne200322.eng ne200.modelx ne200.levelx bw2406.lpe > nucp.txt
nuren ne200322.lp bw2406.lp
nuren ne200322.ls bw2406.ls
nuren ne200322.nhw bw2406.nhw
nucp  bw2408.lph ne200422.eng ne200.modelx ne200.levelx bw2408.lpe > nucp.txt
nuren ne200422.lp bw2408.lp
nuren ne200422.ls bw2408.ls
nuren ne200422.nhw bw2408.nhw
nucp  bw240a.lph ne200522.eng ne200.modelx ne200.levelx bw240a.lpe > nucp.txt
nuren ne200522.lp bw240a.lp
nuren ne200522.ls bw240a.ls
nuren ne200522.nhw bw240a.nhw
nucp  bw240c.lph ne200622.eng ne200.modelx ne200.levelx bw240c.lpe > nucp.txt
nuren ne200622.lp bw240c.lp
nuren ne200622.ls bw240c.ls
nuren ne200622.nhw bw240c.nhw
nucp  bw240e.lph ne200722.eng ne200.modelx ne200.levelx bw240e.lpe > nucp.txt
nuren ne200722.lp bw240e.lp
nuren ne200722.ls bw240e.ls
nuren ne200722.nhw bw240e.nhw
nucp  bw240g.lph ne200822.eng ne200.modelx ne200.levelx bw240g.lpe > nucp.txt
nuren ne200822.lp bw240g.lp
nuren ne200822.ls bw240g.ls
nuren ne200822.nhw bw240g.nhw
nulev ne20w     
levp ne20w     
