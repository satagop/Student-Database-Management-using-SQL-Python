import sqlite3

# Connect to Database
conn = sqlite3.connect("students.db")
cur = conn.cursor()

# Create Table
with open("schema.sql", "r") as f:
    cur.executescript(f.read())

# Insert Data
with open("data.sql", "r") as f:
    cur.executescript(f.read())

print("\n📌 All Students")
cur.execute("SELECT * FROM students")
for row in cur.fetchall():
    print(row)

# Add new student
print("\n➕ Adding a new student...")
cur.execute("INSERT INTO students VALUES (5, 'Manoj', 'CSE', 81, 'manoj@example.com')")
conn.commit()

# Update marks
print("\n✏ Updating marks for student 2...")
cur.execute("UPDATE students SET marks = 82 WHERE student_id = 2")
conn.commit()

# Delete student
print("\n🗑 Deleting student 4...")
cur.execute("DELETE FROM students WHERE student_id = 4")
conn.commit()

# Fetch results after operations
print("\n📌 Updated Students List")
cur.execute("SELECT * FROM students")
for row in cur.fetchall():
    print(row)

conn.close()
print("\n✔ Operations Completed Successfully!")
