FROM python:3.11-slim AS builder

WORKDIR /usr/src/app

RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip

COPY . .
RUN pip install -r requirements.txt --no-cache-dir 

FROM python:3.11-slim AS service
WORKDIR /root/app/site-packages
COPY --from=builder /venv /venv
ENV PATH=/venv/bin:$PATH

WORKDIR /usr/src/app
COPY --from=builder /usr/src/app/src/ .


ENTRYPOINT ["/venv/bin/uvicorn", "openapi_server.main:app", "--host", "0.0.0.0", "--port", "8080"]
