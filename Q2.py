import streamlit as st

def decide(temp, humidity, occ, time, windows):
    if windows:
        return "OFF", "LOW", "-", "Windows open"
    if temp <= 22:
        return "OFF", "LOW", "-", "Already cold"
    if occ == "EMPTY" and temp >= 24:
        return "ECO", "LOW", "27°C", "Home empty"
    if occ == "OCCUPIED" and time == "NIGHT" and temp >= 26:
        return "SLEEP", "LOW", "26°C", "Night comfort"
    if occ == "OCCUPIED" and temp >= 30 and humidity >= 70:
        return "COOL", "HIGH", "23°C", "Hot and humid"
    if occ == "OCCUPIED" and temp >= 28:
        return "COOL", "MEDIUM", "24°C", "Hot"
    if occ == "OCCUPIED" and 26 <= temp < 28:
        return "COOL", "LOW", "25°C", "Slightly warm"

st.title("Smart AC Rule-Based Controller")
mode, fan, setp, reason = decide(22, 46, "OCCUPIED", "NIGHT", False)
st.write(mode, fan, setp, reason)
