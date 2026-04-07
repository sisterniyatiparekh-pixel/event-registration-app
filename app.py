from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# 🔌 Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Niyati@142007",           
        database="college"              )

# 🏠 Home page
@app.route('/')
def home():
    return render_template("index.html")

# 📩 Form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        print("Form Data:", request.form)

        name = request.form['name']
        event = request.form['event']

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO registrations (name, event) VALUES (%s, %s)"
        cursor.execute(query, (name, event))

        conn.commit()
        conn.close()

        return "✅ Data Saved in MySQL!"

    except Exception as e:
        return f"❌ ERROR: {e}"
# ▶️ Run app
if __name__ == '__main__':
    app.run(debug=True)