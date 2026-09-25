from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Locate the CSV file
project_folder = Path(__file__).parent
data_file = project_folder / "data" / "patient_data.csv"

# Load the dataset
df = pd.read_csv(data_file)

# Display the first five rows
print("First five rows:")
print(df.head())

# Display the dataset dimensions
print("\nDataset size:")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

# Check for missing values
print("\nMissing values:")
print(df.isna().sum())

# Calculate the reduction in CRP
df["CRP_Reduction"] = df["Baseline_CRP"] - df["Week8_CRP"]

print("\nCRP values and reduction:")
print(
    df[
        [
            "Patient_ID",
            "Treatment_Group",
            "Baseline_CRP",
            "Week8_CRP",
            "CRP_Reduction",
        ]
    ]
)

# Compare the average CRP reduction between groups
group_summary = (
    df.groupby("Treatment_Group")[
        ["Baseline_CRP", "Week8_CRP", "CRP_Reduction"]
    ]
    .mean()
    .round(2)
)

print("\nAverage CRP values by treatment group:")
print(group_summary)

# Visualise CRP reduction by treatment group
plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Treatment_Group",
    y="CRP_Reduction",
    color="lightblue"
)

sns.stripplot(
    data=df,
    x="Treatment_Group",
    y="CRP_Reduction",
    color="black",
    size=6
)

plt.title("CRP Reduction After Eight Weeks")
plt.xlabel("Treatment group")
plt.ylabel("CRP reduction (mg/L)")
plt.tight_layout()

figure_file = project_folder / "figures" / "crp_reduction_by_group.png"
plt.savefig(figure_file, dpi=300)
plt.show()