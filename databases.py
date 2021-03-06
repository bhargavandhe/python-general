import sqlite3


class Database:
    def __init__(self, file, name):
        self.conn = sqlite3.connect(file)
        self.cursor = self.conn.cursor()
        self.name = name

    def create_table(self):
        cmd = f'''CREATE TABLE IF NOT EXISTS {self.name}(
                    RollNo INTEGER,
                    Name TEXT
                )'''
        self.cursor.execute(cmd)

    def add_data(self, data):
        cmd = f'''INSERT INTO {self.name} (RollNo, Name) VALUES (?, ?)'''
        self.cursor.execute(cmd, data)
        return self.cursor.lastrowid

    def fetch_data(self, param):
        cmd = f'''SELECT {param} FROM {self.name}'''
        self.cursor.execute(cmd)

        fetched_data = self.cursor.fetchall()
        lst = []
        for data in fetched_data:
            for x in data:
                lst.append(x)

        return lst

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()


def main():
    database = Database('database.db', 'SECLASS')
    print("Successfully connected to Database.....")
    database.create_table()
    print(f"Successfully created table {database.name} in database.....")

    print("\nStart adding data to database >")
    entries = int(input('Enter no. of entries: '))

    for entry in range(entries):
        roll_no = int(input('Enter Roll No.: '))
        name = input('Enter name: ')

        if name not in database.fetch_data('Name'):
            data = (roll_no, name)
            database.add_data(data)
            print('Successfully added to database\n')
        else:
            print('Name is already present in database!')

    database.commit_and_close()


if __name__ == '__main__':
    main()
