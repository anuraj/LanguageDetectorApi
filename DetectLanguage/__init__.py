import logging
import json
import azure.functions as func
from langdetect import detect

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
        response = []
        for blurb in req_body:
            title = blurb.get('title')
            description = blurb.get('description')
            titleLanguage = detect(title)
            descriptionLanguage = detect(description)
            data = {}
            data["title"] = title
            data["titleLanguage"] = titleLanguage
            data["description"] = description
            data["descriptionLanguage"] = descriptionLanguage
            response.append(data)

        return func.HttpResponse(json.dumps(response))

    except Exception as e:
        return func.HttpResponse(
             "Invalid input - " + str(e),
             status_code=400
        )