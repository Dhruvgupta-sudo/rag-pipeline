import React, { useState } from 'react';
import axios from 'axios';
import SearchBar from './components/SearchBar';
import AnswerSection from './components/AnswerSection';
import SourceList from './components/SourceList';
import './index.css';

function App() {
  const [answer, setAnswer] = useState('');
  const [sources, setSources] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async (query) => {
    setIsLoading(true);
    setError('');
    setAnswer('');
    setSources([]);

    try {
      const response = await axios.post('http://localhost:8000/query', {
        question: query
      });

      setAnswer(response.data.answer);
      setSources(response.data.sources);
    } catch (err) {
      console.error(err);
      setError('Failed to fetch answer. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="app-header">
        <h1>RAG Knowledge Assistant</h1>
      </header>
      
      <main className="app-main">
        <SearchBar onSearch={handleSearch} isLoading={isLoading} />
        
        {isLoading && <div className="loading-indicator">Thinking...</div>}
        
        <AnswerSection answer={answer} error={error} />
        <SourceList sources={sources} />
      </main>
    </div>
  );
}

export default App;
