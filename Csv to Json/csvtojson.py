import pandas as pd


datapath = r"C:\Users\swaraj.s\Desktop\csvtojson.csv"
outpath = r"C:\Users\swaraj.s\Desktop\csvtojson.json"


data = pd.read_csv(datapath)

rank = data.world_rank
uni_name = data.university_name
country = data.country
teaching = data.teaching
international = data.international
research = data.research
citations = data.citations
income = data.income
total_score = data.total_score
num_students = data.num_students
student_staff_ratio = data.student_staff_ratio
international_students = data.international_students
female_male_ratio = data.female_male_ratio
year = data.year


container = { }

x = 0

while x< len(uni_name):

    container[uni_name[x]] = [
        {"Rank: ":rank[x],},
        {"Country: ": country[x],},
        {"Teaching: ": teaching[x],},
        {"International: ": international[x],},
        {"Researchh: ", research[x],},
        {"Citation": citations[x],},
        {"Income: ": income[x],},
        {"Total_Score: ": total_score[x],},
        {"Number_Students: ":num_students[x]},
        {"Student_staff_ratio: ": student_staff_ratio[x]},
        {"International_Students; ":international_students[x]},
        {"Female_Male_ratio: ":female_male_ratio[x]},
        {"Year: ": year[x]}

    ]



    x = x+1


df = pd.DataFrame(container)
df.to_json(outpath, indent=4)

