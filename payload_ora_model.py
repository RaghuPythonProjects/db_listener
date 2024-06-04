from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class payload_ora_model(Base):
    __tablename__ = 'payload'

    _id = Column(Integer, primary_key=True)  # TODO: make it identity column
    timestamp = Column(DateTime, nullable=False)  # TODO: set to auto populate current time
    payload_received = Column(String, nullable=False)

    def __repr__(self):
        return f"<Payload(_id={self._id}, payload_received='{self.payload_received}', timestamp='{self.timestamp}')>"
    
