# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim


# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .

RUN python -m pip install -r requirements.txt
# add app
WORKDIR /app
COPY . .
EXPOSE 8000
# set working directory

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python","backend\main.py"]
# CMD python ./main.py

ENTRYPOINT ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
# ENTRYPOINT ["", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["python","main.py"]
# CMD gunicorn --bind 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker src.api:app
# CMD ["uvicorn", "-w 4","-k",uvicorn.workers.UvicornWorker,"api:app"]
