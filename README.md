# 📚 EduScore-Panel

**EduScore-Panel** is a web-based application built with **Streamlit** and **MySQL** that allows teachers to manage student marks and students to view their results. It's a user-friendly Student Result Management System designed for quick access and smooth performance.

---

## 📁 Project Structure

```
EduScore-Panel/
├── db.py                 # Handles all database operations (create table, insert, fetch)
├── app.py                # Main Streamlit app file
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🎯 Features

### 👨‍🏫 Teacher Panel

- **Secure access** with a password (`Ganesh123` by default).
- **Create new result tables** dynamically:
  - After entering a table name, you select the number of subject columns.
  - The system automatically generates input fields for each column.
  - Simply provide the **column/subject name**, choose the **data type**, and optionally mark as a **primary key**.
- **Insert student marks**:
  - Enter the registration number, student name, and marks for each subject.
  - Subject and marks input must match in count and order.


### 👨‍🎓 Student Panel
- Enter table name and registration number to **view marks**.
- Shows:
  - Individual subject scores.
  - Total marks, percentage.
  - Result status: ✅ Pass / ❌ Fail.

---

## 🛠️ Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [MySQL](https://www.mysql.com/)
- **Language**: Python 3

---

## 🖥️ Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/EduScore-Panel.git
   cd EduScore-Panel
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up MySQL**
   - Create a database named `student_db`.
   - Update your MySQL credentials in `db.py`:
     ```python
     mysql.connector.connect(
         host="localhost",
         user="your_username",
         password="your_password",
         database="student_db"
     )
     ```

4. **Run the App**
   ```bash
   streamlit run app.py
   ```

---

## 📝 Example Usage

- **Teacher** logs in with password and creates a table like `class10_math`.
- Adds subjects: `Math`, `Science`, `English`.
- Inserts student records with marks.
- **Student** enters `class10_math` and their `regd_no` to check result.

---

## 📌 Notes

- Default teacher password is **Ganesh123**.
- Registration number (`regd_no`) is always used as a primary identifier.
- Marks are considered out of 100 per subject.
- Pass threshold is **30%** overall.

---

## 📬 Contact

**Developer**: Ganesh Prasad Sahoo  
📧 [LinkedIn](https://www.linkedin.com/in/ganesh-prasad-sahoo)

---

## 📄 License

This project is open-source and free to use for educational purposes.
