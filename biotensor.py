import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing



alldata2 = pd.read_csv("alldata3.csv")

# np.set_printoptions(precision = 3, suppress = True)

dataset = alldata2.copy()

train_dataset = dataset.sample(frac = 0.8, random_state = 0)
test_dataset = dataset.drop(train_dataset.index)

# train_dataset.describe().transpose()

train_features = train_dataset.copy()
test_features = test_dataset.copy()

train_labels = train_features.pop("rm")
test_labels = test_features.pop("rm")


normalizer = preprocessing.Normalization()
normalizer.adapt(np.array(train_features))
# print(normalizer.mean.numpy())

first = np.array(train_features[:1])

# with np.printoptions(precision = 2, suppress = True):
# 	print("first example", first)
# 	print()
# 	print("Normalized", normalizer(first).numpy())

# sns.pairplot(train_dataset[["rm","hm","pip"]], diag_kind = "kde")
# plt.savefig("inspect.pdf")



# hm = np.array(train_features["hm"])
# hm_normalizer = preprocessing.Normalization(input_shape = [1,])
# hm_normalizer.adapt(hm)


# linear_model = tf.keras.Sequential([
# 	normalizer,
# 	layers.Dense(units = 1)])

# linear_model.compile(
# 	optimizer = tf.optimizers.Adam(learning_rate = 0.1),
# 	loss = "mean_absolute_error")

# history = linear_model.fit(
# 	train_features,train_labels,
# 	epochs = 100,
# 	verbose = 0,
# 	validation_split = 0.2)

# hm_model = tf.keras.Sequential([
# 	hm_normalizer,
# 	layers.Dense(units = 1)])
# # hm_model.summary()

# # print(hm_model.predict(hm[:10]))

# hm_model.compile(
# 	optimizer = tf.optimizers.Adam(learning_rate = 0.1),
# 	loss = "mean_absolute_error")

# history = hm_model.fit(
# 	train_features["hm"], train_labels,
# 	epochs = 50,
# 	verbose = 0,
# 	validation_split = 0.2)

# test_results = {}

# test_results["hm_model"] = hm_model.evaluate(
# 	test_features["hm"],
# 	test_labels, verbose = 0)

# x = tf.linspace(0.0,4,4)
# y = hm_model.predict(x)


# def plot_hm(x,y):
# 	plt.scatter(train_features["hm"], train_labels, label = "Data")
# 	plt.plot(x,y, color = "k", label = "predictions")
# 	plt.xlabel("hm")
# 	plt.ylabel("rm")
# 	plt.legend()
# 	plt.savefig("regression.pdf")

# plot_hm(x,y)
