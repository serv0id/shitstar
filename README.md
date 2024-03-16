# ShitStar
Client for Hotstar/Disney+ MENA based on Android Mobile endpoints.

## Setup
* Clone the repo
```commandline
git clone https://github.com/serv0id/shitstar.git
```
* Install the requirements
```commandline
pip install -r requirements.txt
```
* Create a credential file (creds.py) with the following content:
```python
PHONE_NUMBER = "PHONE NUMBER LINKED TO ACCOUNT"
```
* Run main.py
```commandline
python main.py
```

## ToDo
* ~~Bypass any app protections (SSL pinning, root, etc.) - **_App seems to have SSL Pinning_**~~
* ~~Sniff login calls~~
* ~~Everything is protobuf~~
* ~~Implement OTP/Cookie system~~
* Implement a search API if needed
* Implement licensing