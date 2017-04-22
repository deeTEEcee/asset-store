### Requirements
- Python 2.7
- Need to support requirements.txt
- Must run from the asset-store folder # `cd asset-store`

### (Optional) Use this guide to setup the virtual environment or manually do it yourself
1. Install virtualenv on your machine.
2. `virtualenv venv`
3. cd into main folder: `source venv bin/activate`
4. `pip install -r requirements.txt`

You can now run the server basic requirements and tests.

### Running the Server
```
install basic python needs
python setup.py
python run.py
```
#####Available Routes
- GET /assets
- GET /asset/\<asset_name\> 
- POST /asset/\<asset_name\>


### Testing
```
python tests.py
```
