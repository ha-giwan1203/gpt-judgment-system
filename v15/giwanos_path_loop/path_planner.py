# path_planner.py
import sys
import os
sys.path.append(os.path.dirname(__file__))
from intent_parser import parse_intent
import json

def plan_execution_path(user_input, catalog_path=os.path.join(os.path.dirname(__file__), "loop_catalog.json")):
    intent = parse_intent(user_input)
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    route = []
    if intent["include_judgement"]:
        route.append("judgement_loop")
    if intent["include_reflection"]:
        route.append("reflection_loop")
    if intent["include_report"]:
        route.append("report_loop")
    if intent["include_sorting"]:
        route.append("sort_loop")

    readable_route = [f"{loop} ({catalog.get(loop, '-')})" for loop in route]
    return route, readable_route
