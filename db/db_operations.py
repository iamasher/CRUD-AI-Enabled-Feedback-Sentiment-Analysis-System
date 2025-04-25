from db.models import db, Feedback
from utils.sentiment_analysis import analyze_sentiment

def add_feedback(text):
    sentiment = analyze_sentiment(text)
    feedback = Feedback(text=text, sentiment=sentiment)
    db.session.add(feedback)
    db.session.commit()
    return feedback

def get_all_feedback():
    return Feedback.query.order_by(Feedback.timestamp.desc()).all()

def update_feedback(feedback_id, new_text):
    feedback = Feedback.query.get(feedback_id)
    if feedback:
        feedback.text = new_text
        feedback.sentiment = analyze_sentiment(new_text)  # Re-analyze sentiment
        db.session.commit()
        return feedback
    return None

def delete_feedback(feedback_id):
    feedback = Feedback.query.get(feedback_id)
    if feedback:
        db.session.delete(feedback)
        db.session.commit()
        return True
    return False
