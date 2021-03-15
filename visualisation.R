msleep

qplot(sleep_total, sleep_rem, data=msleep, color=vore,
      geom=c("point", "smooth"))

qplot(vore, sleep_total, data=msleep, geom="dotplot", stackdir="center",
      binaxis="y", color=vore, fill=vore)
