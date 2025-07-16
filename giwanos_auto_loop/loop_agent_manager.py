import json
from pathlib import Path

PROFILE_PATH = Path("logs/user_profiles.json")
AGENT_ASSIGNMENTS = Path("logs/loop_agent_routes.json")

def assign_agent_loops(agent_id):
    profiles = json.load(open(PROFILE_PATH, encoding="utf-8")) if PROFILE_PATH.exists() else {}
    assignments = json.load(open(AGENT_ASSIGNMENTS, encoding="utf-8")) if AGENT_ASSIGNMENTS.exists() else {}

    profile = profiles.get(agent_id, {"role": "guest"})
    role = profile.get("role", "guest")
    assigned = assignments.get(role, [])

    return {
        "agent": agent_id,
        "role": role,
        "assigned_loops": assigned
    }

if __name__ == "__main__":
    result = assign_agent_loops("지니")
    print(result)