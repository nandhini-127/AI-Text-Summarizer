
import pandas as pd

file_path = "outputs/evaluation_results.csv"
df = pd.read_csv(file_path)

# Remove tests that have not yet been evaluated
reviewed = df[
    df["Factual_Accuracy"].isin(["Pass", "Partial", "Fail"])
]

if reviewed.empty:
    print("Evaluate the summaries in the CSV file first.")
else:
    correct = (
        reviewed["Factual_Accuracy"] == "Pass"
    ).sum()

    accuracy_rate = correct / len(reviewed) * 100

    print("Total reviewed:", len(reviewed))
    print(f"Fully factually supported: {accuracy_rate:.1f}%")

    instruction_results = reviewed[
        reviewed["Instruction_Following"].isin(["Pass", "Fail"])
    ]

    if not instruction_results.empty:
        followed = (
            instruction_results["Instruction_Following"] == "Pass"
        ).sum()

        rate = followed / len(instruction_results) * 100

        print(f"Instruction-following rate: {rate:.1f}%")
