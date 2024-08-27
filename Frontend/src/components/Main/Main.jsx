import { Route, Routes } from 'react-router-dom';
import styles from './Main.module.css';
import Home from './Home/Home.jsx';
import AuthPage from './AuthPage/AuthPage';
import References from "./Home/References/References.jsx";


function Main() {

    return (
        <main className={styles.main_container}>
            <div className="main-content">
                <Routes>
                    <Route path={'/'} element={<Home />}/>
                    <Route path={'/login'} element={<AuthPage />}/>
                    <Route path="/reference/:directoryName/:name" element={<References />} />
                </Routes>

            </div>
        </main>
    );
}

export default Main;