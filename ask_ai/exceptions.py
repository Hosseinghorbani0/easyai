class AskAIError(Exception):
    """Base exception for all ask-ai errors."""
    pass

class APIKeyError(AskAIError):
    """Raised when API key is missing or invalid."""
    pass

class ProviderError(AskAIError):
    """Raised when the provider API fails (e.g. 500 error)."""
    pass

class MediaTypeNotSupportedError(AskAIError):
    """Raised when a provider can't handle the requested media type."""
    pass
