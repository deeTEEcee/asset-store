from core.app import app
import os

os.environ["CONFIG"] = "config.dev"
app.run(debug=True)
