import pandas as pd
import numpy as np
from datetime import datetime
import random

def generate_student_data():
    """
    Generate realistic student management data similar to the Kaggle dataset
    """
    # Create sample data
    data = {
        'student_id': [f'STUD{i:04d}' for i in range(1, 1001)],
        'name': [f'Student_{i}' for i in range(1, 1001)],
        'faculty': np.random.choice([
            'Fakultas Ilmu Komputer', 'Fakultas Ekonomi', 'Fakultas Hukum',
            'Fakultas Teknik', 'Fakultas Sastra', 'Fakultas Kedokteran'
        ], size=1000),
        'major': np.random.choice([
            'Teknik Informatika', 'Sistem Informasi', 'Manajemen', 'Akuntansi',
            'Ilmu Hukum', 'Teknik Elektro', 'Sastra Inggris', 'Kedokteran'
        ], size=1000),
        'year_enrolled': np.random.choice(range(2018, 2024), size=1000),
        'current_year': np.random.choice(['Freshman', 'Sophomore', 'Junior', 'Senior'], size=1000),
        'gpa': np.round(np.random.normal(3.0, 0.5, 1000), 2),
        'status': np.random.choice(['Active', 'Inactive', 'Graduated'], p=[0.8, 0.1, 0.1], size=1000),
        'scholarship': np.random.choice(['None', 'Academic', 'Need-based', 'Sports'], p=[0.7, 0.15, 0.1, 0.05], size=1000),
        'age': np.random.randint(18, 25, size=1000),
        'gender': np.random.choice(['Male', 'Female'], size=1000),
        'city': np.random.choice([
            'Jakarta', 'Bandung', 'Surabaya', 'Medan', 'Makassar', 'Yogyakarta',
            'Semarang', 'Palembang', 'Denpasar', 'Banjarmasin'
        ], size=1000)
    }
    
    df = pd.DataFrame(data)
    
    # Ensure GPA is between 0 and 4
    df['gpa'] = np.clip(df['gpa'], 0, 4)
    
    return df

def generate_academic_performance_data():
    """
    Generate academic performance data
    """
    faculties = ['Fakultas Ilmu Komputer', 'Fakultas Ekonomi', 'Fakultas Hukum',
                 'Fakultas Teknik', 'Fakultas Sastra', 'Fakultas Kedokteran']
    
    years = list(range(2018, 2024))
    
    data = []
    for faculty in faculties:
        for year in years:
            num_students = np.random.randint(80, 150)
            avg_gpa = round(np.random.uniform(2.5, 3.5), 2)
            graduation_rate = round(np.random.uniform(0.7, 0.95), 2)
            
            data.append({
                'faculty': faculty,
                'year': year,
                'num_students': num_students,
                'avg_gpa': avg_gpa,
                'graduation_rate': graduation_rate
            })
    
    return pd.DataFrame(data)

def generate_faculty_data():
    """
    Generate faculty/staff data
    """
    data = {
        'faculty_id': [f'FAC{i:03d}' for i in range(1, 51)],
        'name': [f'Faculty_{i}' for i in range(1, 51)],
        'department': np.random.choice([
            'Teknik Informatika', 'Sistem Informasi', 'Manajemen', 'Akuntansi',
            'Ilmu Hukum', 'Teknik Elektro', 'Sastra Inggris', 'Kedokteran'
        ], size=50),
        'position': np.random.choice(['Professor', 'Associate Professor', 'Assistant Professor', 'Lecturer'], 
                                   p=[0.1, 0.2, 0.3, 0.4], size=50),
        'publications': np.random.poisson(5, size=50),
        'years_experience': np.random.randint(1, 30, size=50)
    }
    
    return pd.DataFrame(data)

# Generate the datasets
student_df = generate_student_data()
academic_df = generate_academic_performance_data()
faculty_df = generate_faculty_data()

# Save to CSV files
student_df.to_csv('students.csv', index=False)
academic_df.to_csv('academic_performance.csv', index=False)
faculty_df.to_csv('faculty.csv', index=False)

print("Sample data generated successfully!")
print(f"Students data shape: {student_df.shape}")
print(f"Academic performance data shape: {academic_df.shape}")
print(f"Faculty data shape: {faculty_df.shape}")

# Show first few rows of each dataset
print("\nStudents data sample:")
print(student_df.head())

print("\nAcademic performance data sample:")
print(academic_df.head())

print("\nFaculty data sample:")
print(faculty_df.head())