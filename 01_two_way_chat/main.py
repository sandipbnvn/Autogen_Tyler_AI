import autogen
import dotenv
import os


def main():
    config_list = autogen.config_list_from_json(
        env_or_file="OAI_CONFIG_LIST.json"
    )
    dotenv.load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    config_list[0]['api_key'] = OPENAI_API_KEY

    assistant = autogen.AssistantAgent(
        name="Assistant",
        llm_config={
            "config_list": config_list
        }
    )

    user_proxy = autogen.UserProxyAgent(
        name="user",
        human_input_mode="ALWAYS",
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False
        }
    )

    user_proxy.initiate_chat(assistant, message="Give me weather for 4 metros in India")


if __name__ == "__main__":
    main()