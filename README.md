# 📝 API REST — Administrador de Tareas (Flask + SQLite)

## 📁 Estructura del proyecto

```
tareas_api/
├── app.py              # Punto de entrada de la aplicación
├── database.py         # Instancia de SQLAlchemy
├── requirements.txt    # Dependencias
├── models/
│   └── tarea.py        # Modelo de la tabla Tareas
└── routes/
    └── tareas.py       # Rutas CRUD del recurso /tareas
```

---

## ⚙️ Instalación y ejecución

### 1. Crear y activar el entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el servidor

```bash
python app.py
```

El servidor correrá en: **http://127.0.0.1:5000**

---

## 🔗 Endpoints disponibles

| Método | Ruta            | Descripción                        |
|--------|-----------------|------------------------------------|
| POST   | /tareas         | Crear una nueva tarea              |
| GET    | /tareas         | Obtener todas las tareas           |
| GET    | /tareas/\<id\>  | Obtener una tarea por ID           |
| PUT    | /tareas/\<id\>  | Actualizar una tarea               |
| DELETE | /tareas/\<id\>  | Eliminar una tarea                 |

---

## 📌 Estados válidos

- `pendiente` (valor por defecto)
- `en_progreso`
- `completada`

---

## 🧪 Ejemplos en Postman

### ✅ Crear tarea — POST /tareas
- **URL:** `http://127.0.0.1:5000/tareas`
- **Headers:** `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
  "titulo": "Estudiar Flask",
  "descripcion": "Repasar blueprints y SQLAlchemy",
  "estado": "pendiente"
}
```

---

### 📋 Obtener todas las tareas — GET /tareas
- **URL:** `http://127.0.0.1:5000/tareas`

**Filtro opcional por estado:**
- `http://127.0.0.1:5000/tareas?estado=pendiente`
- `http://127.0.0.1:5000/tareas?estado=completada`

---

### 🔍 Obtener tarea por ID — GET /tareas/1
- **URL:** `http://127.0.0.1:5000/tareas/1`

---

### ✏️ Actualizar tarea — PUT /tareas/1
- **URL:** `http://127.0.0.1:5000/tareas/1`
- **Headers:** `Content-Type: application/json`
- **Body (raw JSON):**
```json
{
  "estado": "completada"
}
```
> Puedes enviar uno o varios campos: `titulo`, `descripcion`, `estado`.

---

### 🗑️ Eliminar tarea — DELETE /tareas/1
- **URL:** `http://127.0.0.1:5000/tareas/1`

---

## 🗄️ Base de datos

Se usa **SQLite** automáticamente. Al ejecutar `app.py` por primera vez se creará el archivo `tareas.db` en la carpeta del proyecto. No necesitas instalar nada extra.
