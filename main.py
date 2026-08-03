# import modules
from src.load_data import load_data
from src.preprocessing import *
from src.analysis import *
from src.visualisation import *
from src.report import genrate_report

# create the required folder
# os.makedirs("images",exist_ok=True)
# os.makedirs("reports",exist_ok=True)

# load the dataset
print("\n" + "=" * 60)
print("Loading Dataset")
print("="  * 60)

df = load_data("Data\\healthcare_dataset.csv")

# Data preprocessing
print("\n" + "=" * 60)
print("Data Preprocessing")
print("="  * 60)

dataset_info(df)

check_missing_values(df)

check_duplicates(df)

df = remove_duplicates(df)

df = clean_name_col(df)

save_clean_data(df)

# business analysis
print("\n" + "=" * 60)
print("BUSINESS ANALYSIS")
print("="  * 60)

print("\n" + "=" * 60)
print("Patient Demographic Analysis")
print("="  * 60)

gender_count(df)

age_info(df)

blood_group_count(df)

print("\n" + "=" * 60)
print("Disease frequency analysis")
print("="  * 60)

disease_freq(df)

top4_disease(df)

most_common_disease(df)

print("\n" + "=" * 60)
print("Treatment cost analysis")
print("="  * 60)

treatment_cost(df)

total_treatment_cost(df)

print("\n" + "=" * 60)
print("Hospital stay analysis")
print("="  * 60)

hospital_stay_days(df)

average_stay(df)

maximum_stay(df)

minimum_stay(df)

print("\n" + "=" * 60)
print("Department analysis")
print("="  * 60)

count_patient(df)

print("\n" + "=" * 60)
print("Recovery analysis")
print("="  * 60)

recovery_count(df)

recovery_rate(df)

Recovery_percentage(df)

print("\n" + "=" * 60)
print("Correlation analysis")
print("="  * 60)

correlation(df)

print("\n" + "=" * 60)
print("Generate business insights")
print("="  * 60)

business_analysis(df)

# Data visualisation
print("\n" + "=" * 60)
print("Data Visualisation")
print("="  * 60)

age_distribution(df)

gender_count(df)

disease_chart(df)

treatment_cost(df)

hospital_stay(df)

department_count_plot(df)

recovery_pie_chart(df)

stay_vs_billing(df)

age_vs_billing(df)

correlation_heatmap(df)

pair_plot(df)

# Report Generation
print("\n" + "=" * 60)
print("Generate PDF Report")
print("="  * 60)

genrate_report(df)

# Project Completed
print("\n" + "=" * 60)
print("Project Completed Successfully")
print("="  * 60)
