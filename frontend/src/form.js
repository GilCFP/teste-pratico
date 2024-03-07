// DataForm.js
import React from 'react';
import { Button, Form, FloatingLabel } from 'react-bootstrap';
import { PropTypes } from 'prop-types';

function DataForm({ insertData }) {
  const submitForm = (e) => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const payload = Object.fromEntries(formData);
    const [year, month, day] = payload['date'].split("-");

    const requestData = {
      'password': "123456789",
      'day': day,
      'month': month,
      'year': year,
      'quantity': {
        'little': payload['little'] * 1,
        'big': payload['big'] * 1
      }
    };

    fetch('http://localhost:5000/api/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestData)
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Erro ao fazer a requisição');
        }
        return response.json();
      })
      .then(data => {
        insertData(data);
      })
      .catch(error => {
        console.error('Erro:', error);
      });
  };

  return (
    <>
      <h2 className='mt-5'>Preencha os Dados</h2>
      <form onSubmit={submitForm} className='mt-5'>

        <Form.Group className="mb-4" controlId='formBasicDate' >
          <FloatingLabel
            controlId='floatingInput'
            label="Data dos atendimentos"
            className='mb-3'>
            <Form.Control name='date' type='date' placeholder='dd/mm/aaaa' />
          </FloatingLabel>
        </Form.Group>

        <Form.Group className="mb-4">
          <FloatingLabel
            controlId='floatingInput'
            label="Quantidade de cães pequenos"
          >
            <Form.Control type="number" name="little" min="0" placeholder="Numero de Cachorros pequenos" />
          </FloatingLabel>
        </Form.Group>

        <Form.Group className="mb-4">
          <FloatingLabel
            controlId='floatingInput'
            label="Quantidade de cães grandes"
          >
            <Form.Control type="number" name="big" min="0" placeholder="Numero de Cachorros grandes" /></FloatingLabel>
        </Form.Group>

        <Button variant="outline-primary" type="submit">Enviar
        </Button>

      </form>
    </>
  );
}

DataForm.propTypes = {
  insertData: PropTypes.func.isRequired,
};

export default DataForm;
