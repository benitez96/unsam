from sklearn.datasets import load_iris
iris_dataset = load_iris()

import pandas as pd
# creamos un dataframe de los datos de flores
# etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)
# y hacemos una matriz de gráficos de dispersión, asignando colores según la especie
#pd.plotting.scatter_matrix(iris_dataframe, c = iris_dataset['target'], figsize = (15, 15), marker = 'o', hist_kwds = {'bins': 20}, s = 60, alpha = 0.8)

df_targets = pd.DataFrame(iris_dataset['target'], columns=['target'])

frames = [df_targets, iris_dataframe]

new_iris_df = pd.concat(frames, axis = 1)
import seaborn as sns

sns.pairplot(new_iris_df, hue='target')