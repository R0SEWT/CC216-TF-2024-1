import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.regularizers import l2
from sklearn.metrics import mean_squared_error

# Cargar el archivo CSV
df = pd.read_csv('datos_procesados.csv')

# Verificar valores faltantes
print("Valores faltantes en el DataFrame:")
print(df.isnull().sum())

# Inicializar el codificador
label_encoder = LabelEncoder()

df['title'] = label_encoder.fit_transform(df['title'])
df['trending_date'] = label_encoder.fit_transform(df['trending_date'])
df['channel_title'] = label_encoder.fit_transform(df['channel_title'])
df['category_id'] = label_encoder.fit_transform(df['category_id'])
df['publish_time'] = label_encoder.fit_transform(df['publish_time'])
df['thumbnail_link'] = label_encoder.fit_transform(df['thumbnail_link'])
df['tags'] = label_encoder.fit_transform(df['tags'])
df['description'] = label_encoder.fit_transform(df['description'])
df['state'] = label_encoder.fit_transform(df['state'])
df['geometry'] = label_encoder.fit_transform(df['geometry'])
df['comments_disabled'] = label_encoder.fit_transform(df['comments_disabled'])
df['ratings_disabled'] = label_encoder.fit_transform(df['ratings_disabled'])
df['video_error_or_removed'] = label_encoder.fit_transform(df['video_error_or_removed'])

# Definir características (X) y variable objetivo (y)
X = df.drop(columns=['video_id', 'views'])
y = df['views']

# Dividir los datos en conjuntos de entrenamiento y prueba (70% entrenamiento, 30% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inicializar el escalador
scaler = StandardScaler()

# Ajustar el escalador solo en los datos de entrenamiento
X_train_scaled = scaler.fit_transform(X_train)

# Aplicar el escalador en los datos de prueba
X_test_scaled = scaler.transform(X_test)

# ==================DEEP LEARNING====================================
# Crear el modelo de regresión
regression_model = Sequential()
regression_model.add(Dense(128, input_dim=X_train_scaled.shape[1], activation='relu', kernel_regularizer=l2(0.01)))
regression_model.add(Dropout(0.5))
regression_model.add(Dense(64, activation='relu', kernel_regularizer=l2(0.01)))
regression_model.add(Dense(32, activation='relu', kernel_regularizer=l2(0.01)))
regression_model.add(Dense(1, activation='linear'))  # Capa de salida para regresión

# Compilar el modelo
regression_model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001), metrics=['mean_squared_error'])

# Entrenar el modelo
history = regression_model.fit(X_train_scaled, y_train, epochs=150, batch_size=16, validation_split=0.2, verbose=1)

# Evaluar el modelo
mse, mse_accuracy = regression_model.evaluate(X_test_scaled, y_test)
print(f'Regression Test MSE: {mse}')
print(f'Regression Test MSE Accuracy: {mse_accuracy}')

# Guardar el modelo entrenado
regression_model.save('modelo_entrenado_regresion.keras')