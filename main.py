import pandas as pd

df= pd.read_csv("internship_data.csv")

student_skills = {
    "Python" :1,
    "Java" :1,
    "SQL" :0,
    "Excel" :1,
    "Pandas" :0,
    "Machine_Learning" :0,
    "Data_Visualization" :0

}

skill_columns = [
    "Python",
    "Java",
    "SQL",
    "Excel",
    "Pandas",
    "Machine_Learning",
    "Data_Visualization"
]

results = []

for index, internship in df.iterrows():
    matches = 0
    required_skills = 0

    for skill in skill_columns:
        if internship[skill] == 1:
           required_skills += 1

        if student_skills[skill] == 1 and internship[skill] == 1:
           matches += 1
 
    match_percentage = (matches / required_skills) * 100

    results.append({
        
    })

    print(internship["Company"], "match percentages:", round(match_percentage), "%")

