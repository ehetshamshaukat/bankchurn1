FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN  pip install -r requirements.txt
EXPOSE 8501:8501
CMD streamlit run application.py