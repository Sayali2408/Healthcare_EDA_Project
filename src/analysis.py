import pandas as pd
def gender_count(df):
    print("\nGender Count")
    print(df['Gender'].value_counts())
    
def age_info(df):
    print("\nAge Description")
    print(df["Age"].describe())
    
def blood_group_count(df):
    print("\nBlood Group Type Count")
    print(df["Blood Type"].value_counts())

def disease_freq(df):
    print("\nDisease frequency")
    print(df["Medical Condition"].value_counts())
    
def top4_disease(df):
    print("\nTop 4 Disease")
    print(df["Medical Condition"].value_counts().head(4))
    
def most_common_disease(df):
    print("\nMost Common Disease")
    print(df["Medical Condition"].value_counts().idxmax())
    
def treatment_cost(df):
    print("\nTreatment Cost Description")
    print(df["Billing Amount"].describe())
    
def total_treatment_cost(df):
    print("\nTotal Treatment Cost")
    print(df["Billing Amount"].sum())
    
def hospital_stay_days(df):
    print("\nTotal Hospital Stay Days")
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], dayfirst=True)
    df["Discharge Date"] = pd.to_datetime(df["Discharge Date"], dayfirst=True)
    df["Hospital Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days
    print(df[["Date of Admission","Discharge Date","Hospital Stay"]].head(10))

def average_stay(df):
    print("\nAverage Hospital Stay")
    print(df["Hospital Stay"].mean())
    
def maximum_stay(df):
    print("\nMaximum Hospital Stay")
    print(df["Hospital Stay"].max())
    
def minimum_stay(df):
    print("\nMiniimum Hospital Stay")
    print(df["Hospital Stay"].min())

def count_patient(df):
    print("\nDepartment-wise Patient Count")
    print(df["Medical Condition"].value_counts())
    
def recovery_count(df):
    print("\nPatient Recovery Count")
    print(df["Test Results"].value_counts())
    
def recovery_rate(df):
    print("\nRecovery Rate")
    print((df["Test Results"] == "Normal").mean() * 100)

def Recovery_percentage(df):
    print("\nRecovery Percentage")
    print(df["Test Results"].value_counts(normalize=True) * 100)
    
def correlation(df):
    print("\nAge, Billing Amount and Hospital Stay Correlation Analysis")
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], dayfirst=True)
    df["Discharge Date"] = pd.to_datetime(df["Discharge Date"], dayfirst=True)
    df["Hospital Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days
    numeric_data = df[["Age", "Billing Amount", "Hospital Stay"]]
    print(numeric_data.corr())

def business_analysis(df):
    print("\nTotal Patients:", len(df))
    print("Average Age:", round(df["Age"].mean(),2))
    print("Most Common Disease:", df["Medical Condition"].mode()[0])
    print("Average Treatment Cost:", round(df["Billing Amount"].mean(), 2))
    print("\nGender Distribution:",df["Gender"].value_counts())
    print("\nRecovery Status:",df["Test Results"].value_counts())