FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip

COPY . .
RUN python -m pip install -r requirements.txt

EXPOSE 8000

# CMD ["./runserver"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]