from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI, MONGO_DB_NAME
from ..logging import LOGGER

LOGGER.info("🔗 Connecting to NexaMusic MongoDB...")

mongodb = None

try:
    if not MONGO_DB_URI:
        raise ValueError("MONGO_DB_URI is missing in config!")

    client = AsyncIOMotorClient(MONGO_DB_URI)

    # Use custom DB name if provided, else fallback
    db_name = MONGO_DB_NAME if "MONGO_DB_NAME" in globals() else "NexaMusic"
    mongodb = client[db_name]

    LOGGER.info(f"✅ Connected to MongoDB database: {db_name}")

except Exception as e:
    LOGGER.error(f"❌ Failed to connect to MongoDB: {e}")
    raise SystemExit