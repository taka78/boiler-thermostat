#Boiler Thermostat - Home Assistant Custom Integration

This repository contains a custom component for Home Assistant that allows you to integrate your boiler thermostat with the Home Assistant system. The solution is designed for a Raspberry Pi 3B as the main computing device running the Home Assistant container.

Hardware Requirements:

Raspberry Pi 3B
5V-220V Relay Module
DS18B20 Thermistor with 10kΩ Resistor
Features:

Read current boiler temperature using the DS18B20 thermistor.
Set target temperature for the boiler and control it using the relay module (requires a script to handle the logic).
Requirements:

Home Assistant
Python 3
Installation:

Clone this repository into your Home Assistant custom components directory:

Bash

cd <config directory>/custom_components
git clone https://github.com/taka78/boiler-thermostat.git

Restart Home Assistant.

Configuration:

Create a file named thermostat_script.py in the boiler-thermostat directory. This script should contain functions to:

read_temp(): This function should read the temperature from the DS18B20 sensor using the DallasTemperature library (replace with your implementation).
set_target_temp(target_temp): This function should activate the relay module based on the target temperature and current temperature reading (replace with your implementation). You'll likely need to use a library like RPi.GPIO to control the GPIO pins connected to the relay.
In your Home Assistant configuration (configuration.yaml), add the following under the climate section:

YAML

climate:
  - platform: boiler_thermostat

Notes:

This integration relies on a separate script (thermostat_script.py) to interact with your specific boiler hardware. You'll need to implement the logic for reading temperature using the DS18B20 sensor and controlling the relay module based on target temperature.
Ensure proper error handling in your script to handle cases where temperature reading or relay control fails.
Consider using asynchronous functions in your script for potentially improved responsiveness.
Additional Information:

The provided hardware list assumes a basic setup for boiler temperature control. You might need additional components depending on your specific boiler and desired functionalities.
Remember to install the required libraries (DallasTemperature and potentially RPi.GPIO) within your Home Assistant container for the script to function correctly.
Contributing:

Feel free to submit pull requests for improvements or bug fixes.

License:

This project is licensed under the MIT License. See the LICENSE file for details.
