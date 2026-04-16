from flask import Blueprint, request
from app.models.note import Note
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

note_bp = Blueprint("notes", __name__)

@note_bp.route("/notes", methods = ["POST"])
@jwt_required()
def create_note():
    user_id = get_jwt_identity()
    data = request.get_json()

    note = Note(
        title = data["title"],
        content = data.get("content"),
        user_id = user_id
    )

    db.session.add(note)
    db.session.commit()

    return {"message": "Note created successfully", "note_id": note.id}, 201

@note_bp.route("/notes", methods = ["GET"])
@jwt_required()
def get_notes():
    user_id = get_jwt_identity()
    
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 5, type=int)


    note =  Note.query.filter_by(id = id, user_id = user_id).first()


    if not note:
        return ("Error :" "Note not found"), 404
    
    return {
        "id": note.id,
        "title": note.title,
        "content": note.content,
    }, 200


@note_bp.route("/notes/<int:id>", methods = ["PATCH"])
@jwt_required()
def update_note(id):
    user_id = get_jwt_identity()
    data = request.get_json()

    note = Note.query.filter_by(id = id, user_id = user_id).first()


    if not note:
        return ("Error :" "Note not found"), 404
    note.title = data.get("title", note.title)
    note.content = data.get("content", note.content)

    db.session.commit()

    return {"message": "Note updated successfully"}, 200


@note_bp.route("/notes/<int:id>", methods = ["DELETE"])
@jwt_required()
def delete_note(id):
    user_id = get_jwt_identity()

    note = Note.query.filter_by(id = id, user_id = user_id).first()

    if not note:
        return ("Error :" "Note not found"), 404
    
    db.session.delete(note)
    db.session.commit()

    return {"message": "Note deleted successfully"}, 200





    