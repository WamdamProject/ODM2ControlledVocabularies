from cvservices.models import *
from cvinterface.views.base_views import *

vocabulary_list_view = DefaultVocabularyListView
vocabulary_detail_view = DefaultVocabularyDetailView
vocabulary_list_template = 'cvinterface/vocabularies/default_list.html'
vocabulary_detail_template = 'cvinterface/vocabularies/default_detail.html'

request_list_view = DefaultRequestListView
request_create_view = DefaultRequestCreateView
request_update_view = DefaultRequestUpdateView
request_list_template = 'cvinterface/requests/default_list.html'
request_create_template = 'cvinterface/requests/default_form.html'
request_update_template = 'cvinterface/requests/default_update_form.html'

vocabularies = {
    # optional keys:
    # list_view, detail_view, list_template, detail_template

    'methodtype': {
        'name': MethodType._meta.verbose_name,
        'definition': 'A term for describing types of Methods associated with recording or generating data values to attributes. Example method types are like "expert opinion", "field procedure", "model simulation".',
        'model': MethodType,
    },
    'aggregationstatistic': {
        'name': AggregationStatistic._meta.verbose_name,
        'definition': 'A term for describing the statistical action used to calculate over recorded time series values within a time interval. For example, 100 cfs of delivery target to a demand site is a "cumulative" aggregation statistic calculated over a time interval like a month.',
        'model': AggregationStatistic,
    },
    'elevationdatum': {
        'name': ElevationDatum._meta.verbose_name,
        'definition': 'A term for describing vertical datums. Vertical datums are used in WaMDaM to specify the origin for elevations associated with node instance in networks.',
        'model': ElevationDatum,
    },
    'seasonname': {
        'name': SeasonName._meta.verbose_name,
        'definition': 'A term for describing a categorical value that may correspond to numeric values of an attribute. The CategoricalValue represents steps in time (e.g., Winter, Summer, March, April) or space (e.g., categorical levels of reservoir levels (e.g., inactive, conservation, flood)',
        'model': SeasonName,
    },
    'units': {
        'name': Units._meta.verbose_name,
        'definition': 'A term for describing the name of the Unit of data value of an attribute.',
        'model': Units,
    },
    'objecttypology': {
        'name': ObjectTypology._meta.verbose_name,
        'definition': 'A term for describing the category of an Object Type as either: Node, link, network.',
        'model': ObjectTypology,
    },
    'attributename': {
        'name': AttributeName._meta.verbose_name,
        'definition': 'A Term describing the name of quantitate or qualitative property of a water system component (e.g., reservoir).',
        'model': AttributeName,
    },
    'attributedatatype': {
        'name': AttributeDataType._meta.verbose_name,
        'definition': 'A term for describing the supported types of data that an attribute in WaMDaM can take based on logical and physical groupings like numeric, text, time stamped values, and parried categorical values. For example, numeric values, descriptor value, electronic files, time series, and multi attribute series.',
        'model': AttributeDataType,
    },
    'electronicfileformat': {
        'name': ElectronicFileFormat._meta.verbose_name,
        'definition': 'A term for describing the supported physical format of files loaded into WaMDaM as values to attributes(e.g., csv, jpg, NETCDF).',
        'model': ElectronicFileFormat,
    },
    'spatialreference': {
        'name': SpatialReference._meta.verbose_name,
        'definition': 'A term for describing a geographic reference to all the node instances that belong to the same Master Network.',
        'model': SpatialReference,
    },
    'instancename': {
        'name': InstanceName._meta.verbose_name,
        'definition': 'A term for describing the name of a specific node or link system component in a specific location which can related synonymous native instance terms (e.g., Hyrum = Hrm & Hyrum Reservoir).',
        'model': InstanceName,
    },
    'objecttype': {
        'name': ObjectType._meta.verbose_name,
        'definition': 'A term for describing a built or natural water system component .',
        'model': ObjectType,
    },
    'categorical': {
        'name': Categorical._meta.verbose_name,
        'definition': 'A term for describing descriptive values (characters as numeric or strings) for an attribute. The descriptor values can be shared across attributes of systems components like land use "Grass_Pasture" or irrigation type "Flood", or site code as "10000010"',
        'model': Categorical,
    }
}

requests = {
    # optional keys:
    # list_view, create_view, update_view, list_template, create_template, update_template

    'methodtyperequest': {
        'vocabulary': 'methodtype',
        'vocabulary_model': MethodType,
        'name': MethodTypeRequest._meta.verbose_name,
        'model': MethodTypeRequest,
    },
    'aggregationstatisticrequest': {
        'vocabulary': 'aggregationstatistic',
        'vocabulary_model': AggregationStatistic,
        'name': AggregationStatisticRequest._meta.verbose_name,
        'model': AggregationStatisticRequest,
    },
    'elevationdatumrequest': {
        'vocabulary': 'elevationdatum',
        'vocabulary_model': ElevationDatum,
        'name': ElevationDatumRequest._meta.verbose_name,
        'model': ElevationDatumRequest,
    },
    'seasonnamerequest': {
        'vocabulary': 'seasonname',
        'vocabulary_model': SeasonName,
        'name': SeasonNameRequest._meta.verbose_name,
        'model': SeasonNameRequest,
    },
    'unitsrequest': {
        'vocabulary': 'units',
        'vocabulary_model': Units,
        'name': UnitsRequest._meta.verbose_name,
        'model': UnitsRequest,
    },
    'objecttypologyrequest': {
        'vocabulary': 'objecttypology',
        'vocabulary_model': ObjectTypology,
        'name': ObjectTypologyRequest._meta.verbose_name,
        'model': ObjectTypologyRequest,
    },
    'attributenamerequest': {
        'vocabulary': 'attributename',
        'vocabulary_model': AttributeName,
        'name': AttributeNameRequest._meta.verbose_name,
        'model': AttributeNameRequest,
    },
    'attributedatatyperequest': {
        'vocabulary': 'attributedatatype',
        'vocabulary_model': AttributeDataType,
        'name': AttributeDataTypeRequest._meta.verbose_name,
        'model': AttributeDataTypeRequest,
    },
    'electronicfileformatrequest': {
        'vocabulary': 'electronicfileformat',
        'vocabulary_model': ElectronicFileFormat,
        'name': ElectronicFileFormatRequest._meta.verbose_name,
        'model': ElectronicFileFormatRequest,
    },
    'spatialreferencerequest': {
        'vocabulary': 'spatialreference',
        'vocabulary_model': SpatialReference,
        'name': SpatialReferenceRequest._meta.verbose_name,
        'model': SpatialReferenceRequest,
    },
    'instancenamerequest': {
        'vocabulary': 'instancename',
        'vocabulary_model': InstanceName,
        'name': InstanceNameRequest._meta.verbose_name,
        'model': InstanceNameRequest,
    },
    'objecttyperequest': {
        'vocabulary': 'objecttype',
        'vocabulary_model': ObjectType,
        'name': ObjectTypeRequest._meta.verbose_name,
        'model': ObjectTypeRequest,
    },
    'categoricalrequest': {
        'vocabulary': 'categorical',
        'vocabulary_model': Categorical,
        'name': CategoricalRequest._meta.verbose_name,
        'model': CategoricalRequest,
    }
}

