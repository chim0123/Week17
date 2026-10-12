# Simulated Device Monitoring and Alert System

**Student Name:** Chimreigh G. Caraan
**Student Number:** 2600702
**Section:** 1CPE-A

## Project Description
This program monitors simulated device temperature readings. It classify each reading as NORMAL, WARNING, or CRITICAL and prints a summary with the overall status. It also implement data constraints to manage device errors.

## Features
- View all stored temperature readings
- Add a new reading (whole numbers from 0 to 100 only)
- Classify every reading
- Generate a numerical summary and overall status
- Reject invalid menu choices and invalid readings

## Requirements
- Python 3 (no external packages)

## How to Run
1. Open a terminal inside the Week17 folder.
2. Type: `python device_monitor.py` (On macOS or Linux, type: `python3 device_monitor.py`)

## Sample Output
```text
SIMULATED DEVICE MONITORING SYSTEM
----------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit

Enter choice: 4

MONITORING SUMMARY
------------------
Number of readings  : 5
Total of readings   : 160
Average temperature : 32.00 °C
Minimum temperature : 28 °C
Maximum temperature : 37 °C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED
```

## Test Cases
I performed 10 tests. 10 passed and 0 failed.  
Full details is located in [test_cases.md](test_cases.md).

## Known Limitations
- Stored data are lost when the program closes because file handling or database are not used.

## Reflection
The hardest part of this project is implementing manual loop loops to compute totals and boundaries instead of using built-in function like `min()`. I successfully fixed a boundary bug where a value of 35 goes to CRITICAL instead of WARNING. This exercise help me understand logic design and inputs validation.
