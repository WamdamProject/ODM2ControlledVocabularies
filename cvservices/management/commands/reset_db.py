from django.core.management.base import BaseCommand, CommandError
from cvservices.models import Units, MethodType, ObjectTypology, ElectronicFileFormat, CategoricalValue, \
 SpatialReference, DualValueMeaning, DescriptorValue, AttributeDataType, \
 AggregationStatistic, ElevationDatum, SeasonName, ObjectType, InstanceName, AttributeName

class Command(BaseCommand):
    help = 'Deletes every object in the database'

    #def add_arguments(self, parser):
    #    pass

    def handle(self, *args, **options):

        for object in Units.objects.all():
            object.delete()

        for object in MethodType.objects.all():
            object.delete()

        for object in ObjectTypology.objects.all():
            object.delete()

        for object in ElectronicFileFormat.objects.all():
            object.delete()

        for object in CategoricalValue.objects.all():
            object.delete()

        for object in SpatialReference.objects.all():
            object.delete()

        for object in DualValueMeaning.objects.all():
            object.delete()

        for object in DescriptorValue.objects.all():
            object.delete()

        for object in AttributeDataType.objects.all():
            object.delete()

        for object in ElevationDatum.objects.all():
            object.delete()

        for object in SeasonName.objects.all():
            object.delete()

        for object in AggregationStatistic.objects.all():
            object.delete()

        for object in ObjectType.objects.all():
            object.delete()

        for object in InstanceName.objects.all():
            object.delete()

        for object in AttributeName.objects.all():
            object.delete()
