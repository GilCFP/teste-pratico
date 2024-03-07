import './App.css'
import React from 'react'
import { Container, Row} from 'react-bootstrap'
import DataForm from './form'
function App() {

  return (
      <div className='App'>
        <Container class>
          <Row>
            <DataForm/>
          </Row>
          <Row id="Response-insert">
          </Row>
        </Container>
      </div>
  )
}

export default App