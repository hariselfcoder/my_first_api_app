FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy pydantic bcrypt python-jose[cryptography] python-dotenv passlib
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
