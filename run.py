from app import app, db 
from app.blueprints.auth.models import User 
# from app.blueprints.shop 

@app.shell_context_processor 
def make_context():
    return {'db':db, 'User':User}