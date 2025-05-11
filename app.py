from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Organized by tone
positive = [
    "It is certain.",
    "Without a doubt.",
    "Yes, definitely.",
    "You may rely on it.",
    "Most likely.",
    "Outlook good.",
    "Signs point to yes."
]

neutral = [
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again."
]

negative = [
    "Don't count on it.",
    "My reply is no.",
    "Very doubtful.",
    "Outlook not so good.",
    "Chances are slim."
]

# Combine and shuffle for first round
all_responses = positive + neutral + negative
used_responses = []

@app.route("/", methods=["GET", "POST"])
def magic_8_ball():
    answer = None
    question = None
    error = None

    if request.method == "POST":
        question = request.form.get("question").strip().lower()

        # Quit functionality
        if question == "quit":
            return render_template("quit.html")

        # Check for valid question
        if not question.endswith("?") or len(question.split()) < 2:
            error = "Hmm... That doesn't sound like a proper question. Try something like: 'Will I ace the test?'"
        else:
            # Avoid repeating responses until all have been used
            if len(used_responses) == len(all_responses):
                used_responses.clear()

            remaining = [r for r in all_responses if r not in used_responses]
            answer = random.choice(remaining)
            used_responses.append(answer)

    return render_template("index.html", question=question, answer=answer, error=error)


if __name__ == "__main__":
    app.run(debug=True)
