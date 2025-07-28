from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime
import random

app = Flask(__name__)

JOURNAL_FILE = 'journal_entries.txt'
JOURNAL_DIR = "journal_entries"
os.makedirs(JOURNAL_DIR, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entry = request.form['entry']
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(JOURNAL_FILE, 'a', encoding='utf-8') as file:
            file.write(f"Time: {timestamp}\nEntry: {entry}\n---\n")

        return redirect(url_for('thank_you'))

    return render_template('index.html')


@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@app.route('/goodbye')
def goodbye():
    return render_template('goodbye.html')

@app.route('/random')
def randomest():
    prompts = [
        "What’s one thing you’re grateful for today?",
        "What’s something that made you smile?",
        "What’s on your mind right now?",
        "Describe your mood in three words.",
        "Write about a small win you had today."
    ]
    prompt = random.choice(prompts)
    return render_template('index.html', prompt=prompt)

@app.route('/submit', methods=['POST'])
def submit():
    entry = request.form['entry']
    mood = request.form['mood']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('journal_entries.txt', 'a', encoding='utf-8') as f:
        f.write(f"Time: {timestamp}\nMood: {mood}/10\nEntry: {entry}\n---\n")

    return redirect('/thank-you')

@app.route('/entries')
def entries():
    if os.path.exists('journal_entries.txt'):
        with open('journal_entries.txt', 'r') as file:
            entries = file.read().strip().split('\n---\n')  # or your actual separator
    else:
        entries = []
    return render_template('view.html', entries=entries)



@app.route('/view')
def view_entries():
    if os.path.exists('journal_entries.txt'):
        with open('journal_entries.txt', 'r') as file:
            entries = file.read().strip().split('\n---\n')  # Or however you separate them
    else:
        entries = []
    return render_template('view.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)

