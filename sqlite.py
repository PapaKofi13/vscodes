import sqlite3
from employee import Employee


conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""
            CREATE TABLE employees(
            first text,
            last  text,
            pay   integer)
            """)


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (?,?,?)", (emp.first, emp.last, emp.pay))


def get_empl_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""
                UPDATE employee SET pay = :pay
                WHERE first =:first AND last =:last""",
                {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("""
                DELETE FROM employee
                WHERE first =:first AND last =:last""",
                {'first': emp.first, 'last': emp.last})


def get_all_employees():
    with conn:
        c.execute("SELECT * FROM employees")
        print(c.fetchall())


Amerley = Employee('Naa', 'Amerley', 590000)
Mike = Employee('Mikey', 'Kay', 457000)
Kwame = Employee('Kwame', 'Kesse', 440000)
Kay = Employee ('Kay','Kwame',75578)

insert_emp(Amerley)
insert_emp(Mike)
insert_emp(Kwame)
insert_emp(Kay)

new_emp = get_empl_by_name('Amerley')
new_emp2 = get_empl_by_name('Kay')




get_all_employees()



conn.close()
