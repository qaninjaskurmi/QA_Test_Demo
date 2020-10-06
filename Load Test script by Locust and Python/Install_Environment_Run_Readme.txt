Load Test Using by Locust:
----------------------------
-Install Python 3.6 or later.

-Install Locust using pip.

Open command prompt
$ pip3 install locust
Validate your installation and show the Locust version number:

$ locust -V

-How to install or if any troubleshoot needs details:: 
https://docs.locust.io/en/stable/installation.html

How to run locust:
-------------------
Locust file must be saved with .py (A new pycharm project created where, open the Locust file at that pycharm) 
Example: locustfile.py

Open windows power shell in the same file where ocust file saved (Shift +Right click at windows)
Call Locust, type the Host url where you want to Call the load test:

For me here:
locust --host=http://localhost:9999/statements
 
Open browesr and Go:
http://localhost:8089/

Input Three more data for load test here:

-Start new load test
-----------------------
At locust in Browser:
Number of total users to simulate: 1000

Spawn rate : 10
(users spawned/second)

Host : http://localhost:8089/
(e.g. http://www.example.com)

Then click "Start Swarming"
It will start auto the Test: 
It will how the failures, exceptions, chart view, and report results also in different tab

