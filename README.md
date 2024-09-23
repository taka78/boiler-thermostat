<h1>Boiler Thermostat - Home Assistant Custom Integration</h1>

<p>This repository contains a custom component for Home Assistant that integrates your boiler thermostat with the Home Assistant system. It's designed for use with a Raspberry Pi 3B running Home Assistant in a container.</p>

<h2>Hardware Requirements</h2>
<ul>
  <li>Raspberry Pi 3B</li>
  <li>5V-220V Relay Module</li>
  <li>DS18B20 Thermistor with 10kΩ Resistor</li>
</ul>

<h2>Features</h2>
<ul>
  <li>Read current boiler temperature using the DS18B20 thermistor.</li>
  <li>Set target temperature for the boiler and control it using the relay module (requires a script to handle the logic).</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Home Assistant</li>
  <li>Python 3</li>
</ul>

<h2>Installation</h2>
<p>Clone this repository into your Home Assistant <code>custom_components</code> directory:</p>

<pre><code>cd &lt;config directory&gt;/custom_components
git clone https://github.com/taka78/boiler-thermostat.git
</code></pre>

<p>Then restart Home Assistant.</p>

<h2>Configuration</h2>
<p>Create a file named <code>thermostat_script.py</code> in the <code>boiler-thermostat</code> directory. This script should include the following functions:</p>

<ul>
  <li><code>read_temp()</code>: Reads the temperature from the DS18B20 sensor using a library like DallasTemperature (or your implementation).</li>
  <li><code>set_target_temp(target_temp)</code>: Activates the relay module based on the target and current temperature readings (replace with your implementation). A library like <code>RPi.GPIO</code> is recommended for controlling the GPIO pins connected to the relay.</li>
</ul>

<p>Next, add the following to your Home Assistant <code>configuration.yaml</code> file:</p>

<pre><code>climate:
  - platform: boiler_thermostat
</code></pre>

<h2>Notes</h2>
<ul>
  <li>This integration relies on a separate script (<code>thermostat_script.py</code>) to interact with your boiler hardware.</li>
  <li>Implement the logic for reading the DS18B20 sensor temperature and controlling the relay module.</li>
  <li>Ensure proper error handling for temperature readings and relay control failures.</li>
  <li>Consider using asynchronous functions for better responsiveness.</li>
</ul>

<h2>Additional Information</h2>
<p>The provided hardware list assumes a basic setup for boiler temperature control. Depending on your specific boiler and functionalities, you might need additional components.</p>
<p>Ensure the required libraries (e.g., <code>DallasTemperature</code> and <code>RPi.GPIO</code>) are installed within the Home Assistant container for the script to function correctly.</p>

<h2>Contributing</h2>
<p>Feel free to submit pull requests for improvements or bug fixes.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for details.</p>
