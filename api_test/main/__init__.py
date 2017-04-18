from api_test.main.app_init import app as my_app
from api_test.apis.api_user import *
from api_test.apis.api_terrain import *

if __name__ == "__main__":
    my_app.run(debug=True)
