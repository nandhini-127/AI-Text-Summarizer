
from transformers import pipeline, AutoTokenizer

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

print("Loading AI summarization model...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

summarizer = pipeline(
    "summarization",
    model=MODEL_NAME
)

print("Model loaded successfully!")

# Maximum input length allowed by this application
MAX_INPUT_TOKENS = 900

# Requested summary lengths, measured in tokens

LENGTH_SETTINGS = {
    "short": (20, 60),
    "medium": (40, 100),
    "long": (60, 150)
}



def summarize_text(text, length="short"):
    """Validate input and generate a summary."""

    # Handle empty input
    if not isinstance(text, str) or not text.strip():
        return "Error: Please enter some text."

    # Validate summary length
    length = length.lower().strip()

    if length not in LENGTH_SETTINGS:
        return "Error: Choose short, medium, or long."

    # Check input token count
    input_tokens = tokenizer.encode(
        text,
        add_special_tokens=True,
        truncation=False
    )

    if len(input_tokens) > MAX_INPUT_TOKENS:
        return (
            f"Error: Input contains {len(input_tokens)} tokens. "
            f"Please shorten it to {MAX_INPUT_TOKENS} tokens or fewer."
        )

    # Set generation limits based on the requested length
    min_tokens, max_tokens = LENGTH_SETTINGS[length]

    # Adapt the limits for shorter input passages
    max_tokens = min(max_tokens, max(12, len(input_tokens) - 2))
    min_tokens = min(min_tokens, max(5, max_tokens // 3))

    # Generate summary
    result = summarizer(
        text,
        min_length=min_tokens,
        max_length=max_tokens,
        do_sample=False,
        truncation=True
    )

    return result[0]["summary_text"]


def main():
    print("\n===== AI TEXT SUMMARIZER =====")

    text = """Artificial intelligence enables computers to perform
tasks that usually require human intelligence. It is
used in healthcare, education, transportation, and
business. AI can improve productivity and support
decision-making, but it may also produce incorrect
information. Therefore, important AI-generated results
should be verified before they are used."""

    print("\nChoose summary length:")
    print("1. Short")
    print("2. Medium")
    print("3. Long")

    choice = input("Enter your choice (1/2/3): ").strip()

    length_map = {
        "1": "short",
        "2": "medium",
        "3": "long"
    }

    if choice not in length_map:
        print("Error: Please select 1, 2, or 3.")
        return

    summary = summarize_text(text, length_map[choice])

    print("\n===== GENERATED SUMMARY =====")
    print(summary)


if __name__ == "__main__":
    main()
