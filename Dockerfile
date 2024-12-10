FROM python:3.12-alpine as builder
WORKDIR /app
RUN python -m venv venv
COPY requirements.txt .
RUN /app/venv/bin/pip install -r requirements.txt

FROM python:3.12-alpine
WORKDIR /app
COPY --from=builder /app/venv /app/venv
ENV PATH=/app/venv/bin:$PATH
COPY . .
EXPOSE 8000
ENTRYPOINT [ "/app/docker-entrypoint.sh" ]