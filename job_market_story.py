# Install necessary packages
# pip install streamlit

import streamlit as st

# Set the page title and introduction
st.title("Aziz's anxiety-free guide to the Saudi job market")
st.subheader("Insights from Faisal, the Wannabe Data Scientist")

st.write("""
Aziz, a fresh graduate, is ready to enter the job market. He turns to his friend Faisal, a wannabe data scientist, 
for insights on Saudi Arabia's job market. Faisal analyzes the data and provides key information on job 
opportunities, gender preferences, salary expectations, and more.
""")

# Section 1: Job Postings by Region
st.header("1. Where are the Jobs?")
st.write("**Insight:** Job opportunities are concentrated mainly in Riyadh (42.5%), followed by Makkah (24.9%) and the Eastern Province (15%).")
st.write("**Tip for Aziz:** To maximize his chances, Aziz should consider looking for jobs in Riyadh or Makkah.")
st.image("./images/regions.png", caption="Proportion of Job Postings by Region")

# Section 2: Gender Preferences in Job Postings
st.header("2. Males VS Females")
st.write("**Insight:** 38.9% of job postings are open to both genders, while 32.5% prefer male candidates and 28.6% prefer female.")
st.write("**Tip for Aziz:** Gender-neutral roles are plentiful, giving him a broad range of options regardless of gender preferences.")
st.image("./images/gender.png", caption="Gender Preferences in Job Postings")

# Section 3: Salary Distribution for Fresh Graduates
st.header("3. Brokie or Baller?")
st.write("**Insight:** Most fresh graduate positions offer salaries around 4,000 SAR, with higher salaries (up to 9,000 SAR) being less common.")
st.write("**Tip for Aziz:** Aziz can set realistic salary expectations at the entry-level and plan his career path accordingly.")
st.image("./images/salary.png", caption="Salary Distribution for Fresh Graduates")

# Section 4: Job Opportunities for Fresh Graduates vs. Experienced Individuals
st.header("4. Fresh Meat or Seasoned Pro?")
st.write("**Insight:** There are 760 job postings for fresh graduates compared to 532 for experienced professionals.")
st.write("**Tip for Aziz:** The job market is friendly to new grads, with plenty of entry-level openings. Aziz can start applying with confidence!")
st.image("./images/fresh_vs_exp.png", caption="Job Opportunities for Fresh Graduates vs. Experienced Individuals")

# Conclusion
st.subheader("Sooooo, what does this all mean for Aziz?")
st.write("""
With Faisal’s data-driven guidance, Aziz now has a clear picture of where to focus his job search and what to expect as he embarks on his career. 
From knowing the best cities for jobs to understanding salary ranges, Aziz is better prepared to enter the job market with confidence.
""")
