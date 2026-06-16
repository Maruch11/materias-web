# Estado actual:

- ✅ Entorno virtual
- ✅ Flask instalado
- ✅ Proyecto creado
- ✅ Servidor Flask funcionando
- ✅ Ruta / funcionando
- ✅ render_template() funcionando
- ✅ Carpeta templates/ reconocida
- ✅ Primera página HTML renderizada
- ✅get_careers() funciona
    - ✅ get_subjects_by_career() funciona.
    - ✅ Filtra correctamente.
    - ✅ Devuelve 32 materias para la carrera de prueba.

# Estructura de proyecto
```
materias-web/
├── app.py
├── requirements.txt
├── .gitignore
├── data/
├── services/
│   ├── careers_service.py
│   └── subjects_service.py
├── static/
│   ├── css/
│   └── img/
└── templates/
    ├── base.html
    ├── index.html
    ├── careers.html
    ├── subjects.html
    └── subject_detail.html
```
# Primer flujo 
```
Navegador
    ↓
GET /
    ↓
Flask (app.py)
    ↓
render_template("index.html")
    ↓
templates/index.html
    ↓
HTML
    ↓
Navegador
```

# Definición de estructura de navegación
```
Inicio
│
├── Carreras
│     └── Materias
│            └── Detalle de materia
│                    ├── Programa
│                    ├── Enlaces
│                    └── Manuales
│
└── Acerca de
```

# Maquetación 
## Pantalla
```
+----------------------------------+
| Materias Web                     |
+----------------------------------+
| Carreras                         |
|----------------------------------|
| Policia                          |
| Bombero                          |
| ...                              |
+----------------------------------+
```

## Tarjeta career cliqueable
```
┌────────────────────┐
│ Policía            │
│ Ver materias       │
└────────────────────┘
```

## Tarjeta subject
```
Materia
├── Nombre
├── Term
└── Official URL
```
```
┌─────────────────────────────┐
│ Derecho                     │
│ 2° Cuatrimestre             │
│ 🔗 Programa oficial        | 
└─────────────────────────────┘
```

# Estrategia de diseño
```
base.html
↓
layout común

.card
↓
componente visual común

templates
↓
contenido específico
```

# Funcionalidad careers_service
```
careers_service.py
↓
leer careers.csv
↓
devolver lista de carreras
↓
mostrar carreras en index.html
```

# Funcionalidad de subject_service
```
leer subjects.csv
↓
filtrar por career_id
↓
devolver materias de esa carrera
```

# flujo completo de punta a punta
```
http://127.0.0.1:5000
↓
clic en una carrera
↓
http://127.0.0.1:5000/careers/1
↓
lista de materias
```