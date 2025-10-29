from app import create_app
from app.extensions import db
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

# crea la aplicacion Flask
app = create_app()

# verifica la conexion a la base de datos
def check_db_connection(app):
    with app.app_context():
        try:
            db.session.execute(text("SELECT 1"))
            print("Conexión a la base de datos exitosa.")
        except OperationalError as e:
            print("Error al conectar a la base de datos:", e)

# ejecutar la aplicacion
if __name__ == '__main__':
    check_db_connection(app)
    app.run(port = app.config['PORT'])
