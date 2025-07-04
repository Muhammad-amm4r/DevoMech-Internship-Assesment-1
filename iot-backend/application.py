import os
from app.main import app as application

# For AWS Elastic Beanstalk
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    import uvicorn
    uvicorn.run("application:application", host="0.0.0.0", port=port, reload=False) 