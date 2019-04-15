require(knitr)
require(rmarkdown)
library(DBI)

setwd("~/mindset/medteste")
# PARA DEBUG:
#myhash = '80aaweDS'

# puxar dados do database

dbu <<- dbConnect(RSQLite::SQLite(), dbname='~/mindset/formdisc/profiles.sqlite')
tlim <<- dbGetQuery( dbu,paste0("select * from disc where hashkey = '",g$myhash,"'" ) )
#tlim2 <<- dbGetQuery( dbu,paste0("select * from disc" ) )

dbDisconnect(dbu)

inf<<-grepl("^A", tlim)
dom<<-grepl("^B", tlim)
con<<-grepl("^C", tlim)
est<<-grepl("^D", tlim)
perfil <<- c('Dominante','Influente',"Estável","Analítico")
predominancia <<- c(sum(dom, na.rm=T),sum(inf, na.rm=T),sum(est, na.rm=T),sum(con, na.rm=T))
nivel<<-c(predominancia[1]*100/40,predominancia[2]*100/40,predominancia[3]*100/40,predominancia[4]*100/40)
nivel<<-round(nivel,1)


disc<<-data.frame(perfil,predominancia,nivel)
disc$perc = paste(disc$nivel, "%")
disc$label = paste(disc$perfil, disc$perc, sep = "\n")
disc2<<-disc

disc2$perfil = as.numeric(as.character(disc2$perfil))
disc2$perfil[1] = 1
disc2$perfil[2] = 2
disc2$perfil[3] = 3
disc2$perfil[4] = 4

disc_ord <<- disc2[order(-nivel),]
