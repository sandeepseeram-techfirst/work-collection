from elasticsearch import Elasticsearch

esclient = Elasticsearch(['localhost:9200'])
response = esclient.search(
    index='social-*',
    body={
        "query": {
            "match": {
                "message": "myProduct"
            }
        },
        "aggs": {
            "top_10_states": {
                "terms": {
                    "field": "state",
                    "size": 10
                }
            }
        }
    }
)