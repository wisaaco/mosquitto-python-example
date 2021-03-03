
Minor example using [MQTT](http://en.wikipedia.org/wiki/Mqtt) and Python.
forked project


## Requirements
#### Plan A. 
Using test server: https://test.mosquitto.org/

#### Plan B. 
Requires [Mosquitto](http://mosquitto.org/) to be installed.

On Linux/Ubuntu with the **apt-get** package manager:

    sudo apt-get install mosquitto
    sudo apt-get install mosquitto-clients
    sudo service mosquitto start


## Setup
Simply clone this repo, setup virtualenv and use pip to install requirements.

    git clone https://github.com/wisaaco/mosquitto-python-example
    cd mqtt-mosquitto-example
    pip install -r requirements.txt

## Test the subscriber example
First start the subscriber which will enter a loop waiting for new messages:

    python3 subscriber.py

(Only with PlanB) Then open a new terminal and send a message:

    mosquitto_pub -d -h localhost -q 0 -t perros/pics -m "Bonito cachorrito de perro maltes"

This should generate a message in the terminal running the subscriber.

Take a look at **publisher.py** to see how to publish messages using python. Or just open another terminal and run it from command line while **subscriber.py** is running:

    python3 publisher.py


## References
 * https://github.com/roppert/mosquitto-python-example
 * http://jpmens.net/2013/02/25/lots-of-messages-mqtt-pub-sub-and-the-mosquitto-broker/
 * https://www.justinribeiro.com/chronicle/2012/11/08/securing-mqtt-communication-between-ardruino-and-mosquitto/
 * http://www.instructables.com/id/USB-RFID-Python-Pub-Sub-MQTT/
 * http://mosquitto.org/documentation/python/
 * https://pypi.python.org/pypi/paho-mqtt


