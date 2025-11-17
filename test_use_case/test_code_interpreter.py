from dotenv import load_dotenv
load_dotenv()
from e2b_code_interpreter import Sandbox
import time
import os

template_id = os.getenv("TEMPLATE_ID")

def main():
    sbx = Sandbox(template=template_id, timeout=3600) # By default the sandbox is alive for 5 minutes
    print(sbx.sandbox_id)
    time.sleep(1)
    execution = sbx.run_code("print('hello world')") # Execute Python inside the sandbox
    print(execution.logs)

    files = sbx.files.list("/")
    print(files)

if __name__ == "__main__":
    main()