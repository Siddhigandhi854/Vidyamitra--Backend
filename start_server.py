#!/usr/bin/env python3
import sys
import os

# Add the backend directory to Python path
sys.path.insert(0, '/opt/render/project/src/backend')

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
