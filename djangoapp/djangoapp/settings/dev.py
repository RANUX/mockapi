
# WARNING: Set to False in production
CORS_ORIGIN_ALLOW_ALL = True

# WARNING: Don't use this key in production!
SECRET_KEY = 'y4!2#=i&^4u46xla^a&edsog)52__vv!!((5jk#j7)q=0w=9*t'

DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Run server fake smpt server: python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
