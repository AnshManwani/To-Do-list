from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    if content:
        now = datetime.now()
        timestamp = now.strftime("%B %d, %Y — %I:%M %p")
        tasks.append({'content': content, 'timestamp': timestamp})
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    if 0 <= task_id < len(tasks):
        new_content = request.form['updated_content']
        if new_content:
            now = datetime.now()
            tasks[task_id]['content'] = new_content
            tasks[task_id]['timestamp'] = now.strftime("%B %d, %Y — %I:%M %p")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
