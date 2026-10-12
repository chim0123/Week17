def get_initial_readings():
    return [28, 31, 35, 37, 29]

def is_whole_number(text):
    if len(text) == 0:
        return False
    start = 0
    if text[0] == "-":
        start = 1
    if start == len(text):
        return False
    for index in range(start, len(text)):
        if text[index] not in "0123456789":
            return False
    return True

def add_reading(readings):
    text = input("Enter new reading: ")
    
    if len(text) == 0:
        print("\nInvalid input. The reading cannot be empty.")
        return
    
    if not is_whole_number(text):
        print("\nInvalid input. Enter a whole number only.")
        return
        
    value = int(text)
    if value < 0 or value > 100:
        print("\nInvalid reading. Enter a value from 0 to 100.")
        return
        
    readings.append(value)
    print("\nReading added successfully.")

def classify_reading(reading):
    if reading < 30:
        return "NORMAL"
    elif reading <= 35:
        return "WARNING"
    else:
        return "CRITICAL"

def display_readings(readings):
    print("\nCURRENT READINGS")
    print("----------------")
    for i in range(len(readings)):
        print(f"Reading {i + 1}: {readings[i]} °C")

def display_classifications(readings):
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for value in readings:
        print(f"{value} °C -> {classify_reading(value)}")

def compute_total(readings):
    total = 0
    for value in readings:
        total += value
    return total

def find_minimum(readings):
    minimum = readings[0]
    for value in readings:
        if value < minimum:
            minimum = value
    return minimum

def find_maximum(readings):
    maximum = readings[0]
    for value in readings:
        if value > maximum:
            maximum = value
    return maximum

def determine_overall_status(warning_count, critical_count):
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"

def display_summary(readings):
    n = len(readings)
    total = compute_total(readings)
    avg = total / n
    minimum = find_minimum(readings)
    maximum = find_maximum(readings)
    
    normal_count = 0
    warning_count = 0
    critical_count = 0
    
    for value in readings:
        category = classify_reading(value)
        if category == "NORMAL":
            normal_count += 1
        elif category == "WARNING":
            warning_count += 1
        elif category == "CRITICAL":
            critical_count += 1
            
    normal_pct = (normal_count / n) * 100
    warning_pct = (warning_count / n) * 100
    critical_pct = (critical_count / n) * 100
    
    status = determine_overall_status(warning_count, critical_count)
    
    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {n}")
    print(f"Total of readings   : {total}")
    print(f"Average temperature : {avg:.2f} °C")
    print(f"Minimum temperature : {minimum} °C")
    print(f"Maximum temperature : {maximum} °C")
    print("")
    print(f"NORMAL   : {normal_count} ({normal_pct:.2f}%)")
    print(f"WARNING  : {warning_count} ({warning_pct:.2f}%)")
    print(f"CRITICAL : {critical_count} ({critical_pct:.2f}%)")
    print("")
    print(f"Overall Status: {status}")

def main():
    readings = get_initial_readings()
    
    while True:
        print("\nSIMULATED DEVICE MONITORING SYSTEM")
        print("----------------------------------")
        print("[1] View Readings")
        print("[2] Add Reading")
        print("[3] Classify Readings")
        print("[4] Generate Summary")
        print("[5] Exit")
        
        choice = input("\nEnter choice: ")
        
        if choice == "1":
            display_readings(readings)
        elif choice == "2":
            add_reading(readings)
        elif choice == "3":
            display_classifications(readings)
        elif choice == "4":
            display_summary(readings)
        elif choice == "5":
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
