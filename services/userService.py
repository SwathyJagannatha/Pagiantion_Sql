from database import db
from models.user import User 
from sqlalchemy import select
from utils.util import encode_token

def login(username,password): #login using unique info so we dont query mutiple users
    query = select(User).where(User.username == username)
    user = db.session.execute(query).scalar_one_or_none()
    #query user table for a customer with password and username

    if user and user.password == password:
        # if e have  a customer associated with username, validate the password
        auth_token = encode_token(user.id,user.role.role_name)

        response = {
            "status": "success",
            "message" : "Successfully Logged In",
            "auth_token" : auth_token
        }
        return response
    
    else:
        response = {
            "status" : "fail",
            "message" : "Invalid username or password"
        }
        return response 
    
    pass

def save(user_data):
    new_user = User(
        name = user_data['name'],
        email  = user_data['email'],
        password = user_data['password'],
        phone = user_data['phone'],
        username = user_data['username'],
    )

    db.session.add(new_user)
    db.session.commit()
    db.session.refresh(new_user)
    return new_user 

def find_all():
    query = select(User)
    all_users = db.session.execute(query).scalars().all()
    return all_users