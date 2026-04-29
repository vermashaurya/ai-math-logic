import React, { useState } from 'react';
import { Terminal, Code, Cpu, Info, X, Aperture } from 'lucide-react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import algorithmsData from './data/algorithms.json';
import './App.css';

function App() {
  const [selectedAlgo, setSelectedAlgo] = useState(null);

  const getIconForTag = (tag) => {
    switch (tag) {
      case 'Search': return <Terminal size={16} />;
      case 'Machine Learning': return <Cpu size={16} />;
      case 'Graph': return <Code size={16} />;
      default: return <Info size={16} />;
    }
  };

  return (
    <div className="app-container">
      <header className="hero glass-panel">
        <div className="hero-content">
          <div className="ai-core-container">
            <Aperture className="ai-core-icon" size={64} />
          </div>
          <h1 className="text-gradient">AI - Math Logic Challenges</h1>
          <p>A curated collection of classical AI, search, and logic algorithms implemented in Python.</p>
        </div>
      </header>

      <main className="grid-container">
        {algorithmsData.map((algo) => (
          <div key={algo.id} className="algo-card glass-panel" onClick={() => setSelectedAlgo(algo)}>
            <h2>{algo.title}</h2>
            <div className="tags">
              {algo.tags.map((tag) => (
                <span key={tag} className="tag">
                  {getIconForTag(tag)} {tag}
                </span>
              ))}
            </div>
            <div className="card-footer">
              <span>{algo.files.length} File{algo.files.length !== 1 ? 's' : ''}</span>
              <button className="view-btn">Preview</button>
            </div>
          </div>
        ))}
      </main>

      {selectedAlgo && (
        <div className="modal-overlay" onClick={() => setSelectedAlgo(null)}>
          <div className="modal-content glass-panel" onClick={(e) => e.stopPropagation()}>
            <div className="modal-header">
              <h2>{selectedAlgo.title}</h2>
              <button className="close-btn" onClick={() => setSelectedAlgo(null)}>
                <X size={24} />
              </button>
            </div>
            <div className="modal-body">
              {selectedAlgo.imageUrl && (
                <div className="preview-image-container">
                  <img src={selectedAlgo.imageUrl} alt={`${selectedAlgo.title} Preview`} className="preview-image" />
                </div>
              )}
              <div className="tags mb-4">
                {selectedAlgo.tags.map((tag) => (
                  <span key={tag} className="tag">
                    {getIconForTag(tag)} {tag}
                  </span>
                ))}
              </div>
              {selectedAlgo.files.map((file, idx) => (
                <div key={idx} className="code-block-container">
                  <div className="code-header">
                    <span className="file-name">{file.name}</span>
                  </div>
                  <SyntaxHighlighter
                    language="python"
                    style={vscDarkPlus}
                    customStyle={{
                      margin: 0,
                      borderRadius: '0 0 8px 8px',
                      background: '#1e1e1e',
                      fontSize: '14px',
                    }}
                  >
                    {file.content}
                  </SyntaxHighlighter>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
