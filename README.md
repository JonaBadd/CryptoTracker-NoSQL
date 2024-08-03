# Crypto Tracker
### Descripción

Crypto Tracker es un proyecto en Python que permite realizar un seguimiento y gestionar datos de criptomonedas utilizando MongoDB y la API gratuita de Binance. Este sistema incluye funciones para agregar nuevas criptomonedas a la base de datos, actualizar sus precios en tiempo real, y consultar el precio más reciente registrado. Ideal para desarrolladores que buscan integrar datos de criptomonedas en aplicaciones o proyectos de análisis.
Tecnologías Utilizadas

- MongoDB Atlas y Compass: La base de datos se gestiona a través de MongoDB Atlas y Compass.
- Base de Datos: "crypto_tracker"
- Colecciones:
	- cryptocurrencies: Almacena información sobre las criptomonedas.
	- price_history: Almacena el historial de precios.

### Funcionalidades

- Agregar criptomonedas: Permite añadir nuevas criptomonedas a la base de datos con su símbolo, nombre y descripción.
- Actualizar precios: Obtiene el precio más reciente de una criptomoneda desde la API de Binance y lo actualiza en la base de datos.
- Consultar precios: Recupera el precio más reciente registrado para una criptomoneda específica.

### Instalación

#### Clonar el repositorio:
```bash
git clone https://github.com/tuusuario/crypto-tracker.git
cd crypto-tracker
```

#### Instalar dependencias:
Asegúrate de tener pymongo y requests instalados. Puedes instalarlos utilizando pip:

```bash
pip install pymongo requests
```

### Uso

1.   Conectar a la base de datos:
	Asegúrate de reemplazar la cadena de conexión en el script con la configuración adecuada para tu base de datos MongoDB en Atlas.

4. Agregar una criptomoneda:
	Llama a la función add_cryptocurrency(symbol, name, description) con los detalles de la criptomoneda.

7. Actualizar el precio:
	Usa la función update_price(symbol) para obtener y registrar el precio actual desde Binance.

10. Consultar el precio más reciente:
	Llama a get_latest_price(symbol) para recuperar el precio más reciente registrado.

### Ejemplo

```python
add_cryptocurrency("ETH", "Ethereum", "Una plataforma de contratos inteligentes.")
update_price("ETH")
latest_price = get_latest_price("ETH")
print(f"El precio más reciente de ETH es: {latest_price}")
```

#### Contribuciones

Si tienes sugerencias para mejorar este proyecto, por favor realiza un fork del repositorio y envía un pull request. Agradezco tus aportes y comentarios.

#### Licencia
[MIT](https://choosealicense.com/licenses/mit/)
