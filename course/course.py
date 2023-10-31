import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample course data with Udemy URLs
course_data = {
    'Course Name': [
        'Python 101',
        'Data Science 101',
        'Web Development Fundamentals',
        'Machine Learning Basics',
        'SQL for Beginners',
        'Java Programming Essentials',
        'JavaScript for Web Development',
        'Artificial Intelligence: An Introduction',
        'Mobile App Development with Flutter',
        'Cybersecurity Fundamentals',
        'Digital Marketing Strategies',
        'Advanced Data Science Techniques',
        'Full-Stack Web Development with MERN Stack',
        'Game Development with Unity',
        'Ethical Hacking and Penetration Testing',
        'Cloud Computing with AWS',
        'UI/UX Design Principles',
        'Blockchain and Cryptocurrency',
        'Data Visualization with Tableau',
        'Robotics and Automation'],
    'Description': [
        'Intro to Python programming',
        'Foundations of data science',
        'Basic web development concepts',
        'Introduction to ML algorithms',
        'Learn SQL database querying',
        'Core Java programming skills',
        'Client-side web scripting with JS',
        'Explore AI and its applications',
        'Create mobile apps with Flutter',
        'Learn about online security',
        'Digital marketing strategies and tactics',
        'Advanced data analysis methods',
        'Build modern web applications',
        'Create games with Unity engine',
        'Learn ethical hacking techniques',
        'Cloud services and infrastructure',
        'Principles of UI/UX design',
        'Explore blockchain technology',
        'Data visualization and insights',
        'Build robots and automate tasks'],
    'Difficulty': [
        'Beginner',
        'Intermediate',
        'Beginner',
        'Intermediate',
        'Beginner',
        'Beginner',
        'Intermediate',
        'Advanced',
        'Intermediate',
        'Advanced',
        'Intermediate',
        'Advanced',
        'Intermediate',
        'Intermediate',
        'Advanced',
        'Intermediate',
        'Intermediate',
        'Advanced',
        'Intermediate',
        'Advanced'
    ],
    'Rating': [4.5, 4.8, 4.2, 4.9, 4.3, 4.6, 4.4, 4.7, 4.5, 4.8, 4.3, 4.7, 4.4, 4.6, 4.2, 4.8, 4.5, 4.9, 4.4, 4.7],
    'Udemy Link': [
        'https://www.udemy.com/course/python-101/',
        'https://www.udemy.com/course/data-science-101/',
        'https://www.udemy.com/course/web-development-fundamentals/',
        'https://www.udemy.com/course/machine-learning-basics/',
        'https://www.udemy.com/course/sql-for-beginners/',
        'https://www.udemy.com/course/java-programming-essentials/',
        'https://www.udemy.com/course/javascript-web-development/',
        'https://www.udemy.com/course/ai-an-introduction/',
        'https://www.udemy.com/course/mobile-app-development-flutter/',
        'https://www.udemy.com/course/cybersecurity-fundamentals/',
        'https://www.udemy.com/course/digital-marketing-strategies/',
        'https://www.udemy.com/course/advanced-data-science-techniques/',
        'https://www.udemy.com/course/full-stack-web-development-mern-stack/',
        'https://www.udemy.com/course/game-development-unity/',
        'https://www.udemy.com/course/ethical-hacking-penetration-testing/',
        'https://www.udemy.com/course/cloud-computing-aws/',
        'https://www.udemy.com/course/ui-ux-design-principles/',
        'https://www.udemy.com/course/blockchain-cryptocurrency/',
        'https://www.udemy.com/course/data-visualization-tableau/',
        'https://www.udemy.com/course/robotics-automation/'
    ]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(course_data)

# Streamlit app
st.title("Course Recommendation System")

st.sidebar.header("User Preferences")

# Create a checkbox to filter by difficulty
filter_difficulty = st.sidebar.checkbox("Filter by Difficulty")
if filter_difficulty:
    preferred_difficulty = st.sidebar.selectbox("Select your preferred course difficulty:", df['Difficulty'].unique())
    filtered_courses = df[df['Difficulty'] == preferred_difficulty]
else:
    filtered_courses = df

# Display recommended courses
st.subheader("Recommended Courses")

# Create clickable links to Udemy
for idx, course_name in enumerate(filtered_courses['Course Name']):
    st.write(f"{idx + 1}. [{course_name}]({filtered_courses.iloc[idx]['Udemy Link']})")

# Adding a bar chart for course ratings
st.subheader("Course Ratings")
st.bar_chart(filtered_courses.set_index('Course Name')['Rating'])

# Placeholder for growth graphs (replace with actual data)
st.subheader("Course Growth Over 10 Years (Placeholder Data):")
for course_name in filtered_courses['Course Name']:
    st.write(f"Growth for {course_name} (Placeholder Data):")
    years = np.arange(1, 11)
    growth_data = np.random.randint(100, 500, size=10)  # Replace with your actual growth data
    fig, ax = plt.subplots()
    ax.plot(years, growth_data, marker='o', linestyle='-', color='b')
    ax.set_xlabel('Years')
    ax.set_ylabel('Growth')
    st.pyplot(fig)

# streamlit run course.py
