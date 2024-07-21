FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt
EXPOSE 8501:8501
CMD streamlit run application.py --server.port 8501
