import base64

with open("D:/telegram_sessions/pro_session.session", "rb") as f:
    encoded = base64.b64encode(f.read()).decode()

with open("session_b64.txt", "w") as f:
    f.write(encoded)

print("DONE - saved in session_b64.txt")
