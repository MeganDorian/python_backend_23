from sqlalchemy.orm import Session

from homework.models.models import User, Subject


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Get all registered users from db
    """
    return db.query(User).offset(skip).limit(limit).all()


def get_user_subjects(db: Session, user_id: int):
    """
    Get all subjects that user attends from sb
    :return None if there is no user with provided id and empty list if the user doesn't attend any subject
    """
    user = db.query(User).filter(User.id == user_id).first()
    if user is not None:
        subjects = [get_subject(db, user_sub.id_subject) for user_sub in user.subjects]
        return subjects


def get_subject(db: Session, subject_id: int):
    """
    Get subject by id from db
    """
    return db.query(Subject).filter(Subject.id == subject_id).first()


def get_homeworks(db: Session, subject_id: int):
    """
    Get all homeworks of selected subject
    """
    return get_subject(db, subject_id).hws
