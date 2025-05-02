# DocsGPT

While OpenAI's ChatGPT is an extraordinary innovation, we can now also use OpenAI to query our own documents.

This is a very early demo app that uses OpenAI's GPT and LangChain [🦜🔗LangChain](https://langchain.com) to process and chat with your local PDF files. Note: Langchain docs have [helpful videos here](https://python.langchain.com/en/latest/youtube.html)

It comes preloaded with sample Amazon annual and shareholder reports in a ./files/ subfolder. You can start chatting with those or replace the files in the subfolder with your own PDFs

Load it onto your laptop and start asking the PDFs questions.  OpenAI's GPT 3.5-turbo analyzes and provides answers. See the demo screenshots below.


## Screenshots

[2023-04-19] This screenshot shows the Q&A after the PDFs are ingested. Each question is queried to the GPT 3.5-turbo API and the response is generated in real-time.

![Screenshot](https://github.com/alanwunsche/DocsGPT/blob/main/DocsGPT-Demo-CLI-2023-04-19-at-9.12.05%20PM.png)

## Installation

Open your Terminal application:

```git clone https://github.com/alanwunsche/DocsGPT.git```

```cd DocsGPT```

```pip install -r requirements.txt```

## Insert your OpenAI API Key

Rename the ```.env.template``` file to ```.env```

Obtain your own OpenAI API key at https://platform.openai.com

Insert your OpenAI API key into the ```.env``` file.  

## Add your own PDFs (Optional)

If you'd like to query your own PDFs, remove the files in the ```/files/``` folder and copy your PDFs to the ```/files/``` subfolder.

## Run the application
```python main.py```

## 💬Chat with your PDFs

### Example questions you can ask your PDFs:

What's the most profitable business line and how much did it earn in each of 2021 and 2022?

Provide a detailed analysis of how Covid impacted the business in each of the last 2 years 

Describe in depth the company's climate strategy over the past decade

Describe the expected business benefits of the company's climate plans for the upcoming decade

## Contact
Twitter: [@alanwunsche](https://twitter.com/alanwunsche)

## Notes
1. You may encounter a warning "detectron2 is not installed. Cannot use the hi_res partitioning strategy. Falling back to partitioning with the fast strategy." This warning will not prevent your app from working.

2. This is only a demo and may not produce accurate, reliable results.

3. On a MacOS, it's possible that a .DS_Store file gets added automatically to your ``` /files ``` folder.  If this happens, delete the folder and run this command to prevent the .DS_Store from being created : ``` defaults write com.apple.desktopservices DSDontWriteNetworkStores true ```
  You can then recreate the /files subfolder
  


