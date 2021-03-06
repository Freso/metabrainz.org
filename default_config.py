# -*- coding: utf-8 -*-
# DEFAULT CONFIGURATION

SECRET_KEY = "CHANGE_THIS"


# DATABASE
SQLALCHEMY_DATABASE_URI = "postgresql://metabrainz:metabrainz@db:5432/metabrainz"
SQLALCHEMY_TRACK_MODIFICATIONS = False


# REPLICATION PACKETS
# Hourly replication packets must be located in this directory.
REPLICATION_PACKETS_DIR = "/data/replication_packets"
JSON_DUMPS_DIR = "/data/json_dumps"


# PAYMENTS

PAYMENT_PRODUCTION = False

PAYPAL_ACCOUNT_IDS = {
    "USD": "",
    "EUR": "",
}
PAYPAL_BUSINESS = ""

STRIPE_KEYS = {
    "SECRET": "",
    "PUBLISHABLE": "",
}
STRIPE_TEST_KEYS = {
    "SECRET": "",
    "PUBLISHABLE": "",
}


# REDIS
REDIS = {
    "host": "redis",
    "port": 6379,
    "namespace": "MEB",
}


# MUSICBRAINZ OAUTH

MUSICBRAINZ_BASE_URL = "https://musicbrainz.org/"
MUSICBRAINZ_CLIENT_ID = ""
MUSICBRAINZ_CLIENT_SECRET = ""


# MISC

# Mail server
SMTP_SERVER = "metabrainz-mail"
SMTP_PORT = 25
MAIL_FROM_DOMAIN = "metabrainz.org"

ADMINS = []

RECAPTCHA_PUBLIC_KEY = ""
RECAPTCHA_PRIVATE_KEY = ""

NOTIFICATION_RECIPIENTS = []

USE_COMPILED_STYLING = True

BEHIND_GATEWAY = True
REMOTE_ADDR_HEADER = "X-MB-Remote-Addr"

USE_NGINX_X_ACCEL = False
