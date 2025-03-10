studentData = pd.read_csv("university_student_dashboard_data.csv")
st.title("Student Admissions Data")
year = st.slider("Select Year:", int(studentData["Year"].min()), int(studentData["Year"].max()), int(studentData["Year"].min()))
fig = px.scatter(studentData, x="Applications", y="Admitted",
                 size_max=60)
st.plotly_chart(fig)
