"""
title: Mantis Issue Reader
author: ferencbon
repo: https://github.com/ferencbon/openwebui_components
version: 0.0.1
"""

import os
import requests
from datetime import datetime
from pydantic import BaseModel, Field


class Tools:
    class Valves(BaseModel):
        MANTIS_URL: str = Field(default="MANTIS_URL", description="Mantis root url.")
        MANTIS_API_KEY: str = Field(default="API_KEY", description="Mantis api key.")
        SHOW_DEBUG_INFORMATION: bool = Field(
            default=False, description="Show valve data when the HTTP code is not 200."
        )
        pass

    def __init__(self):
        self.citation = True
        self.valves = self.Valves()
        pass

    def get_issue_from_mantis(self, issue_id: str) -> str:
        url = f"{self.valves.MANTIS_URL}api/rest/issues/{issue_id}"
        headers = {
            "Authorization": f"{self.valves.MANTIS_API_KEY}",
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return f"The ticket deatils are: {response.json()}. Don't reference json variables or keys that users can't understand unless they specifically ask for them."
        else:
            if self.valves.SHOW_DEBUG_INFORMATION == True:
                return f"Error: {response.status_code}, {response.text}, show details:{self.valves}, {self.uservalves}"
            else:
                return f"Error: {response.status_code}, {response.text}"
