import streamlit as st
import pandas as pd
import numpy as np

# Load data
@st.cache
def load_data():
    students_df = pd.read_csv('students.csv')
    academic_df = pd.read_csv('academic_performance.csv')
    faculty_df = pd.read_csv('faculty.csv')
    return students_df, academic_df, faculty_df

students_df, academic_df, faculty_df = load_data()

# Set page config
st.set_page_config(
    page_title="Dashboard Universitas",
    page_icon="🎓",
    layout="wide"
)

# Title
st.title("🎓 Dashboard Analitik Universitas")
st.markdown("---")

# Sidebar for filters
st.sidebar.header("Filter Data")

# Filter by year
year_range = st.sidebar.slider(
    'Pilih Rentang Tahun',
    int(students_df['year_enrolled'].min()),
    int(students_df['year_enrolled'].max()),
    (int(students_df['year_enrolled'].min()), int(students_df['year_enrolled'].max()))
)

# Filter by faculty
faculties = sorted(students_df['faculty'].unique())
selected_faculties = st.sidebar.multiselect(
    'Pilih Fakultas',
    faculties,
    default=faculties
)

# Filter by gender
genders = sorted(students_df['gender'].unique())
selected_gender = st.sidebar.selectbox(
    'Pilih Jenis Kelamin',
    ['Semua Jenis Kelamin'] + genders,
    index=0
)

# Apply filters
# For faculty, use the multiselect directly
if selected_faculties:
    faculty_filter = students_df['faculty'].isin(selected_faculties)
else:
    faculty_filter = students_df['faculty'].isin(faculties)  # If nothing selected, show all

# Handle the case when 'Semua Jenis Kelamin' is selected
if selected_gender == 'Semua Jenis Kelamin':
    gender_filter = students_df['gender'].isin(genders)
else:
    gender_filter = students_df['gender'] == selected_gender

filtered_students = students_df[
    (students_df['year_enrolled'] >= year_range[0]) &
    (students_df['year_enrolled'] <= year_range[1]) &
    faculty_filter &
    gender_filter
]

# Main content
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Total Mahasiswa")
    st.metric(label="Jumlah Mahasiswa", value=len(filtered_students), delta=len(filtered_students)-len(students_df))

with col2:
    st.subheader("IPK Rata-rata")
    avg_gpa = filtered_students['gpa'].mean()
    st.metric(label="IPK Rata-rata", value=f"{avg_gpa:.2f}", delta=0.05)

with col3:
    st.subheader("Fakultas Terdaftar")
    unique_faculties = len(filtered_students['faculty'].unique())
    st.metric(label="Jumlah Fakultas", value=unique_faculties, delta=0)

# Charts using Streamlit's built-in chart functions
st.markdown("---")
st.subheader("Distribusi Mahasiswa per Fakultas")

# Bar chart: Distribution of students by faculty
faculty_counts = filtered_students['faculty'].value_counts()
st.bar_chart(faculty_counts)

st.subheader("Tren Jumlah Mahasiswa per Tahun")

# Group by year and count students
yearly_counts = filtered_students.groupby('year_enrolled').size().reset_index(name='count')
yearly_chart = pd.DataFrame(yearly_counts.set_index('year_enrolled')['count'])
st.line_chart(yearly_chart)

# Show raw data
st.markdown("---")
st.subheader("Data Mahasiswa Terfilter")
st.dataframe(filtered_students)

# Additional metrics
st.markdown("---")
st.subheader("Statistik Tambahan")

col1, col2 = st.columns(2)

with col1:
    import matplotlib.pyplot as plt
    
    st.write("**Distribusi Berdasarkan Status**")
    status_counts = filtered_students['status'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.pyplot(fig)

import matplotlib.pyplot as plt

# Create a pie chart for IPK distribution categories
st.write("**Distribusi IPK Mahasiswa**")
# Categorize GPA into ranges
gpa_ranges = pd.cut(filtered_students['gpa'], bins=[0, 2.0, 2.75, 3.5, 4.0], labels=['Kurang (0-2.0)', 'Cukup (2.01-2.75)', 'Baik (2.76-3.5)', 'Sangat Baik (3.51-4.0)'])
gpa_range_counts = gpa_ranges.value_counts()

fig, ax = plt.subplots(figsize=(3, 3))
# Place labels inside the pie chart with both percentage and count
def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f'{pct:.1f}%\n({val})'
    return my_autopct

# Place labels inside the pie chart and make them smaller
wedges, texts, autotexts = ax.pie(gpa_range_counts.values, labels=gpa_range_counts.index, autopct=make_autopct(gpa_range_counts.values), startangle=90, textprops={'fontsize': 5})
ax.axis('equal')

st.pyplot(fig)

# Footer
st.markdown("---")
st.caption("Dashboard Analitik Universitas v1.0 | Dibuat dengan ❤️ menggunakan Streamlit")