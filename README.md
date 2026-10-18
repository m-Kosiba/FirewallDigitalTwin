# Firewall Digital Twin

## Project Description
This project is a Python digital twin of a firewall. It simulates how a firewall works by tracking its status, security rules, and network traffic.

## Attributes
- name: The name of the firewall
- location: The location of the firewall
- status: Whether the firewall is on or off
- rules_count: The number of security rules
- blocked_attempts: The number of blocked traffic attempts
- allowed_attempts: The number of allowed traffic attempts

## Methods
- start(): Turns the firewall on
- stop(): Turns the firewall off
- display_status(): Displays the firewall's information
- add_rule(): Adds a security rule
- simulate_traffic(): Simulates network traffic
- reset_counters(): Resets the traffic counters

## How to Run
Run the following command in the terminal:

python firewall_digital_twin.py

## Purpose
This project demonstrates object-oriented programming in Python and shows how a digital twin can simulate a cybersecurity system.
