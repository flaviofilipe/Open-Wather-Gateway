import React from 'react'
import { InputLine } from './style'

const InputSearch = ({ setCity }) => {
    
    const keyUp = event => {
        if(event.code === 'Enter'){
            console.log('up', event.target.value)
            setCity(event.target.value)
        }
    }

    return (
        <div id="search">
            <span>
                How is the weather in
                <InputLine
                    name="city" 
                    id="city" 
                    type="text"
                    onKeyUp={keyUp}/>
                now?
            </span>
        </div>
    );
}

export default InputSearch;