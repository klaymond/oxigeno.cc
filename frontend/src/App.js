import { Header } from "./Componentes/Header";
import { Buscador } from "./Componentes/Buscador";
import { MainContent } from "./Componentes/MainContent";
import {Provider} from "react-redux"
import { store } from "./store/store";
import { Footer } from "./Componentes/Footer";



function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <Header />
        <Buscador />
        <MainContent />
        <Footer />
      </Provider>


    </div>
  );
}

export default App;
