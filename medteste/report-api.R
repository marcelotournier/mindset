setwd("~/mindset/medteste")
pr <- plumber::plumb("mindset.R")
pr$run(port=7234)