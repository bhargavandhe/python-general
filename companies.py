import sqlite3

companies = ['apple', 'samsung', 'google', 'blackberry', 'realme', 'huawei']


def create_table(conn, company_name):
    # CREATE A TABLE, IF NOT EXISTS, MAKE NEW ONE
    cursor = conn.cursor()
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {company_name}(
                        ID TEXT,
                        NAME TEXT,
                        POST TEXT,
                        SALARY TEXT,
                        GENDER CHAR,
                        PHONE TEXT,
                        EMAIL TEXT
                    )''')
    conn.commit()


def add_employee(conn, company_name):
    id_no = input('Enter ID: ')
    name = input('Enter name: ')
    post = input('Enter your post: ')
    salary = input('Enter salary: ')
    gender = input('Gender (M/F)? ')[0]
    phone = input('Phone-no: ')
    email = input('Enter email-id: ')
    data = (id_no, name, post, salary, gender, phone, email)

    create_table(conn, company_name)
    cursor = conn.cursor()
    # ADDING DATA TO DATABASE
    cursor.execute(
        f'INSERT INTO {company_name} (ID, NAME, POST, SALARY, GENDER, PHONE, EMAIL) VALUES (?, ?, ?, ?, ?, ?, ?)', data)
    conn.commit()
    print('Successfully added!')


def show_all_employees(conn, company_name):
    create_table(conn, company_name)
    cursor = conn.cursor()
    cursor.execute(f'SELECT * FROM {company_name}')

    fetched_data = cursor.fetchall()
    print(f'Showing all users of {company_name}')
    for data in fetched_data:
        print('ID, Name, Post, Salary, Gender, Phone, Email')
        print(
            f'{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}')


def delete_employee(conn, company_name):
    create_table(conn, company_name)
    id_no = input('Enter ID no of employee to be deleted: ')

    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM {company_name} WHERE ID="{id_no}"')
    conn.commit()
    print('Succesfully deleted!')


def company(company_name):
    conn = sqlite3.connect('companies.db')
    while (True):
        print(f'Welcome to databse of {company_name}')
        print('1. To add employee')
        print('2. To show details of an employee')
        print('3. To delete employee')
        print('4. For Previous menu')
        print('5. Exit')
        choice = input('Input choice: ')
        if choice == '1':
            add_employee(conn, company_name)
        elif choice == '2':
            show_all_employees(conn, company_name)
        elif choice == '3':
            delete_employee(conn, company_name)
        elif choice == '4':
            main()
            break
        elif choice == '5':
            exit(0)
        else:
            print('Invalid choice!')


def main():
    print('Available companies: ')
    for company_ in companies:
        print(company_.title(), end=', ')

    ch = input('\nEnter a company: ')
    if ch.lower() in companies:
        company(ch.lower())
    else:
        print('No such company found!')


if __name__ == "__main__":
    main()
