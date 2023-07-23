const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

// Simulando um banco de dados com um array de veículos
let veiculos = [
  {
    id: 1,
    marca: 'Toyota',
    modelo: 'Corolla',
    ano: 2022,
    preco: 100000,
  },
  {
    id: 2,
    marca: 'Honda',
    modelo: 'Civic',
    ano: 2021,
    preco: 95000,
  },
  // Adicione mais veículos aqui...
];

// Listar todos os veículos
app.get('/veiculos', (req, res) => {
  res.json(veiculos);
});

// Buscar veículo pelo ID
app.get('/veiculos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const veiculo = veiculos.find((v) => v.id === id);

  if (!veiculo) {
    res.status(404).json({ message: 'Veículo não encontrado' });
  } else {
    res.json(veiculo);
  }
});

// Adicionar um novo veículo
app.post('/veiculos', (req, res) => {
  const novoVeiculo = req.body;
  novoVeiculo.id = veiculos.length + 1;
  veiculos.push(novoVeiculo);
  res.json({ message: 'Veículo adicionado com sucesso', id: novoVeiculo.id });
});

// Atualizar um veículo pelo ID
app.put('/veiculos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  const veiculoAtualizado = req.body;
  const index = veiculos.findIndex((v) => v.id === id);

  if (index === -1) {
    res.status(404).json({ message: 'Veículo não encontrado' });
  } else {
    veiculos[index] = { ...veiculos[index], ...veiculoAtualizado };
    res.json({ message: 'Veículo atualizado com sucesso' });
  }
});

// Remover um veículo pelo ID
app.delete('/veiculos/:id', (req, res) => {
  const id = parseInt(req.params.id);
  veiculos = veiculos.filter((v) => v.id !== id);
  res.json({ message: 'Veículo removido com sucesso' });
});

const port = 3000;
app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
