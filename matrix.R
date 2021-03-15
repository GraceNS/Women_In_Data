x<-c(4,7,2,8,3)
y<-c(18,4,1,8,4)
z<-c(6,3,5,8,2)
value<-cbind(x,y,z)
print(value)
matplot(value, type="l")
legend("topright", legend=c("x", "y", "z"), pch=1)

