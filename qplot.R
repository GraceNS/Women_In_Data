install.packages("ggplot2", dependencies = TRUE)

library(ggplot2)
importIntoEnv(ggplot2, "qplot")
x<-1:20; y<-x^2
qplot(x, y, geom=c("point", "line"))
