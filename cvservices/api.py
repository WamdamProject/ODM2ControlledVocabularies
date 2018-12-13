import StringIO
from collections import OrderedDict
import csv
from django.http.response import HttpResponse
from tastypie.api import Api
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.utils.mime import build_content_type

from rdfserializer.api import ModelRdfResource
from models import MethodType, ResourceType, AggregationStatistic, ElevationDatum, SeasonName, Units, ObjectTypology, AttributeName, \
     AttributeDataType, ElectronicFileFormat, SpatialReference, InstanceName, ObjectType, \
     Categorical


class CSVSerializer(Serializer):
    formats = ['csv']
    content_types = {
        'csv': 'text/plain'
    }

    def to_csv(self, data, options=None, writer=None):
        options = options or {}
        data = self.to_simple(data, options)
        excluded_fields = [u'resource_uri']

        raw_data = StringIO.StringIO()
        first = True

        if "meta" in data.keys():
            objects = data.get("objects")

            for value in objects:
                test = {}
                for excluded_field in excluded_fields:
                    del value[excluded_field]
                self.flatten(value, test)

                odict = OrderedDict()
                odict['Term'] = test['term']
                del test['term']
                odict['UnitsName'] = test['name']
                del test['name']
                odict['UnitsTypeCV'] = test['type']
                del test['type']
                odict['UnitsAbbreviation'] = test['abbreviation']
                del test['abbreviation']
                odict['UnitsLink'] = test['link']
                del test['link']

                if first:
                    writer = csv.DictWriter(raw_data, odict.keys())
                    writer.writeheader()
                    writer.writerow(odict)
                    first = False
                else:
                    writer.writerow({k: (v.encode('utf-8') if isinstance(v, int) is not True and isinstance(v, type(
                        None)) is not True else v) for k, v in odict.items()})
        else:
            test = {}
            for excluded_field in excluded_fields:
                del data[excluded_field]
            self.flatten(data, test)
            odict = OrderedDict()
            odict['Term'] = test['term']
            del test['term']
            odict['UnitsName'] = test['name']
            del test['name']
            odict['UnitsTypeCV'] = test['type']
            del test['type']
            odict['UnitsAbbreviation'] = test['abbreviation']
            del test['abbreviation']
            odict['UnitsLink'] = test['link']
            del test['link']

            if first:
                writer = csv.DictWriter(raw_data, odict.keys())
                writer.writeheader()
                writer.writerow(odict)
                first = False
            else:
                writer.writerow(odict)
        CSVContent = raw_data.getvalue()
        return CSVContent

    def flatten(self, data, odict={}):
        if isinstance(data, list):
            for value in data:
                self.flatten(value, odict)
        elif isinstance(data, dict):
            for (key, value) in data.items():
                if not isinstance(value, (dict, list)):
                    odict[key] = value
                else:
                    self.flatten(value, odict)


class UnitsResource(ModelRdfResource):
    scheme = 'units'

    class Meta(ModelRdfResource.Meta):
        queryset = Units.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'units'

class MethodTypeResource(ModelRdfResource):
    scheme = 'methodType'

    class Meta(ModelRdfResource.Meta):
        queryset = MethodType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'methodtype'

class ResourceTypeResource(ModelRdfResource):
    scheme = 'resourceType'

    class Meta(ModelRdfResource.Meta):
        queryset = ResourceType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'resourcetype'          
          
          
class AggregationStatisticResource(ModelRdfResource):
    scheme = 'aggregationStatistic'

    class Meta(ModelRdfResource.Meta):
        queryset = AggregationStatistic.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'aggregationstatistic'

class ElevationDatumResource(ModelRdfResource):
    scheme = 'elevationDatum'

    class Meta(ModelRdfResource.Meta):
        queryset = ElevationDatum.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'elevationdatum'

class SeasonNameResource(ModelRdfResource):
    scheme = 'seasonName'

    class Meta(ModelRdfResource.Meta):
        queryset = SeasonName.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'seasonname'

class ObjectTypologyResource(ModelRdfResource):
    scheme = 'objectTypology'

    class Meta(ModelRdfResource.Meta):
        queryset = ObjectTypology.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'objecttypology'

class AttributeNameResource(ModelRdfResource):
    scheme = 'attributeName'

    class Meta(ModelRdfResource.Meta):
        queryset = AttributeName.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'attributename'

class AttributeDataTypeResource(ModelRdfResource):
    scheme = 'attributeDataType'

    class Meta(ModelRdfResource.Meta):
        queryset = AttributeDataType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'attributedatatype'

class ElectronicFileFormatResource(ModelRdfResource):
    scheme = 'electronicfileFormat'

    class Meta(ModelRdfResource.Meta):
        queryset = ElectronicFileFormat.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'electronicfileformat'


class SpatialReferenceResource(ModelRdfResource):
    scheme = 'spatialReference'

    class Meta(ModelRdfResource.Meta):
        queryset = SpatialReference.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'spatialreference'

class InstanceNameResource(ModelRdfResource):
    scheme = 'instanceName'

    class Meta(ModelRdfResource.Meta):
        queryset = InstanceName.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'instancename'

class ObjectTypeResource(ModelRdfResource):
    scheme = 'objectType'

    class Meta(ModelRdfResource.Meta):
        queryset = ObjectType.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'objecttype'


class CategoricalResource(ModelRdfResource):
    scheme = 'categorical'

    class Meta(ModelRdfResource.Meta):
        queryset = Categorical.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = 'categorical'

v1_api = Api(api_name='v1')

v1_api.register(MethodTypeResource())
v1_api.register(ResourceTypeResource())
v1_api.register(AggregationStatisticResource())
v1_api.register(ElevationDatumResource())
v1_api.register(SeasonNameResource())
v1_api.register(UnitsResource())
v1_api.register(ObjectTypologyResource())
v1_api.register(AttributeNameResource())
v1_api.register(AttributeDataTypeResource())
v1_api.register(ElectronicFileFormatResource())
v1_api.register(SpatialReferenceResource())
v1_api.register(InstanceNameResource())
v1_api.register(ObjectTypeResource())
v1_api.register(CategoricalResource())

