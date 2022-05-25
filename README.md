# Welcome to the User Browser #
User browser is an application that ingests a public API describing users. 
The application is broken into two parts, a ReactJs Frontend, and a FastAPI Python backend.

## Running ##
By cloning this repository you should have everything you need to get started. The project is backed by containerisation through Docker, making the process easier to get started. 
In theory, Github Actions builds the docker images when new commits are added to the repository. The two Docker images are labelled 'frontend' and 'backend'
Running from scratch, clone this repository into a directory on your local machine. Navigate to that directory. Please make sure you have Docker installed on your machine. Next, run 'docker compose build' and then 'docker compose up'. 
You should see some log messages appear, and at this point, in your browser you can go to: http://localhost:3000/ to browse the user list. The backend is running at http://localhost:8000/docs

If you get into trouble at any stage, please feel free to message: ttk_tech@outlook.com

<p> Happy browsing </b>
