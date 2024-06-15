#ay to seperate the file 
from flask import Blueprint , render_template, request,flash, jsonify
from flask_login import  login_required,     current_user
import json
from .models import Note

from . import db
from .models import Note
views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    

    if request.method == 'POST':
        if len(Note) < 1:
            flash('Note cannt be used for short')  


    return render_template("home.html",user=current_user)



@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteID = note['noteId']
    note = Note.query.get(noteID)
    if note:        
        if note.user_id == current_user.id:
            db.session.delete(note)

            db.session.commit()
    return jsonify({})