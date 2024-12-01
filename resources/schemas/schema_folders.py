'''
Schema for Folders
'''
from voluptuous import Schema, PREVENT_EXTRA, Any


''' GET /v2/folders '''
valid_folders = Schema([
                        {
                        "id": str,
                        "name": str,
                        "hasChildren": bool,
                        "childrenCount": int,
                        "parentId": Any(None, str),
                        "modifiedBy": str,
                        "idPath": str,
                        "namePath": str,
                        "permissions": Any([], [str]),
                        "favourite": bool,
                        "midpWithKits": bool,
                        "canChangeMidpWithKits": bool,
                        "childrenHaveMidpWthKits": bool,
                        "midpWithBimModels": bool,
                        "canChangeMidpWithBimModels": bool,
                        "childrenHaveMidpWthBimModels": bool
                        }
                       ],
extra=PREVENT_EXTRA,
required=True
)


''' GET /v2/folders/{folderId} '''
valid_folder = Schema(
                        {
                        "id": str,
                        "name": str,
                        "hasChildren": bool,
                        "childrenCount": int,
                        "parentId": Any(None, str),
                        "modifiedBy": str,
                        "idPath": str,
                        "namePath": str,
                        "permissions": Any([], [str]),
                        "favourite": bool,
                        "midpWithKits": bool,
                        "canChangeMidpWithKits": bool,
                        "childrenHaveMidpWthKits": bool,
                        "midpWithBimModels": bool,
                        "canChangeMidpWithBimModels": bool,
                        "childrenHaveMidpWthBimModels": bool
                        },
extra=PREVENT_EXTRA,
required=True
)
