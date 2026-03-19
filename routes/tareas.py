from flask import Blueprint, request, jsonify
from database import db
from models.tarea import Tarea

tareas_bp = Blueprint('tareas', __name__)


# ──────────────────────────────────────────────
# POST /tareas  →  Crear una tarea
# ──────────────────────────────────────────────
@tareas_bp.route('/tareas', methods=['POST'])
def crear_tarea():
    datos = request.get_json()

    if not datos:
        return jsonify({'error': 'El cuerpo de la petición debe ser JSON'}), 400

    titulo = datos.get('titulo', '').strip()
    if not titulo:
        return jsonify({'error': 'El campo "titulo" es obligatorio'}), 400

    descripcion = datos.get('descripcion', '').strip()
    estado = datos.get('estado', 'pendiente').strip()

    if estado not in Tarea.ESTADOS_VALIDOS:
        return jsonify({
            'error': f'Estado no válido. Opciones: {Tarea.ESTADOS_VALIDOS}'
        }), 400

    nueva_tarea = Tarea(
        titulo=titulo,
        descripcion=descripcion,
        estado=estado
    )
    db.session.add(nueva_tarea)
    db.session.commit()

    return jsonify({
        'mensaje': 'Tarea creada correctamente',
        'tarea': nueva_tarea.to_dict()
    }), 201


# ──────────────────────────────────────────────
# GET /tareas  →  Obtener todas las tareas
# ──────────────────────────────────────────────
@tareas_bp.route('/tareas', methods=['GET'])
def obtener_tareas():
    # Filtro opcional por estado: GET /tareas?estado=pendiente
    estado_filtro = request.args.get('estado')

    if estado_filtro:
        if estado_filtro not in Tarea.ESTADOS_VALIDOS:
            return jsonify({
                'error': f'Estado no válido. Opciones: {Tarea.ESTADOS_VALIDOS}'
            }), 400
        tareas = Tarea.query.filter_by(estado=estado_filtro).all()
    else:
        tareas = Tarea.query.all()

    return jsonify({
        'total': len(tareas),
        'tareas': [t.to_dict() for t in tareas]
    }), 200


# ──────────────────────────────────────────────
# GET /tareas/<id>  →  Obtener una tarea por ID
# ──────────────────────────────────────────────
@tareas_bp.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({'error': f'Tarea con id {id} no encontrada'}), 404

    return jsonify({'tarea': tarea.to_dict()}), 200


# ──────────────────────────────────────────────
# PUT /tareas/<id>  →  Actualizar una tarea
# ──────────────────────────────────────────────
@tareas_bp.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({'error': f'Tarea con id {id} no encontrada'}), 404

    datos = request.get_json()
    if not datos:
        return jsonify({'error': 'El cuerpo de la petición debe ser JSON'}), 400

    if 'titulo' in datos:
        titulo = datos['titulo'].strip()
        if not titulo:
            return jsonify({'error': 'El campo "titulo" no puede estar vacío'}), 400
        tarea.titulo = titulo

    if 'descripcion' in datos:
        tarea.descripcion = datos['descripcion'].strip()

    if 'estado' in datos:
        estado = datos['estado'].strip()
        if estado not in Tarea.ESTADOS_VALIDOS:
            return jsonify({
                'error': f'Estado no válido. Opciones: {Tarea.ESTADOS_VALIDOS}'
            }), 400
        tarea.estado = estado

    db.session.commit()

    return jsonify({
        'mensaje': 'Tarea actualizada correctamente',
        'tarea': tarea.to_dict()
    }), 200


# ──────────────────────────────────────────────
# DELETE /tareas/<id>  →  Eliminar una tarea
# ──────────────────────────────────────────────
@tareas_bp.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    tarea = Tarea.query.get(id)
    if not tarea:
        return jsonify({'error': f'Tarea con id {id} no encontrada'}), 404

    db.session.delete(tarea)
    db.session.commit()

    return jsonify({'mensaje': f'Tarea con id {id} eliminada correctamente'}), 200
