from app import create_app
from app.extensions import db, bcrypt  
from app.models import User, Note

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Fixed: Added 'User' class call
    user1 = User(username="Sammy", password_hash=bcrypt.generate_password_hash("Kiddo12345").decode("utf-8"))
    user2 = User(username="Samantha", password_hash=bcrypt.generate_password_hash("Kiddo54321").decode("utf-8"))

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit() # Commit here so user1.id and user2.id are generated

    note1 = Note(
        title="King's Jewls",
        content="The King's Jewls are hidden in the castle's secret chamber.",
        user_id=user1.id
    )

    note2 = Note(
        title="Ancient Map",
        content="The ancient map reveals the location of a hidden treasure buried deep in the forest.",
        user_id=user1.id
    )

    note3 = Note(
        title="Mysterious Letter",
        content="The mysterious letter contains cryptic clues about a long-lost artifact hidden in the old library.",
        user_id=user2.id
    )
    
    note4 = Note(
        title="Note B",
        content="More data here",
        user_id=user2.id
    )

    db.session.add_all([note1, note2, note3, note4])
    db.session.commit()
    
    print("Database seeded successfully!")
