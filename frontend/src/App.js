import './App.css'
import React from 'react'
import { Container, Row} from 'react-bootstrap'
import DataForm from './form'
import { useState, useEffect } from 'react'

function App() {

  const [response, setResponse] = useState(null);
  const [fade, setFade] = useState(false);

  const insertData = (data) => {
    setResponse(data);
  };

  useEffect(() => {
    if (response) {
      setFade(true);
      const timeout = setTimeout(() => {
        setFade(false);
      }, 500); // Tempo da animação

      return () => clearTimeout(timeout);
    }
  }, [response]);

  return (
    <div className='App'>
      <Container>
        <Row>
          <DataForm insertData={insertData} />
        </Row>
        <Row id="response-insert" className={`mt-4 ${fade ? 'fade-in-out' : ''}`}>
          {response && (
            <>O Petshop mais barato é <br /><b id='petshopname'>{response.name}</b><br />e o preço total é <br /><b id='price'>R${response.price}</b></>
          )}
        </Row>
      </Container>
    </div>
  );
}


export default App