import psycopg2

conn = psycopg2.connect(
    host="jobtracker.cvoguqiialth.ap-south-1.rds.amazonaws.com",
    database="jobtracker",
    user="postgres",
    password="Ananyasharma",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    company TEXT,
    role TEXT,
    status TEXT
);
""")

conn.commit()
print("Table created!")

cur.close()
conn.close()