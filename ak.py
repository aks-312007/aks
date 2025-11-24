from flask import Flask, render_template, request
from sanitize import sanitize_html  # import the function above

app = Flask(__name__)

@app.route('/comment', methods=['POST'])
def comment():
    raw = request.form.get('text', '')
    safe = sanitize_html(raw)
    # Jinja2 will still escape, but content is already sanitized
    return render_template('comment.html', text=safe)

