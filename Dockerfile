FROM python:3.12-slim as builder


WORKDIR /Flix-API


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.12-slim


WORKDIR /Flix-API


COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin


COPY . .


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]