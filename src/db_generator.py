
import mysql.connector


def fetch_employees(batch_size=1000):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="R!ya2004",
        database="employees",
    )

    cursor = connection.cursor(buffered=False)

    try:
        cursor.execute(
            "SELECT emp_no, first_name, last_name FROM employees"
        )

        while True:
            rows = cursor.fetchmany(batch_size)

            if not rows:
                break

            for row in rows:
                yield row

    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    count = 0

    for employee in fetch_employees():
        count += 1

    print("Total employees processed:", count)
