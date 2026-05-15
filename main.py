from src.models.database import makeSession

print(makeSession())

# This error is Alembic’s way of saying: "Your database is stuck in the past."