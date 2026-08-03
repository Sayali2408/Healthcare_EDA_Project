import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# create image folder automatically
os.makedirs("images",exist_ok=True)

def age_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df["Age"],bins=10,kde=True)
    plt.title(" Patient Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.savefig("images/age_distribution.png")
    plt.show()

def gender_count(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x = "Gender",data = df)
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("Count")
    plt.savefig("images/Gender_distribution_Count.png")
    plt.show()
    
def disease_chart(df):
    plt.figure(figsize=(8,5))
    sns.barplot(
        x="Medical Condition",
        y= "Test Results",
        data=df
    )
    plt.title("Disease Bar Chart")
    plt.xticks(rotation=45)
    plt.savefig("images/disease_bar_chart.png")
    plt.show()
    
def treatment_cost(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df["Billing Amount"],bins=10,kde=True)
    plt.title("Treatment Cost")
    plt.xlabel("Treatment Cost")
    plt.ylabel("Count")
    plt.savefig("images/treatment_cost.png")
    plt.show()
    
def hospital_stay(df):
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], dayfirst=True)
    df["Discharge Date"] = pd.to_datetime(df["Discharge Date"], dayfirst=True)
    df["Hospital Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days
    plt.figure(figsize=(8,5))
    sns.boxplot(
        y="Hospital Stay",
        data=df
    )
    plt.title("Hospital Stay Box Plot")
    plt.ylabel("Hospital Stay (Days)")
    plt.savefig("images/hospital_stay_boxplot.png")
    plt.show()
    
def department_count_plot(df):
    plt.figure(figsize=(8,5))
    sns.countplot(
        x="Medical Condition",
        data=df
    )
    plt.title("Department Count Plot")
    plt.xlabel("Medical Condition")
    plt.ylabel("Number of Patients")
    plt.xticks(rotation=45)
    plt.savefig("images/department_count_plot.png")
    plt.show()
    
def recovery_pie_chart(df):
    recovery = df["Test Results"].value_counts()
    plt.figure(figsize=(6,6))
    plt.pie(
        recovery,
        labels=recovery.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Recovery Analysis")
    plt.savefig("images/recovery_pie_chart.png")
    plt.show()
    
def stay_vs_billing(df):
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], dayfirst=True)
    df["Discharge Date"] = pd.to_datetime(df["Discharge Date"], dayfirst=True)
    df["Hospital Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days
    plt.figure(figsize=(8,5))
    sns.scatterplot(
        x="Hospital Stay",
        y="Billing Amount",
        data=df.head(100)
    )
    plt.title("Hospital Stay vs Billing Amount")
    plt.xlabel("Hospital Stay (Days)")
    plt.ylabel("Billing Amount")
    plt.savefig("images/stay_vs_billing.png")
    plt.show()
    
def age_vs_billing(df):
    plt.figure(figsize=(8,5))
    sns.scatterplot(
        x="Age",
        y="Billing Amount",
        data=df.head(100)
    )
    plt.title("Age vs Billing Amount")
    plt.xlabel("Age")
    plt.ylabel("Billing Amount")

    plt.savefig("images/age_vs_billing.png")
    plt.show()
    
def correlation_heatmap(df):
    df["Date of Admission"] = pd.to_datetime(df["Date of Admission"], dayfirst=True)
    df["Discharge Date"] = pd.to_datetime(df["Discharge Date"], dayfirst=True)
    df["Hospital Stay"] = (df["Discharge Date"] - df["Date of Admission"]).dt.days
    corr = df[["Age", "Billing Amount", "Hospital Stay"]].corr()
    plt.figure(figsize=(6,5))
    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
    plt.title("Correlation Heatmap")
    plt.savefig("images/correlation_heatmap.png")
    plt.show()
    
def pair_plot(df):
    sns.pairplot(
        df.head(100),
        vars=["Age", "Billing Amount", "Hospital Stay"],
        hue="Gender"
    )
    plt.savefig("images/pair_plot.png")
    plt.show()