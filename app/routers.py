from fastapi import APIRouter, HTTPException

from app.contracts import subjects

router = APIRouter()


@router.get("/")
def hello_world():
    """
    Base entry point
    :return: Hello world
    """
    return {"Hello world"}


@router.get("/subjects/get/{name}")
def get_subject_info(name: str):
    f"""
    Get entry point with parameter
    :return: information about {name} subject
    """
    sub = next((subject for subject in subjects if subject["name"] == name), None)
    if sub is None:
        raise HTTPException(status_code=404, detail=f"Subject {name} not found")
    return {
        "Subject information: ",
        f"Name: {sub['name']} ",
        f"Teacher: {sub['teacher']}",
        f"Start date: {sub['start_date']}",
        f"End date: {sub['end_date']}",
    }


@router.get("/subjects/{name}")
def get_info_by_field(name: str, field: str):
    f"""
    Get entry point with query parameter
    :return: {field} information about {name} subject
    """
    print("dfgkhd")
    sub = next((subject for subject in subjects if subject["name"] == name), None)
    if sub is None:
        raise HTTPException(status_code=404, detail=f"Subject {name} not found")
    if field not in sub:
        raise HTTPException(status_code=404, detail=f"There is no field {field}")
    return {f"Your information: {sub[field]}"}
