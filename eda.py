import pandas as pd

df = pd.read_csv("internship_data.csv")

print(df.head())
print(df.info())
print(df.describe())
print(df.shape)

import matplotlib.pyplot as plt

skills = [
    "Python", "Java", "SQL", "Excel",
    "Pandas", "Machine_Learning",
    "Data_Visualization"
]

skill_counts = df[skills].sum()

skill_counts.plot(kind="bar")

plt.title("Most Requested Internship skills")
plt.xlabel("Technical Skills")
plt.ylabel("Number of Internships")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# Visualization 2: Internship Match Percentages

student_skills = {
    "Python": 1,
    "Java": 1,
    "SQL": 0,
    "Excel": 1,
    "Pandas": 0,
    "Machine_Learning": 0,
    "Data_Visualization": 0
}

match_percentages = []

for index, internship in df.iterrows():
    required_skills = 0
    matches = 0

    for skill in skills:
        if internship[skill] == 1:
            required_skills += 1

            if student_skills[skill] == 1:
                matches += 1

    if required_skills > 0:
        percentage = (matches / required_skills) * 100
    else:
        percentage = 0

    match_percentages.append(percentage)

df["Match_Percentage"] = match_percentages

df_sorted = df.sort_values(
    by="Match_Percentage",
    ascending=False
)

plt.figure(figsize=(12, 7))

plt.barh(
    df_sorted["Company"],
    df_sorted["Match_Percentage"]
)

plt.title("Internship Match Percentages")
plt.xlabel("Match Percentage (%)")
plt.ylabel("Company")
plt.xlim(0, 100)
plt.tight_layout()
plt.show()


# Visualization 3: Missing Technical Skills

missing_skills = {}

for skill in skills:
    if student_skills[skill] == 0:
        missing_skills[skill] = df[skill].sum()

missing_skills_series = pd.Series(missing_skills)

missing_skills_series = missing_skills_series.sort_values(
    ascending=False
)

plt.figure(figsize=(9, 5))

missing_skills_series.plot(kind="bar", color="orange")

plt.title("Missing Skills Across Internships")
plt.xlabel("Technical Skills")
plt.ylabel("Number of Internships Requiring Skill")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.show()
