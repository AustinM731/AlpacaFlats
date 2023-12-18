# Alpaca Flats

## Description
Alpaca Flats is an ASCOM Alpaca driver designed to control a Cover Calibrator Device using a Raspberry Pi. This driver enables any ASCOM Alpaca compatible client to interact with the device, generating a PWM signal on Pin 12 of the Raspberry Pi's GPIO header to control the intensity of an LED tracing panel.

## Features
- **ASCOM Alpaca Compatibility**: Fully compatible with the ASCOM Alpaca standard, facilitating broad interoperability with various astronomy software.
- **PWM Signal Control**: Utilizes the GPIO header of a Raspberry Pi to modulate the intensity of an LED tracing panel through PWM signaling.
- **Customizable LED Intensity**: Offers adjustable brightness settings to cater to different observational needs and environments.

## Prerequisites
- A Raspberry Pi (Model 3B or newer recommended) with Raspberry Pi OS (Bookworm) installed. Ubuntu or other linux distributions may work, but have not been tested.
- Basic understanding of the Raspberry Pi GPIO.
- An ASCOM Alpaca compatible client software.

## Installation

Download/Copy and run the installation script, which will automatically clone the Alpaca Flats repository to the correct location and set up the necessary environment:

```bash
# Ensure the script is executable
chmod +x install_script.sh

# Execute the script (requires sudo privileges)
sudo ./install_script.sh
```
## Usage
### General Usage
1. Run the installation script to install the Alpaca Flats driver and its dependencies. This will also create a systemd service to automatically start the driver on boot. To check the status of the service, run the command below.
```bash
sudo systemctl status alpacaflats.service
```
2. Find the IP address of the Raspberry Pi on the local network by running the command below on the Raspberry Pi.
Depending on your network configuration, the IP address may be listed under the "eth0" or "wlan0" interface. The IP address will be listed under the "inet" field, and will be in the format "xxx.xxx.xxx.xxx".
```bash
ip a
```
## Advanced Usage
- **Application Entry Point**: To manually run the application execute app.py to start the Alpaca Flats application. This script is the main entry point and requires Python 3.7 or later.

- **Configuring the Application**: Edit the config.toml file to customize your installation settings, such as network parameters, server details, device settings, and logging preferences. By default, the application will bind to whatever IP address is assigned to the Raspberry Pi on the local network, and will listen on port 5555.

- **Understanding the Hardware Logic**: The calibratordevice.py file manages the brightness, calibrator state, and cover state of the LED panel, and handles the PWM signals on the Raspberry Pi's GPIO.

- **Adding New Device Features**: The calibratordevice.py file can be modified to add new features to the device, such as a motorized cover, the API endpoints for which already exist in the Alpaca Flats driver.

- **API and Device Interaction**: The covercalibrator.py file handles Alpaca API responses and is key to the interaction between the Alpaca Flats driver and ASCOM Alpaca clients.

## Contributing
Contributions to Alpaca Flats are welcome! Please fork the repository, make your changes, and submit a pull request for review.