# Base image
FROM python

# Working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt ./
RUN apt autoremove && apt clean
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the whole app folder
COPY . .

# Run web server
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]