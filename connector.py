from flask import Flask, jsonify, request
import uuid
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.user_loginsystem


class User:
    def signup(self):

        print(user.form)

        user = {
            "id": uuid.uuid4().hex,
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'password': request.form.get('password')

        }
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "email address already in use"}), 400
        return jsonify(user), 200

    db.users.insert_one(user)
