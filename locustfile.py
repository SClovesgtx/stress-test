from locust import HttpUser, task, tag,  events


@events.init_command_line_parser.add_listener
def _(parser):
    parser.add_argument("--model-id", type=str, env_var="MODEL_ID", include_in_web_ui=True, default="", help="The model id of trained ML model from Omni NLU API")
    parser.add_argument("--access-token", type=str, env_var="ACCESS_TOKEN", include_in_web_ui=True, default="", help="The Access Token of Omni NLU API")

class LocustTest(HttpUser):

    @task(1)
    @tag("making prediction")
    def predict(self):
        self.client.post(
            url=f"models/{self.environment.parsed_options.model_id}/predict",
            json={
                "message": "quero fazer uma compra de café",
                "similarity_threshold": 90,
            },
            headers={"Authorization": f"Bearer {self.environment.parsed_options.access_token}"},
        )