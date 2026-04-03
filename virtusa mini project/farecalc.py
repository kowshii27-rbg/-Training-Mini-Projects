import sys

PRICING_TIERS = {
    "economy": 10.0,
    "premium": 18.0,
    "suv": 25.0
}

def get_valid_input(prompt_text, cast_type, error_msg):
    while True:
        try:
            return cast_type(input(prompt_text).strip())
        except ValueError:
            print(error_msg)

def get_surge_multiplier(hour_of_day):
    return 1.5 if 17 <= hour_of_day <= 20 else 1.0

def generate_trip_summary(distance, car_class, hour_of_day):
    car_key = car_class.lower()
    if car_key not in PRICING_TIERS:
        return None

    rate = PRICING_TIERS[car_key]
    base_cost = distance * rate
    surge = get_surge_multiplier(hour_of_day)
    total_cost = base_cost * surge


    return {
        "Distance": f"{distance:.2f} km",
        "Vehicle Type": car_key.capitalize(),
        "Base Fare": f"{base_cost:.2f} Rupees",
        "Surge Pricing": f"{'Yes' if surge > 1.0 else 'No'} (x{surge})",
        "Final Price": f"{total_cost:.2f} Rupees"
    }

def main():
    print("--- Urban Ride Fare Estimator ---")

    dist = get_valid_input(
        "Enter travel distance (km): ", 
        float, 
        "Invalid input. Please provide a numeric distance."
    )
    if dist < 0:
        sys.exit("Error: Distance cannot be negative.")

    time_of_day = get_valid_input(
        "Enter the time of day (0-23 hours): ", 
        int, 
        "Invalid input. Please provide a whole number."
    )
    if not (0 <= time_of_day <= 23):
        sys.exit("Error: Time must be between 0 and 23.")

    car_selection = input("Select a vehicle category (Economy/Premium/SUV): ").strip()

    receipt_data = generate_trip_summary(dist, car_selection, time_of_day)

    if not receipt_data:
        sys.exit("Error: Service Not Available.")
    print("\n" + "="*35)
    print("RIDE RECEIPT")
    print("="*35)
    for key, value in receipt_data.items():
        print(f"{key:<15}: {value}")
    print("="*35)


if __name__ == "__main__":
    main()