'''
Schema for Documents
'''
from voluptuous import Schema, PREVENT_EXTRA, Required, Any


classification_statuses = ('NOT_CARRIED_OUT', 'IN_CLASSIFICATION_QUEUE', 'TANGLE_ERROR', 'PARSING_ATTRIBUTE_ERROR',
                         'ERROR_BEFORE_CLASSIFICATION_COMPLETE', 'IN_CLASSIFICATION_PROGRESS', 'REQUIRES_CONFIRMATION',
                         'IN_MARKUP_QUEUE', 'IN_MARKUP_PROGRESS', 'PROJECT_CRITERIA_ERROR', 'ERROR_BEFORE_MARKUP_COMPLETE',
                         'NOT_PASSED', 'REQUIRES_ADJUSTMENT', 'PASSED')


''' GET /v2/documents/{documentId} '''
valid_document = Schema({
                        Required("id"): str,
                        Required("name"): str,
                        Required("version"): int,
                        Required("revisionId"): str,
                        Required("size"): int,
                        Required("canComment"): bool,
                        Required("created"): str,
                        Required("createdBy"): {
                                                Required("id"): str,
                                                Required("name"): str
                                                },
                        Required("modified"): str,
                        Required("modifiedBy"): {
                                                Required("id"): str,
                                                Required("name"): str
                                                },
                        Required("type"): str,
                        Required("folders"): [
                                                {
                                                Required("id"): Any(None, str),
                                                Required("namePath"): str,
                                                Required("permissions"): [str]
                                                }
                                            ],
                        Required("optimizationStatus"): str,
                        Required("ifc"): Any(None,
                                                   {  
                                                      Required("id"): str,
                                                      Required("status"): Any('IN_PROGRESS', 'ERROR', 'DONE'),
                                                      Required("error"): Any(None, str),
                                                      Required("model"): Any(None, str),
                                                      Required("version"): Any(None, str)
                                                   }
                                             ),
                        Required("classificationInfo"): Any(None, {
                                                                     Required("id"): str,
                                                                     Required("status"): Any(*classification_statuses),
                                                                     Required("classificationDate"): str,
                                                                     Required("classifiedElementsCount"): int,
                                                                     Required("percentOfElementsWithSameCodes"): int,
                                                                     Required("requiredCount"): int,
                                                                     Required("requiredAndConfirmedSum"): int,
                                                                     Required("elementsFromTanglCount"): int
                                                                     }
                                                            )
                        },                                  
extra=PREVENT_EXTRA,
required=True
)
