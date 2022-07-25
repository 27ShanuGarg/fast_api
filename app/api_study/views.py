# from app import FastAPI
from fastapi import APIRouter
from app.api_study.resources.Study import StudyResource
study_router = APIRouter()

from pydantic import BaseModel


class Item(BaseModel):
    study_name: str
    updated_study_name: str | None = None


class Study:

    @study_router.get("/study/", tags=["study"])
    async def read_study():
        response = StudyResource().get_all_study()
        return response


    @study_router.post("/study/", tags=["study"])
    async def create_study(item : Item):
        item_dict   = item.dict()
        study_name  = item_dict['study_name']
        response = StudyResource().create_study(study_name)
        return response


    @study_router.post("/study/filter", tags=["study"])
    async def read_study_filter(item : Item):
        item_dict   = item.dict()
        study_name  = item_dict['study_name']
        response = StudyResource().get_study_filter(study_name)
        return response



    @study_router.put("/study/", tags=["study"])
    async def update_study(item : Item):
        item_dict   = item.dict()
        study_name  = item_dict['study_name']
        updated_study_name  = item_dict['updated_study_name']
        response = StudyResource().update_study(study_name, updated_study_name)
        return response



    @study_router.delete("/study/", tags=["study"])
    async def delete_study(item : Item):
        item_dict   = item.dict()
        study_name  = item_dict['study_name']
        response = StudyResource().delete_study(study_name)
        return response

