from rest_framework import serializers
# Django REST Framework
from rest_framework.metadata import SimpleMetadata
from rest_framework.utils.field_mapping import ClassLookupDict


class FormMetadata(SimpleMetadata):
    """
    Sirve para mostrar el schema de un form al hacer una petición
    con el método OPTIONS.
    """
    label_lookup = ClassLookupDict({
        serializers.Field: 'field',
        serializers.BooleanField: 'checkbox',
        serializers.NullBooleanField: 'boolean',
        serializers.CharField: 'text',
        serializers.UUIDField: 'text',
        serializers.URLField: 'text',
        serializers.EmailField: 'email',
        serializers.RegexField: 'text',
        serializers.SlugField: 'text',
        serializers.IntegerField: 'number',
        serializers.FloatField: 'number',
        serializers.DecimalField: 'number',
        serializers.DateField: 'date',
        serializers.DateTimeField: 'datetime',
        serializers.TimeField: 'time',
        serializers.ChoiceField: 'choice',
        serializers.MultipleChoiceField: 'multiple choice',
        serializers.FileField: 'file',
        serializers.ImageField: 'image',
        serializers.ListField: 'list',
        serializers.DictField: 'nested object',
        serializers.Serializer: 'nested object',
    })

    def get_field_info(self, field):
        """
        Retorna la metadata de un field de serializer, en caso de que el campo
        sea de tipo serializer.Field, significa que es una foreign key
        por lo que se agregan las opciones de dicho campo
        """
        field_info = super().get_field_info(field)
        field_info['name'] = field.field_name
        if field_info['type'] == 'field':
            try:
                options = field.queryset.filter(is_active=True)
            except AttributeError:
                options = []
            choices = []
            for choice in options:
                choices.append({
                    'value': choice.id,
                    'text': choice.name
                })
            field_info['choices'] = choices
        elif field_info['type'] == 'choice':
            # Se cambia el nombre de las keys para que se use en
            # el frontend
            choices = []
            for choice in field_info['choices']:
                choices.append({
                    'value': choice['value'],
                    'text': choice['display_name']
                })
            field_info['choices'] = choices
        return field_info
