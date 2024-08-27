import './App.css'
import Header from "./components/Header/Header.jsx";
import Footer from "./components/Footer/Footer.jsx";
import Main from "./components/Main/Main.jsx";
import { AuthProvider } from './context/Auth.jsx';
import { BrowserRouter as Router } from 'react-router-dom';

function App() {


  return (
    <Router>
        <AuthProvider>

            <Header/>
            <Main />
            <Footer/>

        </AuthProvider>



    </Router>
  );
}

export default App
