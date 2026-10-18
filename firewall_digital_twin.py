class Firewall:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.status = "Off"
        self.rules_count = 3
        self.blocked_attempts = 0
        self.allowed_attempts = 0

    def start(self):
        self.status = "On"
        print(self.name, "has been turned on.")

    def stop(self):
        self.status = "Off"
        print(self.name, "has been turned off.")

    def display_status(self):
        print("\n--- Firewall Status ---")
        print("Name:", self.name)
        print("Location:", self.location)
        print("Status:", self.status)
        print("Security Rules:", self.rules_count)
        print("Blocked Attempts:", self.blocked_attempts)
        print("Allowed Attempts:", self.allowed_attempts)

    def add_rule(self):
        self.rules_count += 1
        print("A security rule has been added.")

    def simulate_traffic(self, safe):
        if self.status == "Off":
            print("Warning: Firewall is off!")
        elif safe:
            self.allowed_attempts += 1
            print("Safe traffic allowed.")
        else:
            self.blocked_attempts += 1
            print("Suspicious traffic blocked.")

    def reset_counters(self):
        self.blocked_attempts = 0
        self.allowed_attempts = 0
        print("Traffic counters have been reset.")


# Create a digital twin object
my_firewall = Firewall("Campus Firewall", "University Network")

# Demonstrate each method
my_firewall.display_status()
my_firewall.start()
my_firewall.add_rule()
my_firewall.simulate_traffic(True)
my_firewall.simulate_traffic(False)
my_firewall.display_status()
my_firewall.reset_counters()
my_firewall.stop()
my_firewall.display_status()
