
import streamlit as st
from db import create_table, insert_student, get_student_marks

st.set_page_config(page_title="Student Marks Portal", layout="centered")
st.title("🎓 Student Mark Entry & Result Viewer")

menu = st.sidebar.selectbox("Choose Role", ["Teacher", "Student"])

if menu == "Teacher":
    st.header("👩‍🏫 Teacher Login")

    teacher_password = st.text_input("Enter Teacher Password", type="password")
    correct_password = "Ganesh123"  

    if teacher_password != correct_password:
        st.warning("🔐 Enter a valid teacher password to proceed.")
        st.stop()
    else:
        st.success("✅ Access granted to Teacher Panel")


    if st.checkbox("Create New Table"):
        table_name = st.text_input("Enter Table Name (no spaces)")
        num_subjects = st.number_input("Number of Subject Columns", min_value=1, max_value=10, step=1)

        columns = []
        for i in range(int(num_subjects)):
            st.markdown(f"#### Column {i + 1}")
            col1, col2 = st.columns([2, 2])
            with col1:
                col_name = st.text_input("Subject Name", key=f"col_name_{i}")
            with col2:
                data_type = st.selectbox("Data Type", ["INT", "VARCHAR(100)"], key=f"data_type_{i}")

            col3, col4 = st.columns(2)
            with col3:
                is_primary = st.checkbox("Primary Key?", key=f"pk_{i}")
            with col4:
                is_foreign = st.checkbox("Foreign Key?", key=f"fk_{i}")  # Not used now

            if col_name:
                columns.append({
                    "name": col_name,
                    "type": data_type,
                    "primary": is_primary,
                    "foreign": is_foreign
                })

        if table_name and st.button("Create Table"):
            create_table(table_name, columns)
            st.success(f"✅ Table '{table_name}' created successfully!")

    st.subheader("➕ Add Student Marks")

    table = st.text_input("Table Name to Insert Data")
    regd_no = st.text_input("Regd Number")
    name = st.text_input("Student Name")
    subject_list = st.text_area("Enter Subject Columns (comma-separated)")
    marks_list = st.text_area("Enter Marks (comma-separated)")

    if st.button("Submit Marks"):
        try:
            subjects = [s.strip() for s in subject_list.split(',')]
            marks = [int(m.strip()) for m in marks_list.split(',')]
            if len(subjects) != len(marks):
                st.error("❌ Subject and marks count must match!")
            else:
                mark_dict = dict(zip(subjects, marks))
                insert_student(table, regd_no, name, mark_dict)
                st.success("✅ Student data inserted successfully!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

elif menu == "Student":
    st.header("👨‍🎓 Student Panel")

    table = st.text_input("Enter Table Name")
    regd_no = st.text_input("Enter your Regd Number")

    if st.button("Check Result"):
        data = get_student_marks(table, regd_no)
        if data:
            st.subheader(f"🎯 Result for {data['student_name']}")

            # Extract and calculate
            regd_no = data.pop("regd_no")
            student_name = data.pop("student_name")

            subject_marks = {k: v for k, v in data.items() if isinstance(v, int)}

            total_obtained = sum(subject_marks.values())
            total_subjects = len(subject_marks)
            full_marks = total_subjects * 100
            percentage = (total_obtained / full_marks) * 100
            result = "Pass" if percentage >= 30 else "Fail"

            # Show marks in table
            st.markdown("### 📋 Marks Table")
            st.table({ "Subject": list(subject_marks.keys()), "Marks": list(subject_marks.values()) })

            # Show summary
            st.markdown("### 📊 Summary")
            st.write(f"**Total Marks:** {total_obtained} / {full_marks}")
            st.write(f"**Percentage:** {percentage:.2f}%")
            st.write(f"**Result:** {'✅ Pass' if result == 'Pass' else '❌ Fail'}")

        else:
            st.warning("⚠️ No data found")
