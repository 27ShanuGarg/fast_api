from app.api_study.models import Study
from app.database import SessionLocal

db = SessionLocal()

class StudyResource:

    def __init__(self):
        pass

    def create_study(self, study_name):

        try:
            
            study_obj = Study(study_name ='History')
            db.add(study_obj)
            db.commit()
            db.refresh(study_obj)

        except Exception as e:
            
            db.rollback()
            raise e

        db.close()
        return study_obj.study_id



    def get_all_study(self):

        try:

            _studies = db.query(Study).all()

        except Exception as e:
            raise e

        db.close()
        return _studies



    def get_study_filter(self, study_name):

        try:

            _studies = db.query(Study).filter(Study.study_name == study_name).all()

        except Exception as e:
            raise e

        db.close()
        return _studies


    def update_study(self, study_name, updated_study_name):

        try:

            study_obj = db.query(Study).filter(Study.study_name == study_name).update(
                {
                    Study.study_name : updated_study_name
                },
                synchronize_session = False)
            
            db.commit()
        except Exception as e:
            raise e

        db.close()
        return study_obj


    def delete_study(self, study_name):

        try:

            _studies = db.query(Study).filter(Study.study_name == study_name).delete()

        except Exception as e:
            raise e

        db.close()
        return _studies