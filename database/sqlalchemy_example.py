from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

def setup_database():
    engine = create_engine('sqlite:///example.db', echo=True)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)

def add_user(Session, name, age):
    session = Session()
    user = User(name=name, age=age)
    session.add(user)
    session.commit()
    session.close()

def fetch_users(Session):
    session = Session()
    users = session.query(User).all()
    for user in users:
        print(f"{user.name}, {user.age}")
    session.close()

if __name__ == "__main__":
    Session = setup_database()
    add_user(Session, "Alice", 25)
    add_user(Session, "Bob", 30)
    fetch_users(Session)