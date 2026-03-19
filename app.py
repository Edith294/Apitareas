from flask import Flask
from database import db
from routes.tareas import tareas_bp

app = Flask(__name__)

# Configuración de la base de datos SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos
db.init_app(app)

# Registrar blueprint de tareas
app.register_blueprint(tareas_bp)

# Crear tablas si no existen
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
