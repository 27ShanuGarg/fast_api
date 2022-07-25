from fastapi import FastAPI
from .api_study import views as view_study
from .api_user  import views as view_user
from .database import engine

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


# Including Routers
app.include_router(view_study.study_router)
app.include_router(view_user.user_router)


#models creation
from .api_study.models import Study
from .api_user.models import User

Study.metadata.create_all(bind=engine)
User.metadata.create_all(bind=engine)

