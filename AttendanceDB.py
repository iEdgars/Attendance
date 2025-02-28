import sqlite3

def create_database():
    # Connect to SQLite database (if not exists, it will be created)
    conn = sqlite3.connect('Attendance.db')
    
    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS people (
                        Person TEXT NOT NULL,
                        Org TEXT,
                        Team TEXT,
                        City TEXT,
                        Country TEXT,
                        Timezone TEXT,
                        Role TEXT,
                        Title TEXT,
                        Start_Date DATE,
                        End_Date DATE
                    )''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()