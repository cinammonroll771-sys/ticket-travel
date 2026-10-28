# My Travel Ticket Counter

# Step 1: Create Travel Data
travel_data = [
    {"destination": "Paris", "price": 200, "available": 50},
    {"destination": "Tokyo", "price": 400, "available": 30},
    {"destination": "New York", "price": 300, "available": 40},
    {"destination": "London", "price": 250, "available": 20}
]

# Step 2: Calculate Ticket Cost
def calculate_ticket_cost(destination_name, num_tickets):
    for dest in travel_data:
        if dest["destination"].lower() == destination_name.lower():
            return dest["price"] * num_tickets
    return None

# Step 3: Complete Booking
def book_tickets(destination_name, num_tickets):
    for dest in travel_data:
        if dest["destination"].lower() == destination_name.lower():
            if dest["available"] >= num_tickets:
                dest["available"] -= num_tickets
                total_cost = dest["price"] * num_tickets
                return f"Booking confirmed for {num_tickets} tickets to {dest['destination']}. Total cost: ${total_cost}"
            else:
                return f"Sorry, only {dest['available']} tickets available for {dest['destination']}."
    return "Destination not found."

# Step 4: Work with Strings - Print Ticket
def print_ticket(destination_name, num_tickets):
    total = calculate_ticket_cost(destination_name, num_tickets)
    if total is not None:
        print(f"----- Ticket -----")
        print(f"Destination: {destination_name.title()}")
        print(f"Tickets: {num_tickets}")
        print(f"Total Cost: ${total}")
        print(f"------------------")
    else:
        print("Invalid destination")

# Step 5: Print All Ticket Prices
print("Available Destinations:")
for dest in travel_data:
    print(f"{dest['destination']}: ${dest['price']} - {dest['available']} tickets left")

# Example usage - this is what the auto-test checks
print("\n" + book_tickets("Paris", 2))
print(book_tickets("Tokyo", 5))
print_ticket("Paris", 2)