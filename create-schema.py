import os
import weaviate

# Connect to Weaviate instance (WCS)
client = weaviate.Client(
    url=os.getenv("WCS_URL"),
    auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv("WEAVIATE_API_KEY")),
    additional_headers={
        "X-OpenAI-Api-Key": os.getenv("OPENAI_API_KEY")
    }
)

assert client.is_ready()

# Define schema (classes for Article, Catagory, Author, Publication)
schema = {
    "classes" : [
        {
            "class" : "Article",
            "description" : "Article from; Financial Times, New York Times, Guardian, Wallstreet Journal, CNN, Fox News, The Economist, New Yorker, Wired, Vogue",
            "vectorizer" : "text2vec-openai",
            "moduleConfig" : {
                "text2vec-openai": {},
                "generative-openai": {}
            },
            "properties" : [
                {
                    "name" : "title",
                    "description" : "Title of the article",
                    "dataType": [
                        "text"
                    ],
                    "moduleConfig" : {
                        "text2vec-openai": {},
                        "generative-openai": {}
                    }
                },
                {
                    "name" : "url",
                    "description" : "url of the article",
                    "dataType": [
                        "text"
                    ],
                    "moduleConfig" : {
                        "text2vec-openai": {},
                        "generative-openai": {}
                    }
                },
                {
                    "name" : "summary",
                    "description" : "Summary of the article",
                    "dataType": [
                        "text"
                    ],
                    "moduleConfig" : {
                        "text2vec-openai": {},
                        "generative-openai": {}
                    }
                },
                {
                    "name" : "publicationDate",
                    "description" : "Date of publication of the article",
                    "dataType": [
                        "date"
                    ],
                    "moduleConfig" : {
                        "text2vec-openai": {},
                        "generative-openai": {}
                    }
                },
                {
                    "name" : "wordCount",
                    "description" : "Words in the article",
                    "dataType": [
                        "int"
                    ]
                },
                {
                    "name" : "authors",
                    "description" : "Authors of the article",
                    "dataType": [
                        "Author", "Publication"
                    ]
                },
                {
                    "name" : "publication",
                    "description" : "Publication of the article",
                    "dataType": [
                        "Publication"
                    ]
                },
                {
                    "name" : "catagory",
                    "description" : "Catagory of the article",
                    "dataType": [
                        "Catagory"
                    ]
                },
                {
                    "name" : "isAccessible",
                    "description" : "Whether the the article is accessible through the url",
                    "dataType": [
                        "boolean"
                    ]
                }
            ]
        },
        {
            "class" : "Category",
            "description": "Category article may be a type of",
            "vectorizer": "text2vec-openai",
            "moduleConfig" : {
                "text2vec-openai": {},
                "generative-openai": {}
            },
            "properties" : [
                {
                    "name" : "name",
                    "description" : "Name of category",
                    "dataType" : [
                        "text"
                    ],
                    "moduleConfig" : {
                        "text2vec-openai": {},
                        "generative-openai": {}
                    }
                }
            ]
        },
        {
            "class" : "Author",
            "description": "Author article may be written by",
            "vectorizer": "text2vec-openai",
            "moduleConfig" : {
                "text2vec-openai": {},
                "generative-openai": {}
            },
            "properties" : [
                {
                    "name" : "name",
                    "description" : "Name of author",
                    "dataType" : [
                        "text"
                    ],
                    "moduleConfig" : {
                        "text2vec-openai": {},
                        "generative-openai": {}
                    }
                },
                {
                    "name" : "articles",
                    "description" : "Articles written by the author",
                    "dataType" : [
                        "Article"
                    ]
                },
                {
                    "name" : "publication",
                    "description" : "Publicaiton author writes for",
                    "dataType" : [
                        "Publication"
                    ]
                }
            ]
        },
        {
            "class" : "Publicaiton",
            "description" : "Publication for articles with online source",
            "vectorizer": "text2vec-openai",
            "moduleConfig" : {
                "text2vec-openai": {},
                "generative-openai": {}
            },
            "properties" : [
                {
                    "name" : "name",
                    "description" : "Name of publicaiton",
                    "dataType" : [
                        "text"
                    ]
                },
                {
                    "name" : "hqGeoCoordinates",
                    "description" : "GeoLocaiton of publicaiton HQ",
                    "dataType" : [
                        "geoCoordinates"
                    ]
                },
                {
                    "name" : "articles",
                    "description" : "Articles belonging to publicaiton",
                    "dataType" : [
                        "Article"
                    ]
                }
            ]
        }
    ]
}

client.schema.delete_all()

client.schema.create(schema)