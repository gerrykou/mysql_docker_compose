import pymysql
import csv
import configparser
import logging

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
hostname = parser.get("mysql_config", "hostname")
port = parser.get("mysql_config", "port")
username = parser.get("mysql_config", "username")
dbname = parser.get("mysql_config", "database")
password = parser.get("mysql_config", "password")


def connect():
    'Connect to mysql database, return connection object'
    try:
        conn = pymysql.connect(host=hostname,
                user=username,
                password=password,
                db=dbname,
                port=int(port))
        logging.info("MySQL connection established!")
        return conn
    except Exception as e:
        logging.error("Error connecting to the MySQL database")


def main():
    m_query = "SELECT * FROM employees;"
    local_filename = "employees_extract.csv"

    conn = connect()
    m_cursor = conn.cursor()
    m_cursor.execute(m_query)
    results = m_cursor.fetchall()

    with open(local_filename, 'w') as f:
        csv_w = csv.writer(f)
        csv_w.writerows(results)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
