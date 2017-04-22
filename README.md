### Requirements
- Python 2.7
- Need to support requirements.txt
- Must run from the asset-store folder # `cd asset-store`

### (Optional) Use this guide to setup the virtual environment or manually do it yourself
1. Install virtualenv on your machine.
2. cd into main asset-store folder
3. `virtualenv venv`
4. `source venv bin/activate`
4. `pip install -r requirements.txt`

You can now run the server basic requirements and tests.

### Running the Server
```
# after the requirements are met and python in venv activated
python db_init.py
python run.py
```
##### Available Routes and Sample Requests
- GET /api/v1/assets
  - Sample: `curl http://127.0.0.1:5000/api/v1/assets`
- GET /api/v1/asset/\<asset_name\>
  - Sample: `curl http://127.0.0.1:5000/api/v1/asset/alpha-dove`
- POST /api/v1/asset/\<asset_name\>
  - Sample: `curl --data "type=satellite&class=dove" http://127.0.0.1:5000/api/v1/asset/alpha-dove`

### Testing
```
python tests.py
```
