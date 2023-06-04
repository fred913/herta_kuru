import uvicorn
from webapp import app

uvicorn.run(app, port=5000)
