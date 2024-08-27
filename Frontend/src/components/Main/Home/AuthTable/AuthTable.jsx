import {useState , useEffect , useCallback} from 'react';
import {useAuth} from '../../../../context/Auth.jsx';

import {Tabs , Tab} from 'react-bootstrap';



import axios from 'axios';

import './AuthTable.css';

import AllInfoTable from "./AllInfoTable/AllInfoTable.jsx";
import MaintenanceTable from "./MaintenanceTable/MaintenanceTable.jsx";

function AuthTable () {
    const { user , loading , logout , checkAuthStatus } = useAuth ();
    const [key , setKey] = useState ( 'general' );
    const [authChecked , setAuthChecked] = useState ( false );

    const verifyAuthStatus = useCallback ( async () => {
        const token = localStorage.getItem ( 'token' );
        if (token) {
            try {
                const response = await axios.get ( 'http://localhost:8000/accounts/check_auth_status/' , {
                    headers : {
                        'Authorization' : `Bearer ${token}`
                    }
                } );
                console.log ( response.data );
                if (!response.data.is_authenticated) {
                    logout ();
                } else {
                    setAuthChecked ( true );
                }
            } catch (error) {
                console.error ( 'Error checking auth status:' , error );
                logout ();
            }
        }
    } , [logout] );

    useEffect ( () => {
        verifyAuthStatus ();
    } , [verifyAuthStatus] );

    useEffect ( () => {
        if (!loading && !authChecked) {
            verifyAuthStatus ();
        }
    } , [loading , authChecked , verifyAuthStatus] );

    useEffect ( () => {
        console.log ( 'User:' , user );
    } , [user] );

    const displayUserInfo = () => {
        if (loading) return 'Загрузка данных...';
        if (!user) return '';

        let displayInfo = user.company_name || user.username;
        if (user.is_client && user.service_companies) {
            const serviceCompaniesDisplay = user.service_companies.join ( ', ' );
            displayInfo += ` / Сервисные компании: ${serviceCompaniesDisplay}`;
        }
        return displayInfo;
    };

    return (
        <div className="detailed-info-tabs-container">
            <h2 className="user-info">Пользователь: {displayUserInfo ()}</h2>
            <Tabs
                id="detailed-info-tabs"
                className="custom-tabs"
                activeKey={key}
                onSelect={(k) => {
                    checkAuthStatus ();  // Проверка авторизации при переключении вкладок
                    setKey ( k );
                }}
            >
                <Tab eventKey="general" title="Общая информация">
                    {key === 'general' && <AllInfoTable/>}
                </Tab>
                <Tab eventKey="maintenance" title="ТО">
                    {key === 'maintenance' && <MaintenanceTable/>}
                </Tab>
                {/*<Tab eventKey="complaints" title="Рекламации">*/}
                {/*    {key === 'complaints' && <ClaimsTab/>}*/}
                {/*</Tab>*/}
            </Tabs>
        </div>
    );
}

export default AuthTable;