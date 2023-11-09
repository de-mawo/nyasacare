from flask import request, jsonify
import uuid
from app.extensions import db , bcrypt
from app.models.user import User


def list_all_users():
    users = User.query.all()
    results = [
        {
            "id": user.id,
            "name": user.name,
            "lastname": user.lastname,
            "email": user.email,
            "phone": user.phone,
            "profile_img": user.profile_img,
            "created_at": user.created_at,
            "updated_at": user.updated_at
            
        } for user in users]

    return {"count": len(results), "users": results}


def create_user(form):    
    id = str(uuid.uuid4())
    hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    new_user = User(
        id=id,
        name=form.name.data,
        email=form.email.data,
        phone=form.phone.data,
        password=hashed_password,
    ) 

    db.session.add(new_user)
    db.session.commit()

    res = User.query.get(id).toDict()
    print(res)
    return jsonify(res)

