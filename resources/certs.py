cert_path = 'resources/certsData'

admin_cert = (f'{cert_path}/admin_cert.pem', f'{cert_path}/admin_key.pem')
business_admin_cert = (f'{cert_path}/business_admin_cert.pem', f'{cert_path}/business_admin_key.pem')
access_admin_cert = (f'{cert_path}/access_admin_cert.pem', f'{cert_path}/access_admin_key.pem')
user_cert = (f'{cert_path}/user_cert.pem', f'{cert_path}/user_key.pem')
unauthorized_cert = (f'{cert_path}/401_cert.pem', f'{cert_path}/401_key.pem')

hprn_03 = (f'{cert_path}/access_admin_cert_old.pem', f'{cert_path}/access_admin_key_old.pem')


ROLES = {
    'project_admin': admin_cert,
    'user': user_cert,
    'business_admin': business_admin_cert,
    'access_admin': access_admin_cert,
    'external_project_admin': "Sorry, I don't have cert"
}
