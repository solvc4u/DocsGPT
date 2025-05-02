from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator

import os

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY")

root_dir = "."

pdf_folder_path = f'{root_dir}/files/'
os.listdir(pdf_folder_path)

print()

loaders = [UnstructuredPDFLoader(os.path.join(pdf_folder_path, fn)) for fn in os.listdir(pdf_folder_path)]

# print(loaders)
print()


index = VectorstoreIndexCreator().from_loaders(loaders)

index

### Get questions from user, have OpenAI GPT-3.5-turbo process it and return a response.

while True:
    print()
    command = input("Enter a question ('exit' to quit): ")
    if command == 'exit':
        break
    else:
        print('Your question:\n',command)
        print()
        print('Answer: \n')
        print(index.query(command))
        print('---')
        print()
