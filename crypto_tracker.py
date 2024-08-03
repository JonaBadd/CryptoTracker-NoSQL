from pymongo import MongoClient
from datetime import datetime
import requests

# Conectar a la base de datos
client = MongoClient("MONGODB_URI_AQUI")
db = client.crypto_tracker

# Función para agregar una nueva criptomoneda
def add_cryptocurrency(symbol, name, description):
    crypto = {
        "symbol": symbol,
        "name": name,
        "description": description
    }
    db.cryptocurrencies.insert_one(crypto)
    print(f"Criptomoneda {name} agregada con éxito.")

# Función para obtener el precio desde Binance
def fetch_price_from_binance(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT" #API GRATUITA DE BINANCE
    response = requests.get(url)
    data = response.json()
    return float(data["price"]) if "price" in data else None

# Función para actualizar el precio
def update_price(symbol):
    price = fetch_price_from_binance(symbol)
    if price is not None:
        price_data = {
            "symbol": symbol,
            "price": price,
            "timestamp": datetime.utcnow()
        }
        db.price_history.insert_one(price_data)
        print(f"Precio de {symbol} actualizado a {price}.")
    else:
        print(f"No se pudo obtener el precio para {symbol}.")

# Función para obtener el precio más reciente
def get_latest_price(symbol):
    latest_price = db.price_history.find_one(
        {"symbol": symbol},
        sort=[("timestamp", -1)]
    )
    if latest_price:
        return latest_price["price"]
    return None

# Ejemplo de uso
add_cryptocurrency("ETH", "Ethereum", "Una plataforma de contratos inteligentes.")
update_price("ETH")
latest_price = get_latest_price("ETH")
print(f"El precio más reciente de ETH es: {latest_price}")

add_cryptocurrency("BTC", "Bitcoin", "Bitcoin")
update_price("BTC")
latest_price = get_latest_price("BTC")
print(f"El precio más reciente de BTC es: {latest_price}")

add_cryptocurrency("NOT", "Notcoin", "Notcoin coin de la plataforma Telegram")
update_price("NOT")
latest_price = get_latest_price("NOT")
print(f"El precio más reciente de NOT es: {latest_price}")
