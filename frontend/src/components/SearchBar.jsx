import React, { useState } from 'react';

const SearchBar = ({ onSearch, isLoading }) => {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim() && !isLoading) {
      onSearch(query);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="search-bar">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask a question..."
        disabled={isLoading}
      />
      <button type="submit" disabled={isLoading || !query.trim()}>
        {isLoading ? '...' : 'Ask'}
      </button>
    </form>
  );
};

export default SearchBar;
