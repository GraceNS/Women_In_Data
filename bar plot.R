library(ggplot2)

data <- data.frame(
  name=c("A", "B", "C", "D", "E"),
  value=c(5,2,7,2,3)
)

ggplot(data, aes(x=name, y=value)) +
  geom_bar(stat = "identity" ) 

