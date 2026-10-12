def get_initial_readings():
    return [24, 32, 35, 41, 28]

def verify_integer_format(user_input):
    if len(user_input) == 0:
        return False
    
    index_offset = 0
    if user_input[0] == "-":
        index_offset = 1
        
    if index_offset == len(user_input):
        return False
        
    for position in range(index_offset, len(user_input)):
        if user_input[position] not in "0123456789":
            return False
    return True

def add_reading(readings):
    raw_text = input("Enter new reading: ")
    
    if len(raw_text) == 0:
        print("\nInvalid input. The reading cannot be empty.")
        return
        
    if not verify_integer_format(raw_text):
        print("\nInvalid input. Enter a whole number only.")
        return
        
    numeric_value = int(raw_text)
    if numeric_value < 0 or numeric_value > 100:
        print("\nInvalid reading. Enter a value from 0 to 100.")
        return
        
    readings.append(numeric_value)
    print("\nReading added successfully.")

def check_traffic_tier(metric):
    if metric < 30:
        return "NORMAL"
    elif metric <= 35:
        return "WARNING"
    else:
        return "CRITICAL"

def list_stored_metrics(readings):
    print("\nCURRENT READINGS")
    print("----------------")
    for position in range(len(readings)):
        print(f"Reading {position + 1}: {readings[position]} Mbps")

def process_and_list_classes(readings):
    print("\nREADING CLASSIFICATION")
    print("----------------------")
    for load in readings:
        assigned_tier = check_traffic_tier(load)
        print(f"{load} Mbps -> {assigned_tier}")

def sum_array_elements(readings):
    running_total = 0
    for value in readings:
        running_total += value
    return running_total

def extract_lowest_bound(readings):
    lowest_marker = readings[0]
    for value in readings:
        if value < lowest_marker:
            lowest_marker = value
    return lowest_marker

def extract_highest_bound(readings):
    highest_marker = readings[0]
    for value in readings:
        if value > highest_marker:
            highest_marker = value
    return highest_marker

def compile_alert_status(warn_total, crit_total):
    if crit_total >= 1:
        return "ATTENTION REQUIRED"
    elif warn_total >= 1:
        return "MONITOR"
    else:
        return "NORMAL"

def generate_analytics_report(readings):
    total_records = len(readings)
    summed_val = sum_array_elements(readings)
    calculated_mean = summed_val / total_records
    floor_limit = extract_lowest_bound(readings)
    ceil_limit = extract_highest_bound(readings)
    
    tally_norm = 0
    tally_warn = 0
    tally_crit = 0
    
    for reading in readings:
        tier = check_traffic_tier(reading)
        if tier == "NORMAL":
            tally_norm += 1
        elif tier == "WARNING":
            tally_warn += 1
        elif tier == "CRITICAL":
            tally_crit += 1
            
    pct_norm = (tally_norm / total_records) * 100
    pct_warn = (tally_warn / total_records) * 100
    pct_crit = (tally_crit / total_records) * 100
    
    system_health = compile_alert_status(tally_warn, tally_crit)
    
    print("\nMONITORING SUMMARY")
    print("------------------")
    print(f"Number of readings  : {total_records}")
    print(f"Total of readings   : {summed_val}")
    print(f"Average bandwidth   : {calculated_mean:.2f} Mbps")
    print(f"Minimum bandwidth   : {floor_limit} Mbps")
    print(f"Maximum bandwidth   : {ceil_limit} Mbps")
    print("")
    print(f"NORMAL   : {tally_norm} ({pct_norm:.2f}%)")
    print(f"WARNING  : {tally_warn} ({pct_warn:.2f}%)")
    print(f"CRITICAL : {tally_crit} ({pct_crit:.2f}%)")
    print("")
    print(f"Overall Status: {system_health}")

def main():
    historical_logs = get_initial_readings()
    
    while True:
        print("\nSIMULATED DEVICE MONITORING SYSTEM")
        print("----------------------------------")
        print(" View Readings")
        print(" Add Reading")
        print(" Classify Readings")
        print(" Generate Summary")
        print(" Exit")
        
        selection = input("\nEnter choice: ")
        
        if selection == "1":
            list_stored_metrics(historical_logs)
        elif selection == "2":
            add_reading(historical_logs)
        elif selection == "3":
            process_and_list_classes(historical_logs)
        elif selection == "4":
            generate_analytics_report(historical_logs)
        elif selection == "5":
            print("\nThank you for using the Device Monitoring System.")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main() 
