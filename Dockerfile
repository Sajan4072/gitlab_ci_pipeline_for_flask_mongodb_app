#Define the OS of the container
FROM python:3.12-alpine

#Define the location to copy the project files
#put everything in root / is root
WORKDIR /

#copy the files into the owrking directory . is everything to the container
COPY . .

#to install packages (requirements)

RUN pip install -r requirements.txt

#opening the port 5000 on the docker engine
EXPOSE 5000

#to run the application
CMD ["python","main.py"]


