import sqlalchemy as db
import persistence.model as mod
from forms.master.form_inicio import MasterPanel

#Activa base de datos
engine = db.create_engine('sqlite:///db/login.sqlite', echo=True, future=True)
mod.Base.metadata.create_all(engine)

MasterPanel()