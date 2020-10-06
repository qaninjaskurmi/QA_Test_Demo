from locust import HttpUser, User, task, between

def get_statements(htu):
    for i in allRows:
        print("data keyword: " + i[0])

        url="/statements?account_id="
        data_path = i[0].strip()
        response = htu.client.get(url+data_path)

        print("Response status code:", response.status_code)
        print("Response content:", response.text)

class MyUser(HttpUser):
    @task
    def load_statements_page(self):
        # load test csv data to send to face api
        global allRows
        allRows = []
        # open file to read
        with open("account_ids.csv", 'r') as csvfile:
            # iterate on all line
            for line in csvfile:
                data = line.split(',')
                allRows.append(data)
        get_statements(self)
    wait_time = between(5.0, 9.0)