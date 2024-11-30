from resources.static_data import *


url_base = 'https://cde-ift.stroika.tech/api'
external_url_base = 'https://tvlsg-dsc000006.delta.sbrf.ru/bim/api'

url_get_me = f'https://ksup-bim.ift.delta.sbrf.ru/bim/'






#################################################################
#                  Account   v2/accounts                        #
#                            v2/accounts-with-admins            #
#                            v2/accounts-with-admins/archived   #                  
#################################################################
url_accounts = f'{url_base}/v2/accounts'
url_accounts_with_admins = f'{url_base}/v2/accounts-with-admins'
url_accounts_with_admins_archived = f'{url_base}/v2/accounts-with-admins/archived'


#################################################################
#                    Approval   /v2/approvals                   #
#                               /v2/approval-history            #
#                               /v2/approval/status             #
#################################################################
url_approvals = f'{url_base}/v2/approvals'
url_approval_history = f'{url_base}/v2/approval-history'
url_approvals_status = f'{url_base}/v2/approvals/status'


#################################################################
#             ApprovalStage /v2/approval-stages                 #
#                           /v2/approval-stages/archived        #
#################################################################
url_approval_stages = f'{url_base}/v2/approval-stages'
url_approval_stages_archived = f'{url_base}/v2/approval-stages/archived'


#################################################################
#             ApprovalRoute /v2/approval-routes                 #
#                           /v2/approval-routes/archived        #
#################################################################
url_approval_routes = f'{url_base}/v2/approval-routes'
url_approval_routes_archived = f'{url_base}/v2/approval-routes/archived'


#################################################################
#       ApprovalRouteAssignment /v2/approval-assignments        #
#################################################################
url_approval_assignments = f'{url_base}/v2/approval-assignments'


#################################################################
#                          Bin   v2/bin                         #
#                                v2/bin-items                   #
#################################################################
url_bin = f'{url_base}/v2/bin'
url_bin_items = f'{url_base}/v2/bin-items'


#################################################################
#               BulkDownload   v2/bulk-download                 #
#                              v2/bulk-download-size            #
#                              v2/bulk-download-prepare         #
#################################################################
url_bulk_download = f'{url_base}/v2/bulk-download'
url_bulk_download_size = f'{url_base}/v2/bulk-download-size'
url_bulk_download_prepare = f'{url_base}/v2/bulk-download-prepare'


#################################################################
#        FilenameTemplate    v2/filename-templates              #
#                            v2/filename-templates/download     #         
#################################################################
url_filename_templates = f'{url_base}/v2/filename-templates'
url_filename_templates_download = f'{url_base}/v2/filename-templates/download'


#################################################################
#                 FilenameTemplateAssignments                   #
#             v2/filename-templates-assignments                 #       
#################################################################
url_filename_templates_assignments = f'{url_base}/v2/filename-templates-assignments'


#################################################################
#            IssueAccesses     v2/issue-accesses                #
#                              v2/issue-permissions             #
#                              v2/issue-access-levels           #
#################################################################
url_issue_accesses = f'{url_base}/v2/issue-accesses'
url_issue_permissions = f'{url_base}/v2/issue-permissions'
url_issue_access_levels = f'{url_base}/v2/issue-access-levels'


#################################################################
#                IssueAccess    v2/issue-accesses               #
#################################################################
url_issue_accesses = f'{url_base}/v2/issue-accesses'


#################################################################
#             IssueCategory    v2/issue-categories              #
#################################################################
url_issue_categories = f'{url_base}/v2/issue-categories'


#################################################################
#                  IssueType    v2/issue-types                  #
#################################################################
url_issue_types = f'{url_base}/v2/issue-types'


#################################################################
#         IssueAttribute    v2/issue-default-attributes         #
#                           v2/issue-custom-attributes          #
#################################################################
url_issue_default_attributes = f'{url_base}/v2/issue-default-attributes'
url_issue_custom_attributes = f'{url_base}/v2/issue-custom-attributes'


#################################################################
#                 Location    v2/issue-locations                #
#################################################################
url_issue_locations = f'{url_base}/v2/issue-locations'


#################################################################
#                      Issue    v2/issues                       #
#                               v2/issues/search                #
#                               v2/issue-filters                #
#                               v2/issue-history                #
#                               v2/issues/status                #
#################################################################
url_issues = f'{url_base}/v2/issues'
url_issues_search = f'{url_base}/v2/issues/search'
url_issue_filters = f'{url_base}/v2/issue-filters'
url_issue_history = f'{url_base}/v2/issue-history'
url_issues_status = f'{url_base}/v2/issues/status'


#################################################################
#              IssueComments    v2/issues-comments              #
#################################################################
url_issue_comments = f'{url_base}/v2/issue-comments'


#################################################################
#              IssueAttachments   v2/issues-documents           #
#################################################################
url_issue_documents = f'{url_base}/v2/issue-documents'


#################################################################
#                      Folder    v2/folders                     #
#                                v2/folders/search              #
#                                v2/folders/move                #
#                                v2/folders/copy                #
#################################################################
url_folders = f'{url_base}/v2/folders'
url_folders_search = f'{url_base}/v2/folders/search'
url_folders_move = f'{url_base}/v2/folders/move'
url_folders_copy = f'{url_base}/v2/folders/copy'


#################################################################
#            FolderUserAccess    v2/access-users                #
#                                v2/access-folders              #
#                                v2/folder-user-permissions     #
#                                v2/folder-access-levels        #
#################################################################
url_access_users = f'{url_base}/v2/access-users'
url_access_folders = f'{url_base}/v2/access-folders'
url_folder_user_permissions = f'{url_base}/v2/folder-user-permissions'
url_folder_access_levels = f'{url_base}/v2/folder-access-levels'


#################################################################
#                  Document    v2/documents                     #
#                              v2/documents/filters             #
#                              v2/documents/filters/folders     #
#                              v2/documents/move                #
#                              v2/documents/copy                #
#                              v2/documents/check-upload        #
#                              v2/documentation                 #
#################################################################
url_documents = f'{url_base}/v2/documents'
url_documents_filters = f'{url_base}/v2/documents/filters'
url_documents_filters_folders = f'{url_base}/v2/documents/filters/folders'
url_documents_move = f'{url_base}/v2/documents/move'
url_documents_copy = f'{url_base}/v2/documents/copy'
url_documents_optimize = f'{url_base}/v2/documents/optimize'
url_documents_check_upload = f'{url_base}/v2/documents/check-upload'
url_documentation = f'{url_base}/v2/documentation'


#################################################################
#                    Discipline    v2/disciplines               #
#################################################################
url_disciplines = f'{url_base}/v2/disciplines'


#################################################################
#               FilenameBlocks    v2/filename-blocks            #
#################################################################
url_filename_blocks = f'{url_base}/v2/filename-blocks'


#################################################################
#                       login / confirm                         #
#################################################################
url_login = f'{url_base}/v2/login'
url_confirm = f'{url_base}/v2/confirm'

#################################################################
#                      Project    v2/projects                   #
#                                 v2/projects/archived          #
#################################################################
url_projects = f'{url_base}/v2/projects'
url_projects_archived = f'{url_base}/v2/projects/archived'


#################################################################
#            ProjectCompanies  v2/project-companies             #
#                              v2/project-companies/archived    #
#################################################################
url_project_companies = f'{url_base}/v2/project-companies'
url_project_companies_archived = f'{url_base}/v2/project-companies/archived'


#################################################################
#                 ProjectUser  v2/project-users                 #
#                              v2/project-users/archived        #
#                              v2/project-users/access-levels   #
#                              v2/sber-project-users            #
#################################################################
url_project_users = f'{url_base}/v2/project-users'
url_project_users2 = f'{url_base}/v2/project-users2'
url_project_users_archived = f'{url_base}/v2/project-users/archived'
url_project_users_access_levels = f'{url_base}/v2/project-users/access-levels'
url_sber_project_users = f'{url_base}/v2/sber-project-users'


#################################################################
#                   Revisions    v2/revisions                   #
#                                v2/revisions/activate          #
#                                v2/revisions/pages             #
#                                v2/revisions/pages/preview     #
#                                v2/revisions/pages/thumbnail   #
#                                v2/revisions/tiles             #
#                                v2/revision-comments           #
#                                v2/revision-comment-replies    #
#################################################################
url_revisions = f'{url_base}/v2/revisions'
url_revisions_activate = f'{url_base}/v2/revisions/activate'
url_revisions_pages = f'{url_base}/v2/revisions/pages'
url_revisions_pages_preview = f'{url_base}/v2/revisions/pages/preview'
url_revisions_pages_thumbnail = f'{url_base}/v2/revisions/pages/thumbnail'
url_revisions_tiles = f'{url_base}/v2/revisions/tiles'
url_revision_comments = f'{url_base}/v2/revision-comments'
url_revision_comment_replies = f'{url_base}/v2/revision-comment-replies'


#################################################################
#                        User     v2/users                      #
#                                 v2/users/me                   #
#################################################################
url_users = f'{url_base}/v2/users'
url_users_me = f'{url_base}/v2/users/me'




######################################################################################################################################################
#                                                                      ADMIN                                                                         #
######################################################################################################################################################

#################################################################
#                      Account  admin/v2/accounts               #
#                               admin/v2/accounts/archive       #
#################################################################
url_admin_accounts = f'{url_base}/admin/v2/accounts'
url_admin_accounts_archive = f'{url_base}/admin/v2/accounts/archive'


#################################################################
#                      User     admin/v2/admins                 #
#                               admin/v2/admins/blocked         #
#################################################################
url_admin_admins = f'{url_base}/admin/v2/admins'
url_admin_admins_blocked = f'{url_base}/admin/v2/admins/blocked'

#################################################################
#                    User   admin/v2/system-roles               #
#################################################################
url_admin_system_roles = f'{url_base}/admin/v2/system-roles'

#################################################################
#                     User   admin/v2/ldap-users                #
#################################################################
url_admin_ldap_users = f'{url_base}/admin/v2/ldap-users'

#################################################################
#                      User     admin/v2/users                  #
#                               admin/v2/users/blocked          #
#################################################################
url_admin_users = f'{url_base}/admin/v2/users'
url_admin_users_blocked = f'{url_base}/admin/v2/users/blocked'

#################################################################
#                      Audit    admin/v2/events                 #
#                               admin/v2/event-types            #
#                               admin/v2/event-object-types     #
#################################################################
url_events = f'{url_base}/admin/v2/events'
url_event_types = f'{url_base}/admin/v2/event-types'
url_event_object_types = f'{url_base}/admin/v2/event-object-types'
