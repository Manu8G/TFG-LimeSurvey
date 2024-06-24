import base64  
import json
from LimeAPI import Api

user = "manuel"
password = "1234Lime"
url = "http://localhost/limesurvey/index.php/admin/remotecontrol"

lime = Api(url, user, password)

sid = 'sid'
token = 'token'

data_resp = {
    'token': token,
    '999729X44X2131111': "fabio_test_update_response"
}

resu = lime.update_response(sid, json.dumps(data_resp))

print ("END EXAMPLE UPDATE_RESPONSE")