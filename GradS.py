import os
import json
import requests
import time
import ast
import pandas as pd
from dotenv import load_dotenv
import streamlit as st
from openai import AzureOpenAI
from azure.core.credentials import AzureKeyCredential
from azure.identity import get_bearer_token_provider
from azure.search.documents import SearchClient

def generate_client():
    load_dotenv()
    client = AzureOpenAI(
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key = os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-08-01-preview"
    )

    return client

def generate_search():
    load_dotenv()
    credential = AzureKeyCredential(os.getenv("AZURE_SEARCH_API_KEY"))
    search_client = SearchClient(
        endpoint = os.getenv("AZURE_SEARCH_SERVICE"),
        index_name = os.getenv("AZURE_INDEX"),
        credential = credential
    )

    return search_client

def get_response(query):
    model = "gpt-4o"

    grounded_prompt= """
    {query}
    Sources:\n{sources}
    """

    client = generate_client()
    search_client = generate_search()

    search_results = search_client.search(
        search_text = query,
        top = 5,
        select = "content",
        query_type = "semantic",
        semantic_configuration_name="default"
    )
    sources_formatted = "\n".join([res["content"] for res in search_results])

    response = client.chat.completions.create(
        model = model,
        messages = [
            {
            "role": "user",
            "content": grounded_prompt.format(query=query, sources=sources_formatted)
            }
        ],
    )
    return response.choices[0].message.content, sources_formatted

def user_input_response(user_input, column_no, section_purpose):
    query = f"A {column_no}-column Table must be generated from the response for the {section_purpose} for the client id {user_input}"
    response, sources_formatted = get_response(query)
    return response