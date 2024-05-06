from flask import Flask,render_template, jsonify
import pymysql
            # from database import engine
            # from sqlalchemy import text
            # import os
app = Flask(__name__)

@app.route('/')
def index():
                
                connection = pymysql.connect(
                    host="localhost",
                    user="root",
                    password="MASTAN",
                    database="cc",
                    charset="utf8mb4",
                    cursorclass=pymysql.cursors.DictCursor  # Use a dictionary cursor
                )

                try:
                    # Create a cursor
                    with connection.cursor() as cursor:
                        # Execute SQL query
                        cursor.execute("SELECT * FROM jobs")
                        # Fetch all rows
                        jobs = cursor.fetchall()
                finally:
                    # Close the connection
                    connection.close()

                return render_template('home.html', jobs=jobs)



if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)