import os
import urllib.parse as up
import psycopg2

up.uses_netloc.append("postgres")
url = up.urlparse(os.environ["DATABASE_URL"])
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)

cur = conn.cursor()
cur.execute("""SELECT * from account1""")
rows = cur.fetchall()
print("\nShow me the databases:\n")
for row in rows:
    print("   ", row[1],row[0])