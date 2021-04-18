library(mgcv)


in1 = read.table("alldata3.csv", h = T, sep = ",")

hist(in1$rm)

# gam0 = gam(rm ~ s(hm, k = 5), data = in1, method = "REML")
# gam1 = gam(rm ~ s(hm, k = 10), data = in1, method = "REML")
# gam2 = gam(rm ~ s(hm, k = 15), data = in1, method = "REML")

# glm0 = glm(in1$rm ~ poly(in1$hm, degree = 2, raw = T), family = gaussian())
# glm1 = glm(in1$rm ~ poly(in1$hm, degree = 5, raw = T), family = gaussian())
# glm2 = glm(in1$rm ~ poly(in1$hm, degree = 7, raw = T), family = gaussian())


# plot(x = in1$hm, 
# 	y = in1$rm,
# 	)
# lines(in1$hm, glm0$fitted.values,lwd = 3, col = "grey80",lty = 2)
# lines(in1$hm, glm1$fitted.values,lwd = 3, col = "orange",lty = 2)
# lines(in1$hm, glm2$fitted.values,lwd = 3, col = "red",lty = 2)

# par(mfrow= c(2,2))
# plot(glm2)