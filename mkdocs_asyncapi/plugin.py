import logging

from mkdocs.plugins import BasePlugin

log = logging.getLogger(f"mkdocs.plugins.{__name__}")

class AsyncApiPlugin(BasePlugin):

    def on_post_page(self, output, page, config, **kwargs):
        """sdf"""
        log.info("Hello World.")

        