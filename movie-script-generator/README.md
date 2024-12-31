# Movie Script Generator

This project is a full-stack application that utilizes Google Generative AI to generate movie scripts. It consists of a backend built with Flask and a frontend developed using React.

## Project Structure

```
movie-script-generator
├── backend
│   ├── app.py                # Entry point for the backend application
│   ├── requirements.txt      # Backend dependencies
│   ├── models                # Directory for data models
│   │   └── __init__.py
│   ├── routes                # Directory for API routes
│   │   └── __init__.py
│   └── services              # Directory for services interacting with Google Generative AI
│       └── google_generative_ai.py
├── frontend
│   ├── public
│   │   └── index.html        # Main HTML file for the frontend application
│   ├── src
│   │   ├── App.js            # Main component of the React application
│   │   ├── components
│   │   │   └── ScriptGenerator.js # Component for generating scripts
│   │   ├── styles
│   │   │   └── App.css       # CSS styles for the React application
│   │   └── index.js          # Entry point for the React application
│   ├── package.json          # Configuration file for npm
│   └── README.md             # Documentation for the frontend application
├── README.md                 # Overview of the entire project
└── .gitignore                # Files and directories to ignore in version control
```

## Backend Setup

1. Navigate to the `backend` directory.
2. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
3. Run the backend application:
   ```
   python app.py
   ```

## Frontend Setup

1. Navigate to the `frontend` directory.
2. Install the required dependencies using:
   ```
   npm install
   ```
3. Start the frontend application:
   ```
   npm start
   ```

## Usage

Once both the backend and frontend are running, you can access the application in your web browser. Use the Script Generator component to input parameters and generate movie scripts using Google Generative AI.

## License

This project is licensed under the MIT License.