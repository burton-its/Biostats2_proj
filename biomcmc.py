import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import pymc3 as pm
import arviz as az



alldata2 = pd.read_csv("alldata3.csv")

x = alldata2["pip"]
y = alldata2["rm"]




# with Model() as model:

        
#     sigma = pm.HalfCauchy('sigma', beta=10, testval=1.)
#     intercept = pm.Normal('Intercept', 0, sd=20)
#     x_coeff = pm.Normal('x', 0, sd=20)

#     # Define likelihood
#     likelihood = pm.Normal('y', mu=intercept + x_coeff * alldata2['pip'],
#                         sd=sigma, observed=alldata2['rm'])

# with pm.Model() as model:
    
# 	pm.glm.GLM.from_formula("y ~ x", alldata2)
# 	linear_trace = pm.sample(500, cores = 1)
with pm.Model() as model_robust:
    family = pm.glm.families.StudentT()
    pm.glm.GLM.from_formula("y ~ x", alldata2, family=family)
    trace_robust = pm.sample(250, cores=1)   

with model_robust:
	ppc = pm.sample_posterior_predictive(
		trace_robust)

az.plot_ppc(az.from_pymc3(posterior_predictive=ppc, model=model_robust))
plt.show()

# plt.figure(figsize=(7,5))
# plt.plot(x, y, "o", label = "data")
# pm.plot_posterior_predictive_glm(trace_robust, label = "posterior")
# plt.xlabel("pi")
# plt.ylabel("rm")
# plt.xlim(0,0.02)
# plt.ylim(0,5)
# plt.show()