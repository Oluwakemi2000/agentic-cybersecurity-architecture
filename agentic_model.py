# agentic_model.py

class AgenticSecurityAgent:
    def __init__(self):
        self.memory = []
        self.trust_threshold = 0.8

    def sense(self, input_data):
        print("Collecting telemetry...")
        return {"anomaly_score": 0.9, "source": "API-Gateway"}

    def reflect(self, data):
        print("Reflecting on context...")
        if data["anomaly_score"] > self.trust_threshold:
            return "High Threat"
        return "Normal"

    def act(self, decision):
        print(f"Taking action based on decision: {decision}")
        if decision == "High Threat":
            return "Initiate containment"
        return "Allow flow"

if __name__ == "__main__":
    agent = AgenticSecurityAgent()
    data = agent.sense(None)
    decision = agent.reflect(data)
    action = agent.act(decision)
    print(f"Response: {action}")
