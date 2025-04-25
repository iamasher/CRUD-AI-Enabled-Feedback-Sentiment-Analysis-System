from flask import Flask, render_template, request, redirect, url_for
from db.models import db, Feedback
from db.db_operations import add_feedback, get_all_feedback, update_feedback, delete_feedback
from utils.sentiment_analysis import analyze_sentiment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Create the database and tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """
    Show the feedback submission form.
    """
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_feedback():
    """
    Handle form submission, analyze sentiment, and save feedback.
    """
    text = request.form.get('feedback')
    if text:
        feedback = add_feedback(text)
        return redirect(url_for('dashboard'))
    return "Please provide valid feedback.", 400

@app.route('/dashboard')
def dashboard():
    """
    Show all feedback with sentiment.
    """
    feedback_list = get_all_feedback()
    return render_template('dashboard.html', feedback_list=feedback_list)

@app.route('/edit/<int:id>', methods=['POST'])
def edit_feedback(id):
    """
    Update feedback.
    """
    new_text = request.form.get('new_feedback')
    if new_text:
        updated_feedback = update_feedback(id, new_text)
        if updated_feedback:
            return redirect(url_for('dashboard'))
    return "Failed to update feedback.", 400

@app.route('/delete/<int:id>', methods=['POST'])
def delete_feedback_route(id):
    """
    Delete feedback.
    """
    if delete_feedback(id):
        return redirect(url_for('dashboard'))
    return "Failed to delete feedback.", 400

if __name__ == '__main__':
    app.run(debug=True)
