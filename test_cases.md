# Test Cases – Simulated Device Monitoring and Alert System

Tested by: Chimreigh G. Caraan
Date: October 12, 2026

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Displayed 5 readings correctly | Pass |
| TC02 | Choose 2, enter 33 | Reading added successfully | Reading added successfully | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | Invalid input. Enter a whole number only. | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | Invalid reading. Enter a value from 0 to 100. | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | Invalid reading. Enter a value from 0 to 100. | Pass |
| TC06 | Add 30, then choose 3 | 30 °C -> WARNING | 30 °C -> WARNING | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | 35 °C -> WARNING | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Matches expected outputs exactly | Pass |
| TC09 | Enter 9 | Error message; menu shown again | Invalid choice. Please enter a number from 1 to 5. | Pass |
| TC10 | Choose 5 | Exit message; program ends | Thank you for using the Device Monitoring System. | Pass |

## Bugs Found and Fixed
- **Bug Identified:** During early testing of classification conditions, a boundary error occurred where an execution value of `35` returned `CRITICAL` instead of `WARNING`.
- **Correction Applied:** The evaluation operator inside `classify_reading()` was updated from `<` to `<=` (`elif reading <= 35:`) to ensure correct upper-bound inclusion.
