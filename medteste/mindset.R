# plumber.R

setwd("~/mindset/medteste")

#' Processa e envia o report por email
#' @param myhash User's unique hash
#' @get /mailxpto
function(phash=""){
  
  
  #myhash = '80aaweDS'
  
  phash = gsub(" ","",phash)
  myhash <<- phash
  
  Sweave('report.Rnw', encoding = 'UTF-8',output = paste0(myhash,'.tex'))
  
  system(paste0('xelatex -interaction=batchmode ',myhash,'.tex'))
  
  system(paste0('python sendemail.py ',tlim[3]," ",myhash,'.pdf'))
  
}

