import React from 'react';

const SourceList = ({ sources }) => {
  if (!sources || sources.length === 0) return null;

  return (
    <div className="source-list">
      <h3>Sources</h3>
      <ul>
        {sources.map((source, index) => (
          <li key={index} className="source-item">
            <span className="source-file">{source.file}</span>
            <span className="source-page"> — Page {source.page}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default SourceList;
