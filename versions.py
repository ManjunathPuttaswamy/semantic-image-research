import importlib.metadata

packages = [
    # Core project dependencies
    "fastapi",
    "uvicorn",
    "streamlit",
    "coloredlogs",
    "pydantic",
    "requests",
    "python-dotenv",
    "python-multipart",
    
    # LangChain ecosystem
    "langchain-core",
    "langchain-community",
    "langchain-openai",
    "langchain-experimental",
    "langchain-astradb",
    "langchain-huggingface",
    
    # Model / Embeddings
    "huggingface_hub",
    "open_clip_torch",
    "torch",
    "pillow",
    "open_clip_torch",
    "torch",
    "python-multipart",
    "langchain-qdrant",

    # Development & utilities
    "ipython"
]

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg}=={version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg} (not installed)")
