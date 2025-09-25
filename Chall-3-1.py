mission_objectives = ["Secure the server", "Extract the data", "Deploy failsafe"]
mission_objectives[1] = "Copy sensitive files"
mission_objectives.append("Infiltrate the facility")
mission_objectives.insert(0, "Disable security cameras")
del mission_objectives[1]
print(mission_objectives)
