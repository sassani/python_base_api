""" Application entry point """
from src.application import create_app, create_settings

# pylint: disable=unused-import, wrong-import-position, E0611
APP_SETTINGS = create_settings()
APP = create_app(APP_SETTINGS)
import src.core.controllers.routes
