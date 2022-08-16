from sentry_sdk.integrations.logging import LoggingIntegration
import logging
import sentry_sdk
import os


# configura o sistema de logs
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    handlers=[logging.FileHandler('app/logs.log', 'a')]
    )

# cria o logger
logger = logging.getLogger()


# Configura o sentry se houver uma dsn nas 
# variaveis de ambiente
dsn = os.getenv("SENTRY_DSN")
if dsn:

    # configura logs com o sentry
    sentry_logging = LoggingIntegration(
        level=logging.INFO,
        event_level=logging.INFO
    )

    sentry_sdk.init(
        dsn=dsn,
        integrations=[sentry_logging]
    )