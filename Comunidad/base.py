from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///comunidad.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()