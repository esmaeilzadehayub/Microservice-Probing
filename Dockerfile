FROM python:3.7-slim 

# Install test dependencies
RUN pip install requests

# Copy the test application
COPY test_application.py /

# Run the test application
ENTRYPOINT ["python", "/test_application.py"]