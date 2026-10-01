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

# Keep patients with both baseline and Week 8 measurements
complete_data = df.dropna(
    subset=["Baseline_CRP", "Week8_CRP"]
).copy()

# Create separate plots for both groups
fig, axes = plt.subplots(1, 2, figsize=(10, 5), sharey=True)

for ax, (group_name, group_data) in zip(
    axes,
    complete_data.groupby("Treatment_Group")
):
    for _, patient in group_data.iterrows():
        ax.plot(
            ["Baseline", "Week 8"],
            [patient["Baseline_CRP"], patient["Week8_CRP"]],
            marker="o",
            alpha=0.7
        )

    ax.set_title(group_name)
    ax.set_xlabel("Study visit")
    ax.grid(axis="y", alpha=0.3)

axes[0].set_ylabel("CRP (mg/L)")
fig.suptitle("Individual CRP Changes After Eight Weeks")

plt.tight_layout()

figure_file = (
    project_folder
    / "figures"
    / "crp_before_after_by_group.png"
)

plt.savefig(figure_file, dpi=300)
plt.show()

# Keep patients with recorded response information
response_data = df.dropna(subset=["Response"]).copy()

# Convert Yes and No into numerical values
response_data["Responder"] = response_data["Response"].map(
    {"Yes": 1, "No": 0}
)

# Calculate response statistics for each group
response_summary = (
    response_data.groupby("Treatment_Group")["Responder"]
    .agg(["sum", "count", "mean"])
)

response_summary["Response_Rate_Percent"] = (
    response_summary["mean"] * 100
)

print("\nResponse summary:")
print(
    response_summary[
        ["sum", "count", "Response_Rate_Percent"]
    ].round(1)
)

# Create a bar chart
plot_data = response_summary.reset_index()

plt.figure(figsize=(7, 5))

ax = sns.barplot(
    data=plot_data,
    x="Treatment_Group",
    y="Response_Rate_Percent",
    color="steelblue"
)

ax.bar_label(ax.containers[0], fmt="%.1f%%")

plt.title("Response Rate by Treatment Group")
plt.xlabel("Treatment group")
plt.ylabel("Response rate (%)")
plt.ylim(0, 110)
plt.tight_layout()

figure_file = (
    project_folder
    / "figures"
    / "response_rate_by_group.png"
)

plt.savefig(figure_file, dpi=300)
plt.show()
