from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from django.db import models


class ControlledVocabulary(models.Model):
    CURRENT = 'Current'
    ARCHIVED = 'Archived'

    STATUS_CHOICES = (
        (CURRENT, 'Current'),
        (ARCHIVED, 'Archived')
    )

    vocabulary_id = models.AutoField(primary_key=True)
    term = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    definition = models.TextField()
    category = models.CharField(max_length=255, blank=True)
    provenance = models.TextField(blank=True)
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True)
    note = models.TextField(blank=True, null=True)
    vocabulary_status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    previous_version = models.OneToOneField('self', null=True, related_name='revised_version')

    def has_revision(self):
        revision = None
        try:
            revision = self.revised_version
        except ObjectDoesNotExist:
            pass
        return revision is not None

    def get_latest_version(self):
        term = self
        while term.has_revision():
            term = term.revised_version
        return term

    class Meta:
        db_table = 'controlledvocabularies'
        ordering = ["-name"]


class ControlledVocabularyRequest(models.Model):
    PENDING = 'Pending'
    REJECTED = 'Rejected'
    ACCEPTED = 'Accepted'
    ARCHIVED = 'Archived'

    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (REJECTED, 'Rejected'),
        (ACCEPTED, 'Accepted'),
        (ARCHIVED, 'Archived'),
    )

    request_id = models.AutoField(max_length=255, db_column='requestId', primary_key=True)

    term = models.CharField(max_length=255, help_text="Please enter a URI-friendly version of your term with no spaces, special characters, etc.")
    name = models.CharField(max_length=255, help_text="Please enter the term as you would expect it to appear in a sentence.")
    definition = models.TextField(help_text="Please enter a detailed definition of the term.", blank=True)
    provenance = models.TextField(blank=True, help_text="Enter a note about where the term came from. If you retrieved the definition of the term from a website or other source, note that here.")
    provenance_uri = models.URLField(db_column='provenanceUri', blank=True, max_length=1024, help_text="If you retrieved the term from another formal vocabulary system, enter the URI of the term from the other system here.")
    note = models.TextField(blank=True, null=True, help_text="Please enter any additional notes you may have about the term.")
    category = models.CharField(max_length=255, blank=True, help_text="You may suggest a category for the term. Refer to the vocabulary to see which categories have been used. You may also suggest a new category.")

    status = models.CharField(max_length=255, db_column='status', choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    date_submitted = models.DateField(db_column='dateSubmitted', default=timezone.now)
    date_status_changed = models.DateField(db_column='dateStatusChanged', default=timezone.now)
    request_notes = models.TextField(db_column='requestNotes', blank=True)
    submitter_name = models.CharField(max_length=255, db_column='submitterName', help_text="Enter your name.")
    submitter_email = models.CharField(max_length=255, db_column='submitterEmail', help_text="Enter your email address.")
    request_reason = models.TextField(db_column='requestReason', help_text="Please enter a brief description of the reason for your submission (e.g., Term does not exist yet, Term is needed for my data use case, etc.)")

    request_for = models.ForeignKey('ControlledVocabulary', db_column='requestFor', blank=True, null=True)
    original_request = models.ForeignKey('self', db_column='originalRequestId', null=True)

    class Meta:
        db_table = 'requests'
        ordering = ["date_submitted", "-request_id"]


class MethodType(ControlledVocabulary):
    class Meta:
        db_table = 'methodtypecv'
        verbose_name = 'Method Type'
        ordering = ["name"]


class MethodTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'methodtypecvrequests'
        verbose_name = 'Method Type Request'


class AggregationStatistic(ControlledVocabulary):
    class Meta:
        db_table = 'aggregationstatisticcv'
        verbose_name = 'Aggregation Statistic'


class AggregationStatisticRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'aggregationstatisticcvrequests'
        verbose_name = 'Aggregation Statistic Request'


class ElevationDatum(ControlledVocabulary):
    class Meta:
        db_table = 'elevationdatumcv'
        verbose_name = 'Elevation Datum'


class ElevationDatumRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'elevationdatumcvrequests'
        verbose_name = 'Elevation Datum Request'


class SeasonName(ControlledVocabulary):
    class Meta:
        db_table = 'seasonnamecv'
        verbose_name = 'Season Name'


class SeasonNameRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'seasonnamecvrequests'
        verbose_name = 'Season Name Request'


class Units(ControlledVocabulary):
    abbreviation = models.CharField(max_length=255, blank=True, null=False, db_column='UnitsAbbreviation',
        help_text='Please enter the Abbreviation of the unit (e.g., "m" for meter)')
    unit_system = models.CharField(max_length=255, blank=True, db_column='UnitsSystem',
        help_text='English or International System of Units')
    # conversion_factor = models.FloatField(null=True, blank=True, 
    #     db_column='ConversionFactor', default=0)
    linear_factor =  models.TextField(null=True,
        db_column='LinearFactor')
    constant_factor =  models.TextField(null=True,
        db_column='ConstantFactor')

    class Meta:
        db_table = 'unitscv'
        verbose_name = 'Units'
        ordering = ["name"]


class UnitsRequest(ControlledVocabularyRequest):
    abbreviation = models.CharField(max_length=255, blank=True, null=False, db_column='UnitsAbbreviation',
        help_text='Please enter the Abbreviation of the unit (e.g., "m" for meter)')
    unit_system = models.CharField(max_length=255, blank=True, db_column='UnitsSystem',
        help_text='English or International System of Units')
    linear_factor =  models.TextField(null=True,
        db_column='LinearFactor')
    constant_factor =  models.TextField(null=True,
        db_column='ConstantFactor')
    class Meta:
        db_table = 'unitscvrequests'
        verbose_name = 'Units Request'


class ObjectTypology(ControlledVocabulary):
    class Meta:
        db_table = 'objecttypologycv'
        verbose_name = 'Object Typology'


class ObjectTypologyRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'objecttypologycvrequests'
        verbose_name = 'Object Typology Request'


class AttributeName(ControlledVocabulary):
    class Meta:
        db_table = 'attributenamecv'
        verbose_name = 'Attribute Name'


class AttributeNameRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'attributenamecvrequests'
        verbose_name = 'Attribute Name Request'


class AttributeDataType(ControlledVocabulary):
    class Meta:
        db_table = 'attributedatatypecv'
        verbose_name = 'Attribute Data Type'


class AttributeDataTypeRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'attributedatatypecvrequests'
        verbose_name = 'Attribute Data Type Request'


class ElectronicFileFormat(ControlledVocabulary):
    class Meta:
        db_table = 'electronicfileformatcv'
        verbose_name = 'Electronic File Format'


class ElectronicFileFormatRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'electronicfileformatcvrequests'
        verbose_name = 'Electronic File Format Request'


class SpatialReference(ControlledVocabulary):
    class Meta:
        db_table = 'spatialreferencecv'
        verbose_name = 'Spatial Reference'


class SpatialReferenceRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'spatialreferencecvrequests'
        verbose_name = 'Spatial Reference Request'


class InstanceName(ControlledVocabulary):
    class Meta:
        db_table = 'instancenamecv'
        verbose_name = 'Instance Name'


class InstanceNameRequest(ControlledVocabularyRequest):
    class Meta:
        db_table = 'instancenamecvrequests'
        verbose_name = 'Instance Name Request'


class ObjectType(ControlledVocabulary):
    object_typology = models.CharField(max_length=255, null=False, blank=True)
    class Meta:
        db_table = 'objecttypecv'
        verbose_name = 'Object Type'


class ObjectTypeRequest(ControlledVocabularyRequest):
    object_typology = models.CharField(max_length=255, null=False, blank=True)
    class Meta:
        db_table = 'objecttypecvrequests'
        verbose_name = 'Object Type Request'


class Categorical(ControlledVocabulary):
    attribute_name = models.CharField(max_length=255, null=False, blank=True,
        help_text="Please select a controlled Attribute Name that this value belongs to. " \
        "If the Attribute Name does not exist, please add it in the Attribute Name table")
    class Meta:
        db_table = 'categoricalcv'
        verbose_name = 'Categorical'


class CategoricalRequest(ControlledVocabularyRequest):
    attribute_name = models.CharField(max_length=255, null=False, blank=True,
        help_text="Please select a controlled Attribute Name that this value belongs to. " \
        "If the Attribute Name does not exist, please add it in the Attribute Name table")
    class Meta:
        db_table = 'categoricalcvrequests'
        verbose_name = 'Categorical Request'
