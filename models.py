```python
from sqlalchemy import Column, Integer, String
from database import Base

class CV(Base):
    __tablename__ = "cvs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    label = Column(String)
    location = Column(String)
    email = Column(String)
    phone = Column(String)
    website = Column(String)
```