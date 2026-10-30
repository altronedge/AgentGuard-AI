"""Optional model adapters. The policy gateway remains independent of model vendors."""
from .config import settings


class ProviderNotConfigured(RuntimeError):
    pass


def openai_client():
    if not settings.openai_api_key:
        raise ProviderNotConfigured("Set OPENAI_API_KEY to enable OpenAI.")
    from openai import OpenAI
    return OpenAI(api_key=settings.openai_api_key)


def bedrock_client():
    if not settings.aws_bedrock_model_id:
        raise ProviderNotConfigured("Set AWS_BEDROCK_MODEL_ID to enable Bedrock.")
    import boto3
    return boto3.client("bedrock-runtime", region_name=settings.aws_region)
