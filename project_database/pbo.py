import mysql.connector

class Karyawan:
    def __init__(self, id, nama, jabatan, gaji):
        self.id = id
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

    @staticmethod
    def select_all():
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5220411214')
        cursor = conn.cursor()
        query = "SELECT * FROM karyawan"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        karyawans = []
        for row in result:
            karyawan = Karyawan(row[0], row[1], row[2], row[3])
            karyawans.append(karyawan)
        return karyawans

    def insert(self):
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5220411214')
        cursor = conn.cursor()
        query = "INSERT INTO karyawan (nama, jabatan, gaji) VALUES (%s, %s, %s)"
        data = (self.nama, self.jabatan, self.gaji)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self):
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5220411214')
        cursor = conn.cursor()
        query = "DELETE FROM karyawan WHERE id=%s"
        data = (self.id,)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()

    def update(self):
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='5220411214')
        cursor = conn.cursor()
        query = "UPDATE karyawan SET nama=%s, jabatan=%s, gaji=%s WHERE id=%s"
        data = (self.nama, self.jabatan, self.gaji, self.id)
        cursor.execute(query, data)
        conn.commit()
        cursor.close()
        conn.close()

# Contoh penggunaan
karyawans = Karyawan.select_all()
for karyawan in karyawans:
    print(karyawan.id, karyawan.nama, karyawan.jabatan, karyawan.gaji)

karyawan_baru = Karyawan(0, 'Jofran', 'Software Engineer', 50000)
karyawan_baru.insert()
karyawan_baru = Karyawan(0, 'Anggi', 'Hardware Engineer', 100000)
karyawan_baru.insert()
karyawan_baru = Karyawan(0, 'Jerry', 'Software Engineer', 2000000)
karyawan_baru.insert()
karyawan_baru = Karyawan(0, 'Manusia', 'Hardware Engineer', 2000000)
karyawan_baru.insert()
karyawan_baru = Karyawan(0, 'Sumba', 'Software Engineer', 2000000)
karyawan_baru.insert()
karyawan_baru = Karyawan(0, 'Merry', 'Software Engineer', 2000000)
karyawan_baru.insert()

karyawan_to_delete = Karyawan(0, '', '', '')
karyawan_to_delete.id = 2
karyawan_to_delete.delete()

karyawan_to_update = Karyawan(2, 'Karyawan Diperbarui', 'Senior Software Engineer', 70000)
karyawan_to_update.id = 3
karyawan_to_update.update()