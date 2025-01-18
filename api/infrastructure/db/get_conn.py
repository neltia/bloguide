from api.core.config import settings
from elasticsearch import AsyncElasticsearch


# Elasticsearch
def get_elasticsearch_client():
    es_host = settings.ES_HOST
    es_port = settings.ES_PORT
    is_secure = settings.ES_SECURE
    es_user = settings.ES_USER
    es_password = settings.ES_PW

    if not es_host.startswith("http"):
        host_list = get_host_list(es_host, es_port, is_secure=is_secure)
    else:
        host_list = es_host

    es_client = AsyncElasticsearch(
        hosts=host_list,
        basic_auth=(es_user, es_password) if es_user and es_password else None,  # Basic Authentication
        verify_certs=False,  # SSL/TLS 인증 무시 설정, Production에서는 사용 권장
        ssl_show_warn=False,
    )
    return es_client


def get_host_list(host_data, es_port, is_secure=True):
    protocol = "https" if is_secure else "http"

    host_list = list()
    if "," not in host_data:
        host_data = f"{protocol}://{host_data}:{es_port}"
        host_list.append(host_data)
        return host_list

    for host in host_data.split(","):
        host_data = f"{protocol}://{host}:{es_port}"
        host_list.append(host_data)
    return host_list


async def test_elasticsearch_connection():
    es_client = get_elasticsearch_client()
    try:
        if await es_client.ping():
            print("Elasticsearch connection successful.")
        else:
            print("Elasticsearch connection failed.")
    finally:
        await es_client.close()


if __name__ == "__main__":
    import asyncio
    asyncio.run(test_elasticsearch_connection())
