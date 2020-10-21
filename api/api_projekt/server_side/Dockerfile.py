FROM python:3.7-alpine
RUN python3 -m pip install flask gunicorn
COPY api.py .
EXPOSE 8000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "api:app"]
