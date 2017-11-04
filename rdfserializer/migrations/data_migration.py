# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def forwards(apps, schema_editor):
    namespace = apps.get_model('rdfserializer', 'Namespace')
    node = apps.get_model('rdfserializer', 'Node')
    field_relation = apps.get_model('rdfserializer', 'FieldRelation')
    scheme = apps.get_model('rdfserializer', 'Scheme')

    db_alias = schema_editor.connection.alias

    namespace.objects.using(db_alias).bulk_create([
        namespace(alias='skos', reference='http://www.w3.org/2004/02/skos/core'),
        namespace(alias='wamdam1', reference='http://vocabulary.wamdam1.org/WAMDAM1/WAMDAM1Terms'),
        namespace(alias='dc', reference='http://purl.org/dc/elements/1.1/'),
    ])

    node.objects.using(db_alias).bulk_create([
        node(name='prefLabel', namespace_id='skos'),
        node(name='definition', namespace_id='skos'),
        node(name='note', namespace_id='skos'),
        node(name='historyNote', namespace_id='skos'),
        node(name='exactMatch', namespace_id='skos'),
        node(name='category', namespace_id='wamdam1'),
        node(name='producesResult', namespace_id='wamdam1'),
        node(name='Concept', namespace_id='skos'),
        node(name='inScheme', namespace_id='skos'),
        node(name='offset1', namespace_id='wamdam1'),
        node(name='offset2', namespace_id='wamdam1'),
        node(name='offset3', namespace_id='wamdam1'),
        node(name='defaultUnit', namespace_id='wamdam1'),
        node(name='dimensionSymbol', namespace_id='wamdam1'),
        node(name='dimensionLength', namespace_id='wamdam1'),
        node(name='dimensionMass', namespace_id='wamdam1'),
        node(name='dimensionTime', namespace_id='wamdam1'),
        node(name='dimensionCurrent', namespace_id='wamdam1'),
        node(name='dimensionTemperature', namespace_id='wamdam1'),
        node(name='dimensionAmount', namespace_id='wamdam1'),
        node(name='dimensionLight', namespace_id='wamdam1'),
    ])

    field_relation.objects.using(db_alias).bulk_create([
        field_relation(field_name='name',
                       node=node.objects.using(db_alias).get(name='prefLabel', namespace_id='skos')),
        field_relation(field_name='definition',
                       node=node.objects.using(db_alias).get(name='definition', namespace_id='skos')),
        field_relation(field_name='note',
                       node=node.objects.using(db_alias).get(name='note', namespace_id='skos')),
        field_relation(field_name='provenance',
                       node=node.objects.using(db_alias).get(name='historyNote', namespace_id='skos')),
        field_relation(field_name='provenance_uri',
                       node=node.objects.using(db_alias).get(name='exactMatch', namespace_id='skos')),
        field_relation(field_name='category',
                       node=node.objects.using(db_alias).get(name='category', namespace_id='wamdam1')),
        field_relation(field_name='produces_result',
                       node=node.objects.using(db_alias).get(name='producesResult', namespace_id='wamdam1')),
        field_relation(field_name='term',
                       node=node.objects.using(db_alias).get(name='Concept', namespace_id='skos')),
        field_relation(field_name='offset1',
                       node=node.objects.using(db_alias).get(name='offset1', namespace_id='wamdam1')),
        field_relation(field_name='offset2',
                       node=node.objects.using(db_alias).get(name='offset2', namespace_id='wamdam1')),
        field_relation(field_name='offset3',
                       node=node.objects.using(db_alias).get(name='offset3', namespace_id='wamdam1')),
        field_relation(field_name='default_unit',
                       node=node.objects.using(db_alias).get(name='defaultUnit', namespace_id='wamdam1')),
        field_relation(field_name='dimension_symbol',
                       node=node.objects.using(db_alias).get(name='dimensionSymbol', namespace_id='wamdam1')),
        field_relation(field_name='dimension_length',
                       node=node.objects.using(db_alias).get(name='dimensionLength', namespace_id='wamdam1')),
        field_relation(field_name='dimension_mass',
                       node=node.objects.using(db_alias).get(name='dimensionMass', namespace_id='wamdam1')),
        field_relation(field_name='dimension_time',
                       node=node.objects.using(db_alias).get(name='dimensionTime', namespace_id='wamdam1')),
        field_relation(field_name='dimension_current',
                       node=node.objects.using(db_alias).get(name='dimensionCurrent', namespace_id='wamdam1')),
        field_relation(field_name='dimension_temperature',
                       node=node.objects.using(db_alias).get(name='dimensionTemperature', namespace_id='wamdam1')),
        field_relation(field_name='dimension_amount',
                       node=node.objects.using(db_alias).get(name='dimensionAmount', namespace_id='wamdam1')),
        field_relation(field_name='dimension_light',
                       node=node.objects.using(db_alias).get(name='dimensionLight', namespace_id='wamdam1')),
    ])

    scheme.objects.using(db_alias).bulk_create([
        scheme(name='aggregationStatistic', title='WAMDAM1 Aggregation Statistic Controlled Vocabulary',
               creator='WAMDAM1 Working Group',
               description='A vocabulary for describing the calculated statistic associated with recorded observations.'
                           ' The aggregation statistic is calculated over the time aggregation interval associated '
                           'with the recorded observation. ',
               uri='http://vocabulary.wamdam.org/aggregationstatistic'
               ),
        scheme(name='elevationDatum', title='WAMDAM1 Elevation Datum Controlled Vocabulary', creator='WAMDAM1 Working Group',
               description='A vocabulary for describing vertical datums. Vertical datums are used in WAMDAM1 to '
                           'specify the origin for elevations associated with SamplingFeatures.',
               uri='http://vocabulary.wamdam.org/elevationdatum'
               ),
        scheme(name='methodType', title='WAMDAM1 MethodType Controlled Vocabulary', creator='WAMDAM Working Group',
               description='A vocabulary for describing types of Methods associated with creating observations. '
                           'MethodTypes correspond with ActionTypes in WAMDAM1. An Action must be performed using '
                           'an appropriate MethodType - e.g., a specimen collection Action should be associated '
                           'with a specimen collection method.',
               uri='http://vocabulary.wamdam.org/methodtype'
               ),
        scheme(name='units', title='WAMDAM1 Units Controlled Vocabulary', creator='WAMDAM1 Working Group',
               description='A vocabulary for describing the type of units in which a Result is expressed.',
               uri='http://vocabulary.wamdam.org/units'
               ),
        scheme(name='objectTopology', title='WAMDAM1 Object Topology Vocabulary', creator='WAMDAM1 Working Group',
               description='The typology of the Object Type as either: Node, link, network.',
               uri='http://vocabulary.wamdam.org/objecttopology'
               ),
        scheme(name='attributeName', title='WAMDAM1 Attribute Name Vocabulary', creator='WAMDAM1 Working Group',
               description='Controlled vocabulary for attributes like Volume which maps out to native attributes like capacity, vol, and storage.',
               uri='http://vocabulary.wamdam.org/attributename'
               ),
        scheme(name='attributeDataType', title='WAMDAM1 Attribute Data Type Controlled Vocabulary', creator='WAMDAM1 Working Group',
               description='Boolean, parameters, SeasonalParameter, TextFree, ControlledText, Files, TimeSeries, Column, Dummay, Network, MultiColumnArray.',
               uri='http://vocabulary.wamdam.org/attributedatatype'
               ),
        scheme(name='fileFormat', title='WAMDAM1 File Format Controlled Vocabulary', creator='WAMDAM1 Working Group',
               description='File format like csv, jpg, NETCDF.',
               uri='http://vocabulary.wamdam.org/fileformat'
               ),
        scheme(name='seasonName', title='WAMDAM1 Season Name Vocabulary', creator='WAMDAM1 Working Group',
               description='Controlled vocabulary for seasons (e.g., winter and day, night, holiday, weekend, week days).',
               uri='http://vocabulary.wamdam.org/seasonname'
               ),
        scheme(name='spatialReference', title='WAMDAM1 Spatial Reference Controlled Vocabulary', creator='WAMDAM1 Working Group',
               description='A spatial reference (e.g., NAD 1983) to reference all the instances that belong to the same Master Network.',
               uri='http://vocabulary.wamdam.org/spatialreference'
               ),
        scheme(name='instanceName', title='WAMDAM1 Instance Name Controlled Vocabulary', creator='WAMDAM1 Working Group',
               description='Univeral instance name to link synonymous instance terms for the samee instance (e.g., Hyrum = Hrm & HyrumCity).',
               uri='http://vocabulary.wamdam.org/instancename'
               ),
        scheme(name='objectTypes', title='WAMDAM1 Object Types Controlled Vocabulary', creator='WAMDAM1 Working Group',
               description='Controlled vocabulary for Object types like Reservoir which maps out to native object types like dam, reservoir, and waterbody.',
               uri='http://vocabulary.wamdam.org/objecttypes'
               ),
        scheme(name='booleanValueMeaning', title='WAMDAM1 Boolean Value Meaning Controlled Vocabulary', creator='WAMDAM1 Working Group',
               description='This table provides the controlled meaning of boolean data values.',
               uri='http://vocabulary.wamdam.org/booleanvaluemeaning'
               ),
        scheme(name='textControlledValue', title='WAMDAM1 Text Controlled Value Controlled Vocabulary', creator='WAMDAM1 Working Group',
               description='Controlled text values that can be shared across attributes of instances like Land use “Grass_Pasture” or irrigation type "Flood”, states "Utah".',
               uri='http://vocabulary.wamdam.org/textcontrolledvalue'
               ),
    ])


class Migration(migrations.Migration):
    initial = False

    dependencies = [
        ('rdfserializer', 'schema_migration'),
    ]

    operations = [
        migrations.RunPython(
            forwards,
            hints={'target_db': 'default'}
        ),
    ]

