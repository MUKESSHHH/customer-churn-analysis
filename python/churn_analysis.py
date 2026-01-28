import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load & clean data
df = pd.read_csv("../data/customer_churn.csv")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)

sns.set(style="whitegrid")

# -----------------------------
# ONE ADVANCED FIGURE
# -----------------------------
fig, axes = plt.subplots(2, 2, figsize=(15, 11))
fig.suptitle("Customer Churn – Advanced Exploratory Analysis", fontsize=18)

# 1️⃣ Violin Plot: Tenure Distribution by Churn (Advanced)
sns.violinplot(
    x='Churn',
    y='tenure',
    data=df,
    inner='quartile',
    ax=axes[0, 0]
)
axes[0, 0].set_title("Tenure Distribution by Churn")

# 2️⃣ KDE Plot: Monthly Charges Density (Advanced)
sns.kdeplot(
    data=df[df['Churn'] == 'Yes']['MonthlyCharges'],
    label='Churned',
    fill=True,
    ax=axes[0, 1]
)
sns.kdeplot(
    data=df[df['Churn'] == 'No']['MonthlyCharges'],
    label='Not Churned',
    fill=True,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Monthly Charges Density")
axes[0, 1].legend()

# 3️⃣ Stacked Bar: Contract Type vs Churn (Business View)
contract_churn = pd.crosstab(df['Contract'], df['Churn'], normalize='index')
contract_churn.plot(
    kind='bar',
    stacked=True,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Churn Share by Contract Type")
axes[1, 0].set_ylabel("Proportion")

# 4️⃣ Scatter + Transparency: Tenure vs Monthly Charges
sns.scatterplot(
    data=df,
    x='tenure',
    y='MonthlyCharges',
    hue='Churn',
    alpha=0.4,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Tenure vs Monthly Charges")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
