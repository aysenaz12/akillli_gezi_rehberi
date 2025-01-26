import sqlite3

# Veritabanı bağlantısını oluştur
connection = sqlite3.connect("gezi_rehberi.db")
cursor = connection.cursor()

# Kullanıcı tablosunu oluşturma sorgusu
create_table_query = """
CREATE TABLE IF NOT EXISTS kullanicilar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    soyad TEXT NOT NULL,
    uyelik_tarihi TEXT NOT NULL
);
"""

cursor.execute(create_table_query)

# Örnek kullanıcı kayıtları ekleme
insert_query = """
INSERT INTO kullanicilar (ad, soyad, uyelik_tarihi)
VALUES (?, ?, ?)
"""

kullanicilar = [
    ("Ahmet", "Yılmaz", "2025-01-01"),
    ("Ayşe", "Demir", "2025-01-10"),
    ("Mehmet", "Kara", "2025-01-15")
]

cursor.executemany(insert_query, kullanicilar)

# Değişiklikleri kaydet ve bağlantıyı kapat
connection.commit()
connection.close()

print("Tablo oluşturuldu ve örnek kayıtlar eklendi!")
