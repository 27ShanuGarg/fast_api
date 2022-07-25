# from app import db, log
from app.helper.Constants import Constants
from sqlalchemy import Column, String, Integer, ForeignKey, Numeric, Date,Boolean, DateTime, BLANK_SCHEMA, func
from sqlalchemy.dialects.mysql import MEDIUMINT, TINYINT, SMALLINT
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

# Define a base model for other database tables to inherit
class Base(Base):

    __abstract__  = True
    __bind_key__ = 'university'

    created_by = Column(String(100), nullable=True)
    updated_by = Column(String(100), nullable=True)
    created_at = Column(DateTime,  default=func.current_timestamp(), nullable=True)
    updated_at = Column(DateTime, nullable=True)
     
class User(Base):

    __tablename__ = Constants.tbl_user
    # __table_args__ = {Constants.ORM_ExtendExisting: True}
    user_id     = Column(SMALLINT(6), primary_key=True, nullable=False, autoincrement=True)
    user_name   = Column(String(100), nullable=False)