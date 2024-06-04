from sqlalchemy import Column, Integer, String, DateTime, func, Identity
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PayloadOraModel(Base):
    __tablename__ = 'payload'

    _id = Column(Integer, Identity(start=1, cycle=True), primary_key=True)
    timestamp = Column(DateTime, default=func.now(), nullable=False)
    payload_received = Column(String, nullable=False)

    def __repr__(self):
        return f"<Payload(_id={self._id}, payload_received='{self.payload_received}', timestamp='{self.timestamp}')>"
