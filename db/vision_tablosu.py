import sqlite3

# Veritabanı bağlantısını oluştur
connection = sqlite3.connect("gezi_rehberi.db")
cursor = connection.cursor()

# Vision tablosunu oluşturma sorgusu
create_vision_table_query = """
CREATE TABLE IF NOT EXISTS vision (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vision_link TEXT NULL,
    vision_response TEXT NOT NULL CHECK(LENGTH(vision_response) <= 10000),
    duration INTEGER ,
    upload_date_time TEXT NOT NULL,
    device_id TEXT NULL
);
"""

cursor.execute(create_vision_table_query)

# Değişiklikleri kaydet ve bağlantıyı kapat
connection.commit()
connection.close()

print("Vision tablosu oluşturuldu!")
