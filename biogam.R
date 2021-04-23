library(mgcv)
library(ggplot2)


in1 = read.table("alldata3.csv", h = T, sep = ",")
pdf("allmodelsgam_legend1.pdf")


# gam0 = gam(rm ~ s(hm, k = 5), data = in1, method = "REML")
# gam1 = gam(rm ~ s(pip, k = 10), data = in1, method = "REML")
# gam2 = gam(rm ~ s(hm, k = 15), data = in1, method = "REML")

# glm0 = glm(in1$rm ~ poly(in1$hm, degree = 2, raw = T), family = gaussian())
# glm1 = glm(in1$rm ~ poly(in1$hm, degree = 5, raw = T), family = gaussian())
# glm2 = glm(in1$rm ~ poly(in1$hm, degree = 7, raw = T), family = gaussian())


# plot.gam(gam1,
# 	shade = T,
# 	shade.col = "dodgerblue",
# 	main = "x=hm, y = rm, model = gam")

# lines(in1$hm, glm1$fitted.values,lwd = 3, col = "orange",lty = 2)
# lines(in1$hm, glm2$fitted.values,lwd = 3, col = "red",lty = 2)

# par(mfrow= c(2,2))
# plot(glm2)
ggplot(in1, aes(x = pip, y = rm)) +
	geom_point()+
 	stat_smooth(method = "lm", formula = y ~ x, se = FALSE,
    aes(color = "LM")) + 
	stat_smooth(method = "lm", formula = y ~ x + I(x^2), se = FALSE,
    aes(color = "Quad")) + 
	stat_smooth(method = "loess", formula = y ~x, se = FALSE, 
	aes(color = "loess")) + 
	stat_smooth(method = "gam", formula = y ~s(x), se = FALSE,
	aes(color = "gam")) + 
	stat_smooth(method = "gam", formula = y ~ s(x, k = 10), se = FALSE,
	aes(color = "gam10"))+
	scale_color_manual(name = "model", values = c("black", "blue","red","green","violet")) + 
	labs(shape = "")




dev.off()

