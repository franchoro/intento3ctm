import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState, useEffect } from "react";


function Reglamento() {    // usestate for setting a javascript
    // object for storing and using data
    const [reglamento, setReglamento] = useState({
/*
        contenido_reg:"",
        fecha_reg:"",
        id_reg:"",
        nom_reg:""
*/


    });
    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from
        // flask server it will be redirected to proxy
        fetch("/reglamento",{'methods':'GET'}).then((res) =>
            res.json().then((reglamento) => {
                console.log(reglamento);
                console.log(typeof reglamento);
                // Setting a data from api


                setReglamento({reglamento
                });
            })
        );
    }, []);

function child({data}){
    return(
        <pre>
            {JSON.stringify(data,null,2)}
        </pre>
    )
};
    
    return (
        <div className="App">
            <header className="App-header">
                <child data={reglamento}/>
                <h1>React and flask</h1>
                {/* Calling a data from setdata for showing */}
                <p>{JSON.stringify(reglamento,null,2)} hola</p>

                <div>
                    {Object.keys(reglamento).map((key) => (
                        <div key={key}>
                        <strong>{key}: </strong>
                        {reglamento[key]}
                        </div>
                    ))}
                </div>
            

                {/*
                <ul>
                    {Object.entries(reglamento).map(([key,value])=>(
                    <li key={key}>
                        {key}
                        {Array.isArray(value) ? (
                        <ul>
                            {value.map((item,index)=>(
                                <li key={index}>{item}</li>
                            ))}
                        </ul>
                        ) : (
                            value
                        )}
                    </li>))}
                </ul>

                */}
                <p>{reglamento.contenido_reg1}</p>
                <p>{reglamento.nom_reg1}</p>
                <p>{reglamento.fecha_reg1}</p>
    
            </header>
        </div>
    );
}

export default Reglamento;
