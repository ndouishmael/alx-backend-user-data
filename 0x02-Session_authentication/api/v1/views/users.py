#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User

# ... (your existing imports and code)

@app_views.route('/users/me', methods=['GET'], strict_slashes=False)
def view_authenticated_user() -> str:
    """ GET /api/v1/users/me
    Return:
      - Authenticated User object JSON represented
      - 404 if no authenticated user
    """
    if request.current_user is None:
        abort(404)
    return jsonify(request.current_user.to_json())
