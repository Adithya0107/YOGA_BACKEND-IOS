from flask import Blueprint, request, jsonify
from models.yoga_model import create_pose, get_all_poses, save_session_summary

yoga_bp = Blueprint("yoga_bp", __name__)

@yoga_bp.route("/add", methods=["POST"])
def add_pose():
    data = request.json
    create_pose(data["name"], data.get("description", ""), data.get("difficulty", "beginner"))
    return jsonify({"message": "Pose added successfully"})

@yoga_bp.route("/all", methods=["GET"])
def get_poses():
    return jsonify(get_all_poses())

@yoga_bp.route("/save_session", methods=["POST"])
def save_session():
    data = request.json
    user_id = data.get("user_id", 1) # Default to 1 if not provided
    save_session_summary(
        user_id,
        data.get("style_name"),
        data.get("level"),
        data.get("total_duration", 0),
        data.get("actual_duration", 0),
        data.get("completion_percentage", 0.0),
        data.get("status"),
        data.get("calories", 0)
    )
    return jsonify({"message": "Session saved successfully"})
