import React from 'react'
import InputSearch from '../../components/InputSearch'
import CityWeatherCard from '../../components/CityWeatherCard'
import { useState, useEffect } from 'react'
import NotFoundText from '../../components/NotFoundText'

import { Container } from './style'

const CITY_EXAMPLE = {
    "city": "London",
    "description": "broken clouds",
    "temperature": "9ºC"
}

const Home = () => {
    const [city, setCity] = useState();
    const [data, setData] = useState({});
    const [showNotFoundText, setShowNotFoundText] = useState(false)
    const [showCityCard, setShowCityCard] = useState(false)

    useEffect(() => {
        if(city){
            setData(CITY_EXAMPLE);
            setShowCityCard(true)
        }else{
            setShowCityCard(false)
        }
    }, [city])

    return (
        <Container>
            <h1>WEATHER BUDDY</h1>
            <InputSearch setCity={setCity} />
            <NotFoundText show={showNotFoundText} />
            <CityWeatherCard data={data} show={showCityCard} />
        </Container>
    );
}


export default Home;
