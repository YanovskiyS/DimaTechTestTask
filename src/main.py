from fastapi import FastAPI
import uvicorn

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.api.auth import router as router_auth
from src.api.users import router as router_users
from src.api.transactions import router as router_trans
from src.api.accounts import router as router_accounts

app = FastAPI()

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_trans)
app.include_router(router_accounts)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

