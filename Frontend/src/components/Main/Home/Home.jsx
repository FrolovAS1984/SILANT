import { useAuth } from '../../../context/Auth.jsx';

import GeneralTable from './GeneralTable/GeneralTable.jsx';
import AuthTable from "./AuthTable/AuthTable.jsx";

import './Home.css';


function Home() {
  const { isAuthenticated } = useAuth();

  return (
    <div className="home">
        {isAuthenticated ? <AuthTable /> : <GeneralTable />}

    </div>
  );
}

export default Home;