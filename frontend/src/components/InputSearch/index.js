import React from 'react'
import { InputLine } from './style'

const InputSearch = () => {
    return (
        <div id="search">
            <span>How is the weather in <InputLine name="city" id="city" class="text-line" onchange="find_city()"/> now?</span>
        </div>
    );
}

export default InputSearch;