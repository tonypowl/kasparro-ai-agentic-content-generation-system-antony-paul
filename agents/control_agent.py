from data.sample_data import PRODUCT_DATA
from agents.parsing_agent import ParsingAgent
from agents.content_agent import ContentAgent
from agents.page_format_agent import PageFormatAgent


class ControlAgent:
    def run(self):
        parsed = ParsingAgent().run(PRODUCT_DATA)
        content = ContentAgent().run(parsed)
        PageFormatAgent().run(parsed, content)
