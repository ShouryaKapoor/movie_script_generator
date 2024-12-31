import React, { useState } from 'react';

const ScriptGenerator = () => {
    const [parameters, setParameters] = useState({
        genre: '',
        length: '',
        title: '',
    });
    const [script, setScript] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setParameters({ ...parameters, [name]: value });
    };

    const generateScript = async () => {
        const response = await fetch('/api/generate-script', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(parameters),
        });
        const data = await response.json();
        setScript(data.script);
    };

    return (
        <div>
            <h1>Movie Script Generator</h1>
            <input
                type="text"
                name="title"
                placeholder="Title"
                value={parameters.title}
                onChange={handleChange}
            />
            <input
                type="text"
                name="genre"
                placeholder="Genre"
                value={parameters.genre}
                onChange={handleChange}
            />
            <input
                type="text"
                name="length"
                placeholder="Length (in minutes)"
                value={parameters.length}
                onChange={handleChange}
            />
            <button onClick={generateScript}>Generate Script</button>
            <h2>Generated Script:</h2>
            <pre>{script}</pre>
        </div>
    );
};

export default ScriptGenerator;