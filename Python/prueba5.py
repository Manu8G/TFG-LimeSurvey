from limesurveyrc2api.limesurvey import LimeSurvey

url = "http://localhost/limesurvey/index.php/admin/remotecontrol"
username = "manuel"
password = "1234Lime"

# Open a session.
api = LimeSurvey(url=url, username=username)
api.open(password=password)

# Get a list of surveys the admin can see, and print their IDs.
result = api.survey.list_surveys()
for survey in result:
    print(survey.get("sid"))

# Close the session.
api.close()