import stories
from flask import Flask, render_template, request

app = Flask(__name__)

# used to generate Sample story
words = ["place", "noun", "verb", "adjective", "plural_noun"]
template = """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""


@app.route("/")
def generate_form():
    return render_template("storyForm.html", words=words)


@app.route("/story")
def generate_story():
    answers = request.args
    story = stories.Story(
        words,
        template
    )
    your_story = stories.Story.generate(story, answers)

    return render_template("story.html", story=your_story)
