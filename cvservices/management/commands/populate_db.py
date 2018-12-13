import xlrd
from django.db import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from cvservices.models import Units, MethodType, ResourceType,ObjectTypology, ElectronicFileFormat, \
 SpatialReference, Categorical, AttributeDataType, \
 AggregationStatistic, ElevationDatum, SeasonName, ObjectType, InstanceName, AttributeName

models = {
    'Units': Units,
    'ResourceType': ResourceType,
    'MethodType': MethodType,
    'ObjectTypology': ObjectTypology,
    'ElectronicFileFormat': ElectronicFileFormat,
    'SpatialReference': SpatialReference,
    'Categorical': Categorical,
    'AttributeDataType': AttributeDataType,
    'AggregationStatistic': AggregationStatistic,
    'ElevationDatum': ElevationDatum,
    'SeasonName': SeasonName,
    'ObjectType': ObjectType,
    'InstanceName': InstanceName,
    'AttributeName': AttributeName
}

class Command(BaseCommand):
    help = 'Populates the database from an excel file with a given format'

    def add_arguments(self, parser):
        parser.add_argument('excel_file', nargs='+', type=str)

    def handle(self, *args, **options):

        excel_file = options.get('excel_file')

        try:
            wb = xlrd.open_workbook(excel_file[0])
        except IOError as e:
            raise CommandError(e)

        for sheet in wb.sheets():

            # Just get row names
            col_names = []
            for row in range(sheet.nrows):
                if row > 0:
                    break

                if row == 2:
                    continue

                for col in range(sheet.ncols):
                    col_names.append(sheet.cell(row,col).value.lower())

            # Read data from cells
            for row in range(sheet.nrows):
                col_values = []
                if row < 2:
                    continue

                for col in range(sheet.ncols):
                    #if isinstance(sheet.cell(row,col).value, float):
                    #    col_values.append(int(round(sheet.cell(row,col).value)))
                    #else:
                        col_values.append(sheet.cell(row,col).value)

                kwargs = dict(zip(col_names, col_values))

                obj = models[sheet.name].objects.filter(term=kwargs['term']).first()

                if not obj:
                    obj = models[sheet.name](**kwargs)
                    obj.save()
                else:
                    print "Avoided duplicate term: %s" % kwargs['term']

                #try:
                #    obj, created = models[sheet.name].objects.get_or_create(**kwargs)
                #except IntegrityError, e:
                #    print "Avoided duplicate term: %s" % kwargs['term']
