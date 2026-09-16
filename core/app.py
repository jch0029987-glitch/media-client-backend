import importlib
import pkgutil
from fastapi import FastAPI
import addons
from core.plugin_interface import MediaAddon

app = FastAPI(
    title="Media Client TV Backend",
    version="1.0.0",
    description="Self-hosted backend with modular add-on support."
)

def load_addons():
    """Dynamically discover and load all plugins in the addons package."""
    package = addons
    prefix = package.__name__ + "."
    for _, module_name, _ in pkgutil.walk_packages(package.__path__, prefix):
        module = importlib.import_module(module_name)
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, type) and issubclass(attribute, MediaAddon) and attribute is not MediaAddon:
                addon_instance = attribute()
                addon_instance.register_routes(app)
                print(f"Loaded Addon: {addon_instance.name} ({addon_instance.id})")

@app.on_event("startup")
async def startup_event():
    load_addons()

@app.get("/health")
async def health_check():
    return {"status": "online", "service": "media-client-backend"}
