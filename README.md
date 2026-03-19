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
## ⚙️Capturas de pantalla
<img width="1919" height="1075" alt="Captura de pantalla 2026-03-19 130259" src="https://github.com/user-attachments/assets/9dce64bb-50f3-483b-a51c-a2e6c6a0cca6" />
<img width="1919" height="1079" alt="Captura de pantalla 2026-03-19 130408" src="https://github.com/user-attachments/assets/e141a10f-bd9b-42b7-9a3d-f5a36a777cad" />
<img width="1919" height="1079" alt="Captura de pantalla 2026-03-19 130542" src="https://github.com/user-attachments/assets/9e9f733c-3ed7-4afc-b965-ef24a4b43262" />
<img width="1919" height="1079" alt="Captura de pantalla 2026-03-19 130640" src="https://github.com/user-attachments/assets/4c7286cd-b50c-48ec-b96f-6ebd8eb2ebbd" />

---

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
