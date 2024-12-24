const express = require('express');
const { CohereClientV2 } = require('cohere-ai'); // Cohere API
const app = express();

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Cohere API Setup
const cohere = new CohereClientV2({
    token: 'ves5auIvAhaJdlzuGTLB442wOQv3lUPPdMBal8n2', }); // Replace with your Cohere API key

// Serve Static Files
app.use(express.static('public'));

// Routes
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
});

app.post('/generate', async (req, res) => {
    const { genre, theme, characters } = req.body;
    try {
        const response = await cohere.generate({
            model: 'command-r-08-2024', // Use the Gemini model version, e.g., 'xlarge' for larger models
            prompt: `Generate a movie script. Genre: ${genre}, Theme: ${theme}, Characters: ${characters}.`,
            max_tokens: 300,
            temperature: 0.7,
        });

        if (response.statusCode === 200) {
            const script = response.body.generations[0].text;
            res.send(`<h1>Generated Script</h1><pre>${script}</pre>`);
        } else {
            console.error('Error generating script:', response.body);
            res.status(500).send('Error generating script. Please try again later.');
        }
    } catch (error) {
        console.error(error);
        res.status(500).send('Error generating script. Please try again later.');
    }
   
});

// Start Server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
