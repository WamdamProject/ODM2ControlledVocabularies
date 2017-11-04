import re

def upper_splitted(string):
    return " ".join(re.findall('[A-Z][a-z]*', string))

lfirst = lambda s: s[:1].lower() + s[1:] if s else ''


"""
This template resembles a couple of ControlledVocabulary and ControlledVocabularyRequest
found on the file cvservices/models.py
"""
model_template = """class %(uppercase)s(ControlledVocabulary):
    class Meta:
        db_table = '%(lowercase)s'
        verbose_name = '%(uppercase)s'
        ordering = ["name"]


class %(uppercase)sRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = '%(lowercase)srequests'
        verbose_name = '%(uppersplitted)s Request'

"""

"""
This template resembles an item of the dictionary named 'vocabularies' found on the file 
cvinterface/controlled_vocabularies.py in the line 16
"""
vocabularies_template = """'%(lowercase)s': {
    'name': %(uppercase)s._meta.verbose_name,
    'definition': '%(description)s',
    'model': %(uppercase)s,
},"""

"""
This template resembles an item of the dictionary named 'requests' found on the file 
cvinterface/controlled_vocabularies.py in the line 257
"""
requests_template = """'%(lowercase)srequest': {
    'vocabulary': '%(lowercase)s',
    'vocabulary_model': %(uppercase)s,
    'name': %(uppercase)sRequest._meta.verbose_name,
    'model': %(uppercase)sRequest,
},"""

"""
This template resembles a ModelResource class found on the file 
cvservices/api.py
"""
model_resource_template = """class %(uppercase)sResource(ModelRdfResource):
    scheme = '%(lfirst)s'

    class Meta(ModelRdfResource.Meta):
        queryset = %(uppercase)s.objects.filter(ModelRdfResource.vocabulary_filter)
        resource_name = '%(lowercase)s'
"""

"""
This template resembles the registration of a ModelResource class found on the file 
cvservices/api.py from line 434
"""
model_resource_register_template = """v1_api.register(%(uppercase)sResource())"""

"""
This template resembles instructions erase all the table objects in the database,
found on the file cvservices/management/commands/reset_db.py from line 19
"""
reset_db_template = """for object in %(uppercase)s.objects.all():
    object.delete()"""

"""
This template resembles an item on the list 
found on the file rdfserializer/migrations/data_migration.py from line 88
"""
data_migration_template = """scheme(name='%(lfirst)s', title='WaDE %(uppercase)s Controlled Vocabulary', creator='WaDE Working Group',
    description='%(description)s',
    uri='http://vocabulary.wade.org/%(lowercase)s'
    ),"""

""" 
You shold replace the titles and descriptions in this list with your own table names and descriptions

Every item of this list of tuples must follow this convention: 
('<CamelCaseName>', '<Description>')
https://en.wikipedia.org/wiki/Camel_case
"""

titles = [

("LuBeneficialUse", 'This table is based on the [use] column in the [vw_CDSS_NetAmts] view, but the definitions have been recreated so that the user can see the full definition. For example, for a water right that has a beneficial use listed as "IRRDOMSTO", the category has been broken down to reflect the three uses: "Irrigation, domestic, storage." Please see Appendix A - [LU_BENEFICIAL_USE] for the view script.'),

("LuCropType", "To be added"),

("LuFreshSalineIndicator", "This table is based on the reported water quality of the resource in question. The default for Colorado is fresh/potable water."),

("LuGeneratorType", "To be added"),

("LuIrrigationMethod", "To be added"),

("LuLegalStatus", 'This table is based on the [vw_CDSS_NetAmts] view. The possible values are "absolute", "conditional", "conditional absolute", and "unknown" based on the values in the [net_rate_abs], [net_rate_cond], [net_vol_abs], [net_vol_cond] columns.'),

("LuRegulatoryStatus", "To be added"),

("LuSourceType", "This table contains the source type characteristics listed in the HydroBase Data Dictionary Appendix. These values are currently not used in the HydroBase WaDE data."),

("LuState", "To be added"),

("LuUnits", "This table is based on the units used within the [vw_CDSS_NetAmts] view, which specify both cubic feet per second and acre feet per year."),

("LuValueType", "To be added"),

("LuWaterSupplyType", "To be added"),

("Organization", "Organization responsible for the data reported."),

("DataSources", "To be added"),

("Methods", "To be added"),

("Report", "Header for the water summary or water detail report."),

("GeospatialRef", "Header for the Geospatial Information related to the report."),

("ReportingUnit", "The Unit for which the Allocation or Estimate is being reported"),

("SummaryAvailabilility", "Summary of water availability within the reporting unit."),

("SAvailabilityAmount", "Estimate of the water availability for the given time frame as either a volume amount or a relative metric."),

("SAvailabilityMetric", "Metric measuring relative availability of water within this reporting unit."),

("SummaryAllocation", "Annual summary of water allocations within the reporting unit."),

("SAllocationIrrigation", "Additional Metadata for irrigation water supply uses"),

("SummaryUse", "Annual summary of water use within the reporting unit"),

("SUseIrrigation", "Additional Metadata for irrigation water supply uses"),

("SUseAmount", "Amount of water used"),

("SummaryWaterSupply", "Summary of derived water supply within the reporting unit for the reporting year."),

("SWaterSupplyAmount", "Water supply summaries for the specified time frame"),

("SummaryRegulatory", "Summary of regulatory status for the reporting unit."),

("DetailAllocation", "Detailed, site specific information on water allocations, diversions, use, and return flows."),

("DAllocationLocation", "The Location of the detailed allocation, diversion, use, or return flow."),

("DAllocationFlow", "Defines the amount of water attributed to the entire allocation.  If an allocation has diversions associated with it, then report this information for each diversion."),

("DAllocationUse", "Beneficial use for which the water is used."),

("DAllocationActual", "The actual amount of water diverted at this diversion for the reporting period."),

("DetailDiversion", "Description of the location for the diverted water."),

("DDiversionFlow", "Defines the amount of water attributed to the entire allocation.  If an allocation has diversions associated with it, then report this information for each diversion."),

("DDiversionUse", "Beneficial use for which the water is used."),

("DDiversionActual", "The actual amount of water diverted at this diversion for the reporting period."),

("DetailUse", "Information about the use of the water"),

("DUseLocation", "The location of the detailed allocation, diversion, use, or return flow"),

("DConsumptiveUse", "Estimate of water use"),

("DCommunityWaterSupply", "Additional Metadata for community water supply uses."),

("DIrrigation", "Additional Metadata for irrigation water supply uses"),

("DThermoelectric", "Additional Metadata for thermoelectric water supply uses."),

("DUseAmount", "The actual volume of water diverted at this diversion for the reporting period."),

("DetailReturnFlow", "The amount and location of water returned"),

("DReturnFlowActual", "Web Feature Service feature reference for the return flow")

]

"""
It is recommended that you print only one template at a time to copy the output 
and place it on the proper file
"""

for title, description in titles:
    print model_template % {'lowercase': title.lower(), 'uppercase': title, 'uppersplitted': upper_splitted(title)}
    #print requests_template % {'lowercase': title.lower(), 'uppercase': title}
    #print model_resource_template % {'lowercase': title.lower(), 'uppercase': title, 'lfirst': lfirst(title)}
    #print model_resource_register_template % {'lowercase': title.lower(), 'uppercase': title, 'lfirst': lfirst(title)}
    #print reset_db_template % {'lowercase': title.lower(), 'uppercase': title, 'lfirst': lfirst(title)}
    #print data_migration_template % {'lowercase': title.lower(), 'uppercase': title, 'lfirst': lfirst(title), 'description': description }



