import importlib.metadata

# ---------------------------------------------------------
# Grouped, deduplicated, and enhanced package list
# ---------------------------------------------------------
packages = [

    # -------------------------------
    # Core project dependencies
    # -------------------------------
    "fastapi",
    "uvicorn",
    "starlette",
    "requests",
    "coloredlogs",
    "structlog",
    "python-dotenv",
    "python-multipart",
    "typing_extensions",
    "anyio",
    "httpx",

    # -------------------------------
    # LangChain ecosystem
    # -------------------------------
    "langchain-core",
    "langchain-community",
    "langchain-openai",
    "langchain-experimental",
    "langchain-astradb",
    "langchain-huggingface",
    "langchain-qdrant",

    # -------------------------------
    # Vector DB / Embedding Models
    # -------------------------------
    "qdrant-client",
    "open_clip_torch",
    "huggingface_hub",
    "torch",
    "pillow",
    "numpy",
    "opencv-python",

    # -------------------------------
    # Utilities / Dev Tools
    # -------------------------------
    "streamlit",
    "ipython",
    "nest_asyncio",
    "tqdm"
]

# ---------------------------------------------------------
# Print versions
# ---------------------------------------------------------
print("\n🔍 Installed Package Versions:\n")

for pkg in packages:
    try:
        version = importlib.metadata.version(pkg)
        print(f"{pkg:<20} => {version}")
    except importlib.metadata.PackageNotFoundError:
        print(f"{pkg:<20} => NOT INSTALLED")

print("\n✅ Version check complete!\n")
