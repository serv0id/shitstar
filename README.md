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
* Run main.py to log in to your account and save the access token
```commandline
python main.py
```

## Usage
Once your account access token has been saved successfully, you are good to go ahead and start using ShitStar for title manifest retrieval.

## Development
Most of the .proto schemas for the Android application can be found in the `proto_raw` dir. PRs that implement additional functionality are welcome.

## ToDo
* Parse search response
* Parse manifest response
* Tidy code
