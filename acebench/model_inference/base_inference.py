import json
from pathlib import Path

class BaseHandler:
    model_name: str

    def __init__(self, model_name, model_path=None, temperature=0.7, top_p=1, max_tokens=1000, language = "zh") -> None:
        self.model_name = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.language = language

    def inference(self, prompt, functions, test_category):
        # This method is used to retrive model response for each model.
        pass


    def write_result(self, result, model_name, result_path):
        result_dir = Path(result_path) / model_name
        result_dir.mkdir(parents=True, exist_ok=True)

        if type(result) is dict:
            result = [result]

        for entry in result:
            if "normal_multi_turn" not in entry["id"]:
                test_category = entry["id"].rsplit("_", 1)[0]
            else:
                test_category = "_".join(entry["id"].split("_")[:-2])
            file_to_write = result_dir / f"data_{test_category}_result.json"

            with file_to_write.open("a+", encoding="utf-8") as f:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
