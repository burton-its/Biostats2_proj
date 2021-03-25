library("ggplot2")
library("nlme")
library("ggpubr")
library(mgcv)

i1 = read.table("285nr0_wi.csv", h = F, sep = ",")
i2 = read.table("285nr1_wi.csv", h = F, sep = ",")
i3 = read.table("285nr2_wi.csv", h = F, sep = ",")
pdf("outlierspi.pdf")

colnames(i1) = c("rm","hm","pip")
colnames(i2) = c("rm","hm","pip")
colnames(i3) = c("rm","hm","pip")


# strains0 = c("B935", "B2247", "B4142", "B1908", "B2249", "B2302", "B75", "B3926", "B1489", "B279", "B1572", "B3866", "B4498", "B1776", "B345")




comb1 = rbind(i1,i2)
comb2 = rbind(comb1,i3)

# par(mfrow=c(3,1))
# hist(i1$pip, col = "blue")
# hist(i2$pip, col = "green")
# hist(i3$pip, col = "red")

# box1hm = boxplot(i1$rm,i2$rm,i3$rm)
# boxplot(i1$rm,i2$rm,i3$rm)

# table = box1hm$stats
# colnames(table) = box1hm$names
# rownames(table) = c('min','lower quartile','median','upper quartile','max')
# table











# gam0 = gam(rm ~ s(hm, bs = "ds"), data = comb2)
# lm0 = lm(rm ~ hm, data = comb2)

lmtest = lm(pip ~ ., data = comb2)
cooksd = cooks.distance(lmtest)



plot(cooksd, pch = "*", cex = 2)
abline(h = 4*mean(cooksd, na.rm = T), col = "red")
# anova(lm0,gam0, test = "Chisq")
# AIC(lm0)
# AIC(gam0)
# plot.gam(gam0,
#   shade = T,
#   shade.col = "dodgerblue",
#   main = "x=hm, y = rm, model = gam")

# comb2$predicted = predict(linreg1)
# comb2$residuals = residuals(linreg1)


# vm1 = gls(rm ~ hm, data = comb2, weights = varFixed(~hm))

# plot(vm1)


# plot(comb2$hm,
# 	comb2$rm,
# 	col = "dodgerblue",
# 	pch = 17,
# 	xlab = "homoplasic alleles / non homoplasic",
# 	ylab = "recombination events to mutation events"
# 	)
# abline(vm1)

# legend("bottomright", legend = c("Folder0","Folder1","Folder2"), col = c("dodgerblue","blueviolet","coral3"), pch = 17:19)
# plot(linreg1, which = 2, col = "dodgerblue")










#histogram of residuals to see if model fits data(decently symmetrical)
# hist(linreg1$residuals, col = "white",border = "dodgerblue")


#ggplot (scatterplot of data with a linear regression)
# ggplot(comb2, aes(hm,rm))+
# geom_point() +
# stat_smooth(method = "lm", formula = y~x, col = "dodgerblue3")+
# theme(panel.background = element_rect(fill = "white"),
# axis.line.x=element_line(),
# axis.line.y=element_line())


#ggplot of residuals showing over/under with predicted values
# ggplot(comb2, aes(hm,rm))+
# geom_smooth(method = "lm", se = FALSE, color = "lightgrey")+
# geom_segment(aes(xend = hm, yend = predicted), alpha = .2) +
# geom_point(aes(color = residuals))+
# scale_color_gradient2(low = "blue", mid = "white", high = "red")+
# guides(color = FALSE) +
# geom_point(aes(y = predicted), shape = 1) + 
# theme_bw()

#4 panel showing metrics
# par(mfrow = c(2,2))
# plot(linreg1)


#base R scatter plot of data
# plot(i1$hm,
# 	i1$rm,
# 	col = "dodgerblue",
# 	xlim = c(0,2),
# 	ylim = c(0,4),
# 	pch = 17,
# 	xlab = "homoplasic alleles / non homoplasic",
# 	ylab = "recombination events to mutation events"
# 	)
# points(i2$hm,
# 	i2$rm,
# 	pch = 18,
# 	col = "blueviolet")
# points(i3$hm,
# 	i3$rm,
# 	pch= 19,
# 	col = "coral3")
# legend("bottomright", legend = c("Folder0","Folder1","Folder2"), col = c("dodgerblue","blueviolet","coral3"), pch = 17:19)
# abline(linreg1)
# plot(linreg1, which = 2, col = "dodgerblue")

#summary statistics
# capture.output(summary(linreg1), file = "summarylinreg1.txt")
dev.off()
