import sqlite3

# Veritabanı bağlantısını oluştur
connection = sqlite3.connect("gezi_rehberi.db")
cursor = connection.cursor()

# Request-Response tablosunu oluşturma sorgusu
create_request_response_table_query = """
CREATE TABLE IF NOT EXISTS request_response (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    request TEXT NOT NULL CHECK(LENGTH(request) <= 2000),
    response TEXT NOT NULL CHECK(LENGTH(response) <= 10000),
    duration INTEGER NULL,
    request_date_time TEXT NOT NULL,
    device_id TEXT NULL
);
"""

cursor.execute(create_request_response_table_query)

# Değişiklikleri kaydet ve bağlantıyı kapat
connection.commit()
connection.close()

print("Request-Response tablosu oluşturuldu!")
