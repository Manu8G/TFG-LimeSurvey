from limesurveyrc2api.limesurvey import LimeSurvey

url = "http://localhost/limesurvey/index.php/admin/remotecontrol"
username = "manuel"
password = "1234Lime"

api = LimeSurvey(url=url, username=username)
api.open(password=password)

result = api.survey.list_surveys()
for survey in result:
    print(survey.get("sid"))

api.close()