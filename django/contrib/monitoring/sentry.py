try:
	import sentry_sdk
except ImportError:
	print("Warning, you don't have the Sentry SDK installed.")
	sentry_sdk = None

sentry_dsn = os.environ.get('SENTRY_DSN', '')
if not sentry_dsn:
	print("Warning, you don't SENTRY_DSN set.")

if not(sentry_sdk and sentry_dsn):
	print("To configure Sentry for application monitoring, visit https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#monitoring")

else:
	from sentry_sdk.integrations.django import DjangoIntegration

	sentry_sdk.init(
		dsn=sentry_dsn,
		integrations=[DjangoIntegration()],

		# Set traces_sample_rate to 1.0 to capture 100%
		# of transactions for performance monitoring.
		# We recommend adjusting this value in production,
		traces_sample_rate=1.0,

		# If you wish to associate users to errors (assuming you are using
		# django.contrib.auth) you may enable sending PII data.
		send_default_pii=True,

		# By default the SDK will try to use the SENTRY_RELEASE
		# environment variable, or infer a git commit
		# SHA as release, however you may want to set
		# something more human-readable.
		# release="myapp@1.0.0",
	)
