# [Khonsu the Car Chatbot]([https://car-chatbot.streamlit.app](https://khonsu.streamlit.app))

A simple chat interface that answers questions about cars using a Neo4j database and GPT-3.5 Turbo, complete with conversational history.

## Screenshot

<img width="1107" alt="image" src="https://github.com/Amloner/Khonsu-the-Car-Chatbot/assets/124287518/a05fdd47-788f-40c2-9d7f-c84c6e672d94">

## Usage

Khonsu helps users find cars by specific features. It can also find similar cars or compare two cars (though this feature is buggy and works occasionally). With further improvements, this chatbot can be used by used car dealers to quickly find multiple cars based on customer requirements.

## Neo4j Database

The database was created using this [dataset](https://www.kaggle.com/datasets/CooperUnion/cardataset) from Kaggle and deployed in Neo4j's AuraDB. It contains details about cars including, but not limited to, manufacturer, year of manufacture, size, style, number of doors, and transmission. These details were appropriately converted into labels, relationships, and properties.

## Chatbot

The chatbot mainly functions using the Streamlit and LangChain libraries of Python. Streamlit is used for UI development, and the LLM of OpenAI is used in conjunction with our database to help answer questions with respect to our database. LangChain has been configured to ensure that the LLM only provides actually available data and does not produce hallucinations.

## Issues

- **Model**: The chatbot currently uses GPT-3.5 Turbo due to fiscal constraints. However, results can be significantly improved by using newer GPT models.
- **Accuracy**: Frequently, the LLM outputs that it does not know the answer even though LangChain has provided the relevant details from the database.
- **Autocapitalization**: There are issues with auto-capitalization of words in queries, leading to false negative answers.
