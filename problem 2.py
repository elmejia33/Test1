import streamlit as st
import plotly.express as px
import pandas as pd
#import folium
#import seaborn as sns
import matplotlib.pyplot as plt

studentData = pd.read_csv("university_student_dashboard_data.csv")
st.title("Student Admissions Data")
#line Admissions
year = st.slider("Select Year:", int(studentData["Year"].min()), int(studentData["Year"].max()), int(studentData["Year"].min()))
filtered_data = studentData[studentData['Year'] == year]
st.title('University Admissions Data')
st.subheader(f'Admissions Data for {year}')
st.write(filtered_data)
st.subheader('Applications, Admitted, and Enrolled Over Time')
fig, ax = plt.subplots()
ax.plot(filtered_data['Year'], filtered_data['Applications'], label='Applications', marker='o')
ax.plot(filtered_data['Year'], filtered_data['Admitted'], label='Admitted', marker='o')
ax.plot(filtered_data['Year'], filtered_data['Enrolled'], label='Enrolled', marker='o')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
ax.set_title('Applications, Admitted, and Enrolled Over Time')
ax.legend()
st.pyplot(fig)
#Box Department
st.subheader('Enrollment by Department Over Time')
fig, ax = plt.subplots()
filtered_data.set_index('Year')[['Engineering Enrolled', 'Business Enrolled', 'Arts Enrolled', 'Science Enrolled']].plot(kind='bar', stacked=True, ax=ax)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Students')
ax.set_title('Student Enrollment by Department')
st.pyplot(fig)
#Scatter Retention/Satisfaction
st.subheader('Retention Rate vs. Satisfaction Rate')
fig, ax = plt.subplots()
ax.scatter(filtered_data['Retention Rate (%)'], filtered_data['Student Satisfaction (%)'], c=filtered_data['Year'], cmap='viridis')
ax.set_xlabel('Retention Rate (%)')
ax.set_ylabel('Student Satisfaction (%)')
ax.set_title('Retention Rate vs. Satisfaction Rate')
st.pyplot(fig)
