import sys
sys.path.append('./')
from demo import api_function

class TestAPI:
    def test_ping_1(self):
        response_code = api_function.curl_github()
        assert response_code == 200, "Test failed"
        
    def test_ping_2(self):
        response_code = api_function.curl_github_bad()
        assert response_code == 200, "Test failed"
    
        