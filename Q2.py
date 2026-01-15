import streamlit as st
import json

with open("json_q2.txt") as f:
    rules = json.load(f)

st.title("Smart Home Air Conditioner Controller")

temperature = 22
humidity = 46
occupancy = "OCCUPIED"
time_of_day = "NIGHT"
windows_open = False

facts = {
    "temperature": temperature,
    "humidity": humidity,
    "occupancy": occupancy,
    "time_of_day": time_of_day,
    "windows_open": windows_open
}

def check_condition(condition, facts):
    key, op, value = condition
    if op == "==": return facts[key] == value
    if op == ">=": return facts[key] >= value
    if op == "<=": return facts[key] <= value
    if op == "<": return facts[key] < value

valid_rules = []
for rule in rules:
    if all(check_condition(c, facts) for c in rule["conditions"]):
        valid_rules.append(rule)

selected = max(valid_rules, key=lambda r: r["priority"])

st.subheader("Selected Rule")
st.write(selected["name"])
st.json(selected["action"])
