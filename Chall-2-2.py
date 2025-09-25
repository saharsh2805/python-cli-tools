agent_level=8
if(agent_level>=10):
    print("Full administrative access")
elif(agent_level>=7):
    print("Access to classified files")
elif(agent_level>=5):
    print("Access to general records")
else:
    print("Acess denied")

