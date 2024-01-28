import sqlite3

class SQLAgent:
    def __init__(self, name_db):
        self.db = sqlite3.connect(name_db)
        self.create_tables()
        self.create_tables_2()
        self.create_tables_3()
        self.create_tables_4()


    def create_tables(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS LogoCars (        
            id_logo INTEGER PRIMARY KEY,
            name_logo TEXT,
            name_page_a TEXT,
            href_car_a TEXT,
            img_logo_name TEXT
            )
            
        ''')

    def create_tables_2(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS BrandCars (        
            id_car INTEGER PRIMARY KEY,
            car_brand TEXT,
            type_brand TEXT,
            car_price TEXT,
            img_car TEXT,
            main_description TEXT,
            kyzov_type TEXT,
            engine_volume INTEGER,
            engine_power INTEGER,
            torque INTEGER,
            fuel_use TEXT,
            max_speed INTEGER,
            improve_speed TEXT,
            volume_tank INTEGER,
            transmission TEXT,
            drive_type TEXT,
            img_up_car TEXT,
            year INTEGER
            
            )
        ''')

    def create_tables_4(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (        
            id_user INTEGER PRIMARY KEY,
            name_user TEXT,
            sub_name TEXT,
            tel_user TEXT,
            email_user TEXT,
            password_user TEXT
            )
        ''')

    def create_tables_3(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS NewsCards (        
            id_new INTEGER PRIMARY KEY,
            txt_new TEXT,
            date_new TEXT,
            img_new TEXT
            )

        ''')
        self.db.commit()

    def add_brand_car(self, car_brand, type_brand, car_price, img_car, main_description, kyzov_type, engine_volume, engine_power, torque, fuel_use, max_speed, improve_speed, volume_tank, transmission, drive_type, img_up_car, year):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO  BrandCars(car_brand, type_brand, car_price, img_car, main_description, kyzov_type, engine_volume, engine_power, torque, fuel_use, max_speed, improve_speed, volume_tank, transmission, drive_type, img_up_car, year) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [car_brand, type_brand, car_price, img_car, main_description, kyzov_type, engine_volume, engine_power, torque, fuel_use, max_speed, improve_speed, volume_tank, transmission, drive_type, img_up_car, year])
        cursor.close()
        self.db.commit()


    def add_logo(self, name_logo, name_page_a, href_car_a, img_logo_name):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO  LogoCars(name_logo, name_page_a, href_car_a, img_logo_name) VALUES(?, ?, ?, ?)', [name_logo, name_page_a, href_car_a, img_logo_name])
        cursor.close()
        self.db.commit()
    def get_all(self):
        cursor = self.db.cursor()
        query = "SELECT * FROM LogoCars"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result


    def get_all_cars(self):
        cursor = self.db.cursor()
        get_cars = "SELECT * FROM BrandCars"
        cursor.execute(get_cars)
        result2 = cursor.fetchall()
        cursor.close()
        return result2

    def add_new(self, txt_new, date_new, img_new):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO  NewsCards(txt_new, date_new, img_new) VALUES(?, ?, ?)', [txt_new, date_new, img_new])
        cursor.close()
        self.db.commit()
    def get_news(self):
        cursor = self.db.cursor()
        get_news = "SELECT * FROM NewsCards"
        cursor.execute(get_news)
        result3 = cursor.fetchall()
        cursor.close()
        return result3

    def get_filtred_cars(self, year):
        cursor = self.db.cursor()
        query = "SELECT * FROM BrandCars  WHERE year = ?"
        cursor.execute(query, [year])
        result4 = cursor.fetchall()
        cursor.close()
        return result4

    def add_user(self, name_user, sub_user, tel_user, email_user, password_user):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO  Users(name_user, sub_name, tel_user, email_user, password_user) VALUES(?, ?, ?, ?, ?)', [name_user, sub_user, tel_user, email_user, password_user])
        cursor.close()
        self.db.commit()

    def get_correct_user(self, name_user, email_user, password_user):
        cursor = self.db.cursor()
        query = "SELECT * FROM Users  WHERE name_user = ? AND email_user = ? AND password_user = ?"
        cursor.execute(query, [name_user, email_user, password_user])
        result = cursor.fetchone()
        cursor.close()
        if len(result) > 1:
            return result
    def get_uncorrect_user(self, name_user, email_user, password_user):
        cursor = self.db.cursor()
        query = "SELECT * FROM Users  WHERE name_user = ? AND email_user = ? AND password_user = ?"
        cursor.execute(query, [name_user, email_user, password_user])
        result = cursor.fetchone()
        cursor.close()
        if len(result) == None:
            return result

    def get_user_dani(self, name_user, email_user, password_user):
        cursor = self.db.cursor()
        query = "SELECT * FROM Users WHERE name_user = ? AND email_user = ? AND password_user = ?"
        cursor.execute(query, [name_user, email_user, password_user])
        result5 = cursor.fetchone()
        cursor.close()
        return result5

    def get_user_columns(self):
        return ['id_user', 'name_user', 'sub_name', 'tel_user', 'email_user', 'password_user']

