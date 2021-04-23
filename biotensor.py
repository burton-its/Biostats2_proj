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


# normalizer = preprocessing.Normalization()
# normalizer.adapt(np.array(train_features))
# print(normalizer.mean.numpy())

first = np.array(train_features[:1])



# with np.printoptions(precision = 2, suppress = True):
# 	print("first example", first)
# 	print()
# 	print("Normalized", normalizer(first).numpy())

# sns.pairplot(train_dataset[["rm","hm","pip"]], diag_kind = "kde")
# plt.savefig("inspect.pdf")



pip = np.array(train_features["pip"])

# pip_normalizer = preprocessing.Normalization()
# pip_normalizer.adapt(pip)
# normalized_data = pip_normalizer(pip)


# print(pip_normalizer.numpy().std())


pi_model = keras.Sequential([
	layers.Dense(32, activation = "relu"), 
	layers.Dense(1)])

pi_model.compile(loss = "mean_absolute_error",
	optimizer = tf.optimizers.Adam(0.01))




history = pi_model.fit(
	train_features["pip"],train_labels,
	validation_split = 0.2,
	verbose = 0, epochs = 500)



# x = tf.linspace(0.0,10,11)
# y = pi_model.predict(x)

# def plot_pi(x,y):
# 	plt.scatter(train_features["pip"], train_labels, label = "data")
# 	plt.plot(x, y, color = "k", label = "predictions")
# 	plt.xlabel("pi")
# 	plt.ylabel("rm")
# 	# plt.xlim(0,2)
# 	# plt.ylim(0,7)
# 	plt.legend()
# 	plt.show()
# 	# plt.savefig("dnn_pi_model_2.pdf")

# plot_pi(x,y)
# plot_pi(x,y)
# def plot_loss(history):
#   plt.plot(history.history['loss'], label='loss')
#   plt.plot(history.history['val_loss'], label='val_loss')
#   plt.ylim([0, 5])
#   plt.xlabel('Epoch')
#   plt.ylabel('Error [rm]')
#   plt.legend()
#   plt.grid(True)
#   plt.savefig("pi_dnn_test1.pdf")


# pip_model = tf.keras.Sequential([
# 	pip_normalizer,
# 	layers.Dense(units = 1)])




# pip_model.compile(
# 	optimizer = tf.optimizers.Adam(learning_rate = 0.1),
# 	loss = "mean_absolute_error")

# history = pip_model.fit(
# 	train_features["pip"], train_labels,
# 	epochs = 100,
# 	verbose = 0,
# 	validation_split = 0.2)



# test_results = {}

# test_results["pip_model"] = pip_model.evaluate(
# 	test_features["pip"],
# 	test_labels, verbose = 0)



# print(dnn_pi_model.summary())

# test_results["dnn__pi_model"] = dnn_pi_model.evaluate(
# 	test_features["pip"], test_labels, verbose = 0)

# modelcompare = pd.DataFrame(test_results, index = ["Mean absolute error[pi]"]).T







test_predictions = pi_model.predict(test_features["pip"]).flatten()
error = test_predictions - test_labels
plt.hist(error, bins = 25)
plt.xlabel("prediction error for pi")
plt.show()


# plt.scatter(test_labels, test_predictions)
# plt.xlabel("true values rm")
# plt.ylabel("predictions rm")
# plt.show()













