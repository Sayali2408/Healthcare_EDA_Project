import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import(
    SimpleDocTemplate,
    Paragraph,
    Image,
    Spacer
)

def genrate_report(df):
    os.makedirs("reports",exist_ok=True)
    
    pdf = SimpleDocTemplate(
        "reports/Final_Report.pdf"
    )
    styles = getSampleStyleSheet()
    elements = []
    
    # Title
    elements.append(
        Paragraph(
            "Healthcare Patient Analysis",
            styles["Title"]
        )     
    )
    elements.append(Spacer(1,20))
    
    
# Business Insights    
    elements.append(
        Paragraph(
            "<b>Business Insights</b>",
            styles["Heading2"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Total Patients: {len(df)}",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Average Patient Age: {round(df['Age'].mean(), 2)} Years",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Most Common Disease: {df['Medical Condition'].mode()[0]}",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Average Treatment Cost: {round(df['Billing Amount'].mean(), 2)}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Most Common Admission Type: {df['Admission Type'].mode()[0]}",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Most Common Blood Group: {df['Blood Type'].mode()[0]}",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Most Common Insurance Provider: {df['Insurance Provider'].mode()[0]}",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Recovery Rate (Normal Test Results): {round((df['Test Results']=='Normal').mean()*100, 2)}%",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Average Hospital Stay: {round(df['Hospital Stay'].mean(), 2)} Days",
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1, 20))
    
# Charts
    elements.append(
        Paragraph(
            "<b>Charts</b>",
            styles["Heading2"]
        )
    )
    elements.append(Image("images/age_distribution.png", width=400, height=250))
    elements.append(Spacer(1, 10))
    
    elements.append(Image("images/Gender_distribution_Count.png", width=400, height=250))
    elements.append(Spacer(1, 10))
    
    elements.append(Image("images/disease_bar_chart.png", width=400, height=250))
    elements.append(Spacer(1, 10))
    
    elements.append(Image("images/treatment_cost.png", width=400, height=250))
    elements.append(Spacer(1, 10))
    
    elements.append(Image("images/hospital_stay_boxplot.png", width=400, height=250))
    elements.append(Spacer(1, 10))
    
    elements.append(Image("images/department_count_plot.png", width=400, height=250))
    elements.append(Spacer(1, 10))
    
    elements.append(Image("images/recovery_pie_chart.png", width=400, height=250))
    elements.append(Spacer(1, 10))
    
    elements.append(Image("images/age_vs_billing.png", width=400, height=250))
    elements.append(Spacer(1, 10))
    
    elements.append(Image("images/correlation_heatmap.png", width=400, height=250))
    elements.append(Spacer(1, 10))
    
    elements.append(Image("images/pair_plot.png", width=400, height=250))
    elements.append(Spacer(1, 20))
    
# Final Summary
    elements.append(
        Paragraph(
            "<b>Final Summary</b>",
            styles["Heading2"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Total Patients Analysed: {len(df)}",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Average Patient Age: {round(df['Age'].mean(), 2)} Years",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Most Common Disease: {df['Medical Condition'].mode()[0]}",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Average Treatment Cost: {round(df['Billing Amount'].mean(), 2)}",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Recovery Rate: {round((df['Test Results']=='Normal').mean()*100, 2)}%",
            styles["BodyText"]
        )
    )
    
    elements.append(Spacer(1,20))
    
# Recommendations
    elements.append(
        Paragraph(
            "<b>Recommendations</b>",
            styles["Heading2"]
        )
    )
    
    elements.append(
        Paragraph(
            "1. Allocate more doctors and resources to departments treating the most common diseases.",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            "2. Monitor patients with longer hospital stays to improve recovery and reduce treatment costs.",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            "3. Improve treatment plans for patients with abnormal or inconclusive test results.",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            "4. Plan medicine inventory based on disease frequency to avoid shortages.",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            "5. Continue using data-driven analysis to improve patient care, hospital efficiency, and resource planning.",
            styles["BodyText"]
        )
    )
    
    elements.append(Spacer(1,20))
    
    # Build PDF
    pdf.build(elements)
    print("=" * 50)
    print("Final_Report.pdf Generated Successfully")
    print("=" * 50)