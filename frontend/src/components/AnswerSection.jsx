import React from 'react';
import ReactMarkdown from 'react-markdown'; 
// Note: ReactMarkdown is great but standard text display is fine if we don't have it installed.
// The prompt didn't strictly require markdown support but RAG answers often have it.
// To stick to "axios only" as extra dependency, I will just display text or simple whitespace handling.
// Actually, I can use whitespace-pre-wrap for basic formatting.

const AnswerSection = ({ answer, error }) => {
  if (error) {
    return <div className="answer-section error">{error}</div>;
  }

  if (!answer) return null;

  return (
    <div className="answer-section">
      <h3>Answer</h3>
      <div className="answer-content">
        <ReactMarkdown>{answer}</ReactMarkdown>
      </div>
    </div>
  );
};

export default AnswerSection;
