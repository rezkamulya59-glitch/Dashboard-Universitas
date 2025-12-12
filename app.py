import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load data
@st.cache_data
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

# Header
st.title("🎓 Dashboard Analitik Universitas")
st.markdown("---")

# Sidebar for filters
st.sidebar.header("🔍 Filter Data")

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

# KPI Metrics
st.subheader("📊 KPI Utama")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Mahasiswa", 
        value=len(filtered_students),
        delta=len(filtered_students)-len(students_df)+len(filtered_students)
    )

with col2:
    avg_gpa = filtered_students['gpa'].mean()
    st.metric(
        label="IPK Rata-rata", 
        value=f"{avg_gpa:.2f}",
        delta=round(avg_gpa - students_df['gpa'].mean(), 2)
    )

with col3:
    unique_faculties = len(filtered_students['faculty'].unique())
    st.metric(
        label="Jumlah Fakultas", 
        value=unique_faculties,
        delta=0
    )

with col4:
    active_students = len(filtered_students[filtered_students['status'] == 'Active'])
    st.metric(
        label="Mahasiswa Aktif", 
        value=active_students,
        delta=round(active_students * 0.05)  # Simulasi perubahan
    )

# Charts
st.markdown("---")
st.subheader("📈 Visualisasi Data")

# Create two columns for charts
col1, col2 = st.columns(2)

with col1:
    # Bar chart: Distribution of students by faculty
    st.write("**Distribusi Mahasiswa per Fakultas**")
    faculty_counts = filtered_students['faculty'].value_counts()
    fig_bar = px.bar(
        x=faculty_counts.index,
        y=faculty_counts.values,
        labels={'x': 'Fakultas', 'y': 'Jumlah Mahasiswa'},
        color=faculty_counts.index,
        title="Distribusi Mahasiswa per Fakultas"
    )
    fig_bar.update_layout(xaxis_tickangle=-45, height=400)
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    # Line chart: Trend of enrolled students by year
    st.write("**Tren Jumlah Mahasiswa per Tahun**")
    yearly_counts = filtered_students.groupby('year_enrolled').size().reset_index(name='count')
    fig_line = px.line(
        yearly_counts,
        x='year_enrolled',
        y='count',
        markers=True,
        title="Tren Jumlah Mahasiswa Terdaftar per Tahun",
        labels={'year_enrolled': 'Tahun', 'count': 'Jumlah Mahasiswa'}
    )
    fig_line.update_layout(height=400)
    st.plotly_chart(fig_line, use_container_width=True)

# Additional visualizations
st.markdown("---")
st.subheader("🔍 Analisis Lebih Lanjut")

# Create tabs for different analysis views
tab1, tab2, tab3 = st.tabs(["Status Mahasiswa", "IPK per Fakultas", "Distribusi Gender"])

with tab1:
    import matplotlib.pyplot as plt
    
    st.write("Distribusi Status Mahasiswa")
    status_counts = filtered_students['status'].value_counts()
    fig, ax = plt.subplots(figsize=(3, 3))
    # Place labels inside the pie chart with both percentage and count
    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return f'{pct:.1f}%\n({val})'
        return my_autopct
    
    # Place labels inside the pie chart and make them smaller
    wedges, texts, autotexts = ax.pie(status_counts.values, labels=status_counts.index, autopct=make_autopct(status_counts.values), startangle=90, textprops={'fontsize': 5})
    ax.axis('equal')
    ax.set_title("Distribusi Status Mahasiswa", fontsize=7)
    
    st.pyplot(fig)

with tab2:
    import matplotlib.pyplot as plt
    
    st.write("Rata-rata IPK per Fakultas")
    faculty_gpa = filtered_students.groupby('faculty')['gpa'].mean().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(3, 3))
    # Place labels inside the pie chart with both percentage and count
    def make_autopct(values):
        def my_autopct(pct):
            total = sum(values)
            val = int(round(pct*total/100.0))
            return f'{pct:.1f}%\n({val})'
        return my_autopct
    
    # Place labels inside the pie chart and make them smaller
    wedges, texts, autotexts = ax.pie(faculty_gpa.values, labels=faculty_gpa.index, autopct=make_autopct(faculty_gpa.values), startangle=90, textprops={'fontsize': 5})
    ax.axis('equal')
    ax.set_title("Rata-rata IPK per Fakultas", fontsize=7)
    
    st.pyplot(fig)

with tab3:
    st.write("Distribusi Gender Mahasiswa")
    import matplotlib.pyplot as plt
    
    gender_counts = filtered_students['gender'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(gender_counts.values, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title("Distribusi Gender Mahasiswa")
    
    st.pyplot(fig)

# Detailed Data Section
st.markdown("---")
st.subheader("📋 Data Mahasiswa Terfilter")

# Show filtered data with pagination
start_idx = st.slider('Pilih baris awal data', 0, max(0, len(filtered_students)-10), 0)
end_idx = min(start_idx + 10, len(filtered_students))
st.dataframe(filtered_students.iloc[start_idx:end_idx])

# Summary statistics
st.markdown("---")
st.subheader("📈 Statistik Ringkasan")

summary_stats = pd.DataFrame({
    'Statistik': ['Jumlah Total', 'IPK Rata-rata', 'IPK Tertinggi', 'IPK Terendah', 'Rata-rata Umur'],
    'Nilai': [
        len(filtered_students),
        round(filtered_students['gpa'].mean(), 2),
        filtered_students['gpa'].max(),
        filtered_students['gpa'].min(),
        round(filtered_students['age'].mean(), 1)
    ]
})

col1, col2 = st.columns(2)
with col1:
    st.write("**Statistik Umum**")
    st.table(summary_stats)

with col2:
    st.write("**Distribusi Program Studi (Top 5)**")
    top_majors = filtered_students['major'].value_counts().head(5)
    st.bar_chart(top_majors)

# Footer
st.markdown("---")
st.caption("Dashboard Analitik Universitas v1.0 | Dibuat dengan ❤️ menggunakan Streamlit")