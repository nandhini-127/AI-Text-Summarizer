
import os
import pandas as pd

from main import summarize_text

examples = [
    {
        "topic": "Artificial Intelligence",
        "text": (
            "Artificial intelligence enables computers to perform "
            "tasks that usually require human intelligence. AI is "
            "used in healthcare for disease detection, in education "
            "for personalized learning, and in transportation for "
            "route optimization. However, AI can produce inaccurate "
            "results, so human verification remains important."
        ),
        "expected_facts": (
            "AI supports healthcare, education, and transportation; "
            "AI outputs may need human verification."
        )
    },
    {
        "topic": "Climate Change",
        "text": (
            
            "Climate change refers to long-term changes in "
            "temperature and weather patterns. Burning fossil fuels "
            "increases greenhouse gas concentrations. These gases "
            "trap heat and contribute to global warming. Climate "
            "change affects ecosystems, agriculture, and water "
            "resources. Renewable energy can help reduce emissions."
        ),
        "expected_facts": (
            "Fossil fuels increase greenhouse gases; climate change "
            "affects ecosystems, agriculture, and water resources."
        )
    },
    {
        "topic": "Education",
        "text": (
            "Technology has changed how students learn. Online "
            "courses provide access to educational resources from "
            "different locations. Digital tools support collaboration "
            "and self-paced learning. However, unequal internet "
            "access and excessive screen time can create challenges."
        ),
        "expected_facts": (
            "Technology supports online and self-paced learning; "
            "internet access and screen time can be challenges."
        )
    },
    {
        "topic": "Healthcare",
        "text": (
            "Wearable devices can monitor heart rate, physical "
            "activity, and sleep. Some devices identify unusual "
            "patterns and encourage users to seek medical advice. "
            "Device readings are not always accurate and should "
            "not replace professional medical diagnosis."
        ),
        "expected_facts": (
            "Wearables monitor health measurements; their readings "
            "may be inaccurate and do not replace diagnosis."
        )
    },
    {
        "topic": "Cybersecurity",
        "text": (
            "Cybersecurity protects computers, networks, and "
            "information from unauthorized access and attacks. "
            "Common threats include phishing, malware, and password "
            "theft. Strong unique passwords, multifactor "
            "authentication, software updates, and avoiding "
            "suspicious links can improve security."
        ),
        "expected_facts": (
            "Threats include phishing, malware, and password theft; "
            "security practices help reduce risk."
        )
    }
]

results = []

for number, example in enumerate(examples, start=1):
    print(f"\n{'=' * 50}")
    print(f"TEST {number}: {example['topic']}")

    summary = summarize_text(
        example["text"],
        length="short"
    )

    print("\nGenerated summary:")
    print(summary)

    results.append({
        "Test_No": number,
        "Topic": example["topic"],
        "Input_Text": example["text"],
        "Expected_Facts": example["expected_facts"],
        "Generated_Summary": summary,
        "Factual_Accuracy": "",
        "Instruction_Following": "",
        "Comments": ""
    })

# Save evaluation results
os.makedirs("outputs", exist_ok=True)

df = pd.DataFrame(results)

file_path = "outputs/evaluation_results.csv"
df.to_csv(file_path, index=False)

print(f"\nEvaluation file saved to: {file_path}")
print("\nAll five test cases completed.")
