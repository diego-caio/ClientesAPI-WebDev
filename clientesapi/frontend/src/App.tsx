import {useState} from 'react';
import ClientePython from './components/ClientePython'
import ClienteApi from './components/ClienteApi'

//Define os tipos possiveis para aba ativa
type TabType = 'python'| 'api';

const App = () => {
  //Hook useState
  const [activeTab,setActiveTab] = useState<TabType>('python')

  return (
     <div className="min-h-screen bg-gray-100 p-6 font-sans">
      <div className="max-w-3xl mx-auto bg-white rounded-xl shadow-md overflow-hidden p-6">
        
        {/* Título Principal */}
        <h1 className="text-2xl font-bold text-gray-800 mb-4 text-center">
          Painel Simples Clientes
        </h1>

        {/* Botões de Navegação entre Abas */}
        <div className="flex justify-center space-x-4 mb-6 border-b pb-4">
          <button
            onClick={() => setActiveTab('python')}
            className={`px-4 py-2 rounded-lg font-medium transition ${
              activeTab === 'python'
                ? 'bg-blue-600 text-white'
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`}
          >
            Clientes (Python)
          </button>
          <button
            onClick={() => setActiveTab('api')}
            className={`px-4 py-2 rounded-lg font-medium transition ${
              activeTab === 'api'
                ? 'bg-blue-600 text-white'
                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
            }`}
          >
            API Externa
          </button>
        </div>

        {/* Renderização Condicional dos Componentes */}
        {activeTab === 'python' && <ClientePython />}
        {activeTab === 'api' && <ClienteApi />}

      </div>
    </div>
  )
}

export default App
