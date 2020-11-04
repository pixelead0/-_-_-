# Pasos para generar diagramas entidad relación de los modelos del sistema

## Requisitos
```
apt-get update
apt-get install python-dev graphviz libgraphviz-dev pkg-config

pip install pygraphviz pyparsing pydot graphviz
```

## Para generar los diagramas
```
# en español
python manage.py graph_models  -a --pydot  -g  -E -n -o db_diagrams/$(date +"%Y-%m-%d_%H%M%S").png --disable-abstract-fields

# en inglés
python manage.py graph_models -a  --pydot  -g  -E  -o db_diagrams/$(date +"%Y-%m-%d_%H%M%S").png --disable-abstract-fields

# En circulo
python manage.py graph_models --pygraphviz -a -l circo -g  -E  -o db_diagrams/$(date +"%Y-%m-%d_%H%M%S").png --disable-abstract-fields


```
