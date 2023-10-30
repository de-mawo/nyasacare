from flask import request, jsonify
import uuid
from app.extensions import db
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


def create_user():
    req_form = request.form.to_dict()

    # print(req_form)

    id = str(uuid.uuid4())
    new_user = User(
        id=id,
        name=req_form['name'],
        email=req_form['email'],
        phone=req_form['phone'],
        lastname=req_form['lastname'],
        profile_img=req_form['profile_img'],
        password=req_form['password'],
    )

    db.session.add(new_user)
    db.session.commit()

    res = User.query.get(id).toDict()
    return jsonify(res)
