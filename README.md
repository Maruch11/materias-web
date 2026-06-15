# Estado actual:

- ✅ Entorno virtual
- ✅ Flask instalado
- ✅ Proyecto creado
- ✅ Servidor Flask funcionando
- ✅ Ruta / funcionando
- ✅ render_template() funcionando
- ✅ Carpeta templates/ reconocida
- ✅ Primera página HTML renderizada

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

# Maquetación de cada pantalla
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